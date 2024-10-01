from pydantic import BaseModel
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
    get_udio : str
    get_images: list[str] 