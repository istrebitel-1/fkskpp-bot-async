from fastapi import FastAPI
from json import dumps, dump, load

app = FastAPI()

@app.get("/")
async def root():

    return '<h3 align="middle">ФКСКПП БОТЯРА ЛЮТЫЙ</h3>'

    
from src.bot import config
from . import routes