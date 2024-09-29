from openaiapi import story_generator
from elevenlabs import ElevenLabs, VoiceSettings
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("ELEVENLABS_KEY")


def audio_generator(story):

    client = ElevenLabs(
        api_key=api_key,
    )
    
    response = client.text_to_speech.convert(
        voice_id="jsCqWAovK2LkecY7zXl4",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=story,
        voice_settings=VoiceSettings(
            stability=0.1,
            similarity_boost=0.3,
            style=0.2,
        ),
    )

    # The response is a generator, so we need to iterate through it to get the audio data
    audio_data = b"".join(response)  # Concatenating all chunks into a single byte string
    
  
    with open("output_audio.mp3", "wb") as audio_file:
        audio_file.write(audio_data)

    print("Audio file generated successfully!")
    return "output_audio.mp3"



story = story_generator("car", "thrill", "horror")

audio_generator(story)
