import os
import asyncio
import fal_client
from fastapi import HTTPException
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FAL_KEY = os.getenv('FAL_KEY')

async def flux_image_gen(user_prompts):
    try:
        image_urls = []
        for prompt in user_prompts:
            handler = await fal_client.submit_async(
                "fal-ai/flux/schnell",
                arguments={"prompt": prompt},  
            )

            log_index = 0
            async for event in handler.iter_events(with_logs=True):
                if isinstance(event, fal_client.InProgress):
                    new_logs = event.logs[log_index:]
                    for log in new_logs:
                        print(log["message"])
                    log_index = len(event.logs)

            result = await handler.get()
            if 'images' not in result or not result['images']:
                raise HTTPException(status_code=500, detail="No images returned from the API for prompt: {}".format(prompt))

            image_urls.append(result['images'][0]['url'])
            await asyncio.sleep(3)  # Delay

        return {"image_urls": image_urls}  

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")  # Log the error message
        raise HTTPException(status_code=500, detail="An unexpected error occurs")
