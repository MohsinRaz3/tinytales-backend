import os
import asyncio
import fal_client
from fastapi import HTTPException

FAL_API_KEY = os.getenv('FAL_API')

async def flux_image_gen(user_prompts: list[str]):
    try:
        image_urls = []  # Initialize a list to hold the image URLs

        for prompt in user_prompts:  # Iterate over each prompt
            handler = await fal_client.submit_async(
                "fal-ai/flux/schnell",
                arguments={"prompt": prompt},  # Use the current prompt
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

            # Assuming you want to get the first image URL from each result
            image_urls.append(result['images'][0]['url'])

        return {"image_urls": image_urls}  # Return all generated image URLs

    except fal_client.FalClientError:
        raise HTTPException(status_code=500, detail="Failed to communicate with the image generation service")
    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


async def image_result():
    image_results = await flux_image_gen(["A beautiful sunset", "A futuristic city", "A serene forest"])
    print(image_results)  # This will print the URLs of the generated images
asyncio.run(image_result())