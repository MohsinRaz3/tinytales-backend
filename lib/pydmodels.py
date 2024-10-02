from pydantic import BaseModel, HttpUrl
from typing import List, Dict

class StoryTitle(BaseModel):
    title: str

class StoryDescription(BaseModel):
    description_1: str = None
    description_2: str = None
    description_3: str = None

class StoryData(BaseModel):
    title: str

class StoryModel(BaseModel):
    story_data: StoryData
    description: List[Dict[str, str]]

class GetStoryData(BaseModel):
    story_idea: str
    age_group:str
    genre:str
    characters:str
    
    
class GeneratedStoryModel(BaseModel):
    get_story: GetStoryData
    get_audio : str
    get_images: list[str] 
    
    
# Final Output respone model

class FluxImagesUrl(BaseModel):
    image_urls: List[HttpUrl]

class StoryResult(BaseModel):
    story_title: str
    story_des_1: str
    story_des_2: str
    story_des_3: str
    flux_images_url: FluxImagesUrl
    audio_url: HttpUrl

class StoryResponse(BaseModel):
    result: StoryResult
