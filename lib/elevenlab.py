from elevenlabs import ElevenLabs, VoiceSettings
import os
import io
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ELEVENLABS_KEY")

async def audio_generator(story) -> io.BytesIO:
    client = ElevenLabs(
        api_key=api_key,
    )
    response = client.text_to_speech.convert(
        voice_id="jsCqWAovK2LkecY7zXl4",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=story,
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.0,
            use_speaker_boost=False,
        ),
    )
    
    audio_data = io.BytesIO()
    for chunk in response:
        if chunk:
            audio_data.write(chunk)
    audio_data.seek(0) 
    return audio_data
