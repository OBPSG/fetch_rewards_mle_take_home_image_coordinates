from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/image_coordinates/")
async def intro():
    return {"message": "Use Postman, a similar web API driver, or navigate to the /docs# endpoint to make a POST request"}

