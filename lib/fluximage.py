import fal_client
from dotenv import load_dotenv
import os

load_dotenv()

FAL_API_KEY = os.getenv('FAL_API')
async def subscribe(prompts):
    image_urls = []

    async def generate_image(prompt):
        # Submitting the job to fal_client
        handler = await fal_client.submit_async(
            "fal-ai/flux/schnell",
            arguments={"prompt": prompt}
        )

        # Handle the streaming of logs or progress (if supported)
        log_index = 0
        async for event in handler.iter_events(with_logs=True):
            if isinstance(event, fal_client.InProgress):
                new_logs = event.logs[log_index:]
                for log in new_logs:
                    print(log["message"])
                log_index = len(event.logs)

        # Get the result after completion
        result = await handler.get()
        if 'images' in result and result['images']:
            image_urls.append(result['images'][0]['url'])
        else:
            print(f"No image generated for prompt: {prompt}")

    # Loop through each prompt and generate an image
    for prompt in prompts:
        await generate_image(prompt)

    return image_urls
