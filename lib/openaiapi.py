from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")



def story_generator(title,genra,type):
  
  client = OpenAI()

  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
        "role": "system",
        "content": [
          {
            "type": "text",
            "text": "You are a story generator in a paragraph format based on user-provided text prompts. When the user provides a brief text input, such as a theme, character, or setting, create a detailed story script that includes dialogue, narration, and vivid descriptions. The story should not be more than 200 words "
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": f"Create a story title: {title} | Genra: {genra} | Type: {type}"
          }
        ]
      },
    ],
    temperature=1,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
      "type": "text"
    }
  )

  assistant_response = response.choices[0].message.content
  
  return assistant_response


