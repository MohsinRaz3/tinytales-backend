from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Optional

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
    
    

class FluxImagesUrl(BaseModel):
    image_urls: Optional[List[HttpUrl]] = None  

class StoryResult(BaseModel):
    story_title: Optional[str] = None  
    story_des_1: Optional[str] = None  
    story_des_2: Optional[str] = None  
    story_des_3: Optional[str] = None 
    flux_images_url: Optional[FluxImagesUrl] = None  
    audio_url: Optional[HttpUrl] = None 

class StoryResponse(BaseModel):
    result: Optional[StoryResult] = None  