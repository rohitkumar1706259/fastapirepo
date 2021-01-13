from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class PackageIN(BaseModel):
    secret: int
    name: str
    number: str
    description: Optional[str] = None


class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None


app = FastAPI()


@app.get("/")
async def hello_world():
    return {"Hello": "World"}


@app.post("/package/",response_model=Package,response_model_exclude_unset=True)
async def makes(package: PackageIN):
    return package
