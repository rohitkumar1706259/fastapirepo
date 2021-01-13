import uvicorn
import fastapi

api=fastapi.FastAPI()

@api.get("/")
async def index():
    return {
        "message":"Hello World",
        "status":"OK"
    }
uvicorn.run(api);