from fastapi import FastAPI, HTTPException
from lib.openaiapi import story_generator
from lib.pydmodels import GetStoryData, StoryResponse

app = FastAPI(title="TinyTales", description="Story generator for kids", version="0.0.1")

@app.get("/", tags=["Story Creation"])
def root():
    return "tiny tales"


@app.post("/story_creation", tags=["Story Creation"], response_model=StoryResponse)
async def generate_story(story_data: GetStoryData):
    try:
        generated_story = await story_generator(
            story_data.story_idea, 
            story_data.age_group, 
            story_data.genre, 
            story_data.characters
        )
        return {"result": generated_story}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")