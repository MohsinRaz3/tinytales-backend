import os
import json
import uuid
import openai
import asyncio
from openai import OpenAI
from dotenv import load_dotenv
from lib.backblaze import upload_audio
from lib.elevenlab import audio_generator
from lib.fluximage import flux_image_gen

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key  
client = OpenAI()

################  GENERATE PROMPTS FLUXAI IMAGES  ##########################
async def prompt_gen(list_of_prompts:list[str]):
    system_message = {"role": "system", "content": "You are a helpful assistant that generates image prompts for fluxai.  Image prompt should be under 60 words."}
    generated_prompts = []

    for i, prompt_string in enumerate(list_of_prompts, 1):
        user_message = {
            "role": "user",
            "content": f"Here is text string {i}: '{prompt_string}'. Please generate an image prompt based on this string. Image prompt should be under 60 words."
        }
        completion = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                system_message,
                user_message
            ]
        )
        generated_prompt = completion.choices[0].message.content
        generated_prompts.append(generated_prompt) 
    return generated_prompts

#######################  GENERATE STORY  #####################
async def story_generator(story_idea, age_group, genre, characters):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-2024-08-06", 
            messages=[
                {
                    "role": "system",
                    "content": """
You are a story generator in a paragraph format based on user-provided text prompts. You generate engaging, vivid stories for kids based on their age group, genre, characters, and story idea. Your goal is to create fun, imaginative stories that sentences have proper pauses, punctuations and are age-appropriate.

    For kids aged 3-5: Use simple language, repetition, and a gentle tone with basic descriptions.
    For kids aged 6-8: Add a sense of adventure, some problem-solving, and slightly more complex descriptions.
    For kids aged 9-11: Include more detailed descriptions, a complex plot, and elements of mystery or excitement.

Each story should contain a single title and one script description. The script description should be divided into 3 distinct segments: starter, middle, and ending. These segments should flow seamlessly without any additional titles or headings separating them.

Ensure the story is no more than 600 words, with a balance of dialogue, narration, and vivid imagery to captivate young readers.
"""
                },
                {
                    "role": "user",
                    "content": f"""
Age group: {age_group}
Genre: {genre}
Characters: {characters}
Story Idea: {story_idea}

Please generate a fun and engaging story based on the above information, suitable for the selected age group. Your generated output should be in JSON format and it should look like this:
{{
    "story_data": {{
        "title": " Luna and the Lost Star"
    }},
    "description": [
        {{"description_1": "One quiet night, a little girl named Luna gazed up at the sky. She loved watching the stars twinkle and wondered about the stories they told. But tonight, something was different. A star was missing! Luna gasped, “Where could it have gone?”"}},
        {{"description_2": "Determined to find the lost star, Luna grabbed her magical telescope and set off on an adventure. She soared through the sky on a silver cloud, passing glowing planets and swirling comets. As she floated deeper into the stars, she heard a tiny voice crying, "Help!" Luna followed the sound and found the missing star, trapped in a thick cloud of darkness. "Don't worry," she said bravely, "I'll save you!"

Luna reached into her pocket and pulled out a glowing crystal her grandmother had given her. Holding it high, she whispered a magical word, and the crystal lit up the sky. The darkness melted away, freeing the star. The star beamed with joy and danced around Luna in thanks. "I knew you'd come!" it twinkled. Together, they returned to the sky, where the star shined even brighter than before."}},
        {{"description_3": "Back home, Luna lay in bed, smiling. She had saved the star and learned that sometimes, even the smallest voices need the biggest hearts to hear them. As she drifted off to sleep, the stars above twinkled their thanks, lighting up the night in a magical glow. Luna closed her eyes, dreaming of her next adventure among the stars."}}
    ]
}}
"""
                },
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            response_format={"type": "json_object"}
        )

        assistant_response = response.choices[0].message
        if assistant_response:
          response_json = json.loads(assistant_response.content)
          
          story_title = response_json['story_data']['title']
          story_des_1 = response_json['description'][0]['description_1']
          story_des_2 = response_json['description'][1]['description_2']
          story_des_3 = response_json['description'][2]['description_3']
          print("01_ story_title", story_title,"story_des_1",story_des_1,"story_des_2",story_des_2,"story_des_3",story_des_3)
         
          img_prompt_res = await prompt_gen(list_of_prompts=[story_des_1,story_des_2,story_des_3])
         # print("02_ story prompt ", img_prompt_res)
          
          image_results = await flux_image_gen(img_prompt_res)
         # print("03_flux_image",image_results)
           
          result_result = [response_json['description'][0]['description_1'], response_json['description'][1]['description_2'],response_json['description'][2]['description_3']]
          audio_script  = " ".join(result_result)
          
          audio_file = await audio_generator(audio_script)
          file_name = f"RT{uuid.uuid4()}.mp3"
          backblaze_bucket = await upload_audio(audio_file,file_name, content_type="audio/mpeg")
          #print("04_ backblaze bucket", backblaze_bucket)
          story_output = {"story_title" : story_title,"story_des_1":story_des_1,"story_des_2":story_des_2,"story_des_3":story_des_3, "flux_images_url" : image_results, "audio_url": backblaze_bucket}
          print(story_output)
          return story_output
        else:
          print(assistant_response)

    except Exception as e:
        print(f"Error during API call: {e}")
        return None

