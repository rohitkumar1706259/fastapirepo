from fastapi import FastAPI

app=FastAPI()
@app.get("/")
async def hello_world():
    return {"Hello":"World"}

@app.get("/component/{comp_id}") #parameter
#async def component(comp_id):
async def component(comp_id:int):
    return {"Hello":comp_id}

#query paramter
@app.get("/component/")
async def runit(number:int,text:str):
    return {"number":number,"text":text}
