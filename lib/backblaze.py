#backblaze integration 
# https://github.com/Backblaze/b2-sdk-python

import os
import io
import uuid
from dotenv import load_dotenv
from b2sdk.v2 import InMemoryAccountInfo, B2Api
from fastapi import HTTPException


async def upload_b2_storage(audio_data: io.BytesIO, file_name: str, content_type: str):
    APPLICATION_KEY_ID_MP = os.getenv('APPLICATION_KEY_ID_MP')
    APPLICATION_KEY_MP = os.getenv('APPLICATION_KEY_MP')
    try:
        info = InMemoryAccountInfo()
        b2_api = B2Api(info)
        b2_api.authorize_account('production', APPLICATION_KEY_ID_MP, APPLICATION_KEY_MP)

        bucket_name = os.getenv('BUCKET_NAME_MP')
        bucket = b2_api.get_bucket_by_name(bucket_name)

        # Upload file content to B2 storage
        bucket.upload_bytes(
            audio_data.getvalue(),
            file_name,
            content_type=content_type
        )

        bucket_url = os.getenv('BUCKET_URL')
        file_url = f"{bucket_url}/{file_name}"
        return file_url
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload failed: {e}")
    