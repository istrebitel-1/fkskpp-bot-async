from fastapi import FastAPI
from json import dumps, dump

app = FastAPI()

@app.get("/")
async def root():
    return {'version':f"{config['version']}"}


from src.bot import config
