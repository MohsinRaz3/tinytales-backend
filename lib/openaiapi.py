from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are a story generator in a paragraph format based on user-provided text prompts. When the user provides a brief text input, such as a theme, character, or setting, create a detailed story script that includes dialogue, narration, and vivid descriptions. The story should not be more than 450 words "
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "oceanic flight 815 surviours"
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

print(assistant_response)