from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os


class Item(BaseModel):
    url: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ping")
async def root(data: Item):
    url = data.url
    command = "dig " + url
    stream = os.popen(command)
    output = stream.readlines()
    return output


@app.get("/")
async def root():
    return {"message": "Hello World"}
