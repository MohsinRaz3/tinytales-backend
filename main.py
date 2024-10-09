from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse
from lib.openaiapi import story_generator
from lib.pydmodels import GetStoryData, StoryResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TinyTales", description="Story generator for kids", version="0.0.1", docs_url="/docs", redoc_url="/redoc",   openapi_url="/openapi.json" )

# origins = [
#     "https://tinytales-lablab.vercel.app",
#     "http://localhost:3000",
#     "http://localhost:3000/",
# ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/", tags=["Story Creation"])
def root():
    return "tiny tales"


@app.post("/story_creation", tags=["Story Creation"],response_model=StoryResponse)
async def generate_story(story_data: GetStoryData = Body(...))-> dict:
    try:
        generated_story = await story_generator(
            story_data.story_idea, 
            story_data.age_group, 
            story_data.genre, 
            story_data.characters
        )
        data  = {"result": generated_story}
        return JSONResponse(content=data)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")