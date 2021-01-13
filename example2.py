from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None


app = FastAPI()


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.post("/package{priority}")
async def makes(priority:int ,package: Package,value:bool):
    return {"priority":priority,**package.dict(),"value":value};
