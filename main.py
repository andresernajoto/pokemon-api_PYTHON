import os
import requests

from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from os.path import join, dirname

app = FastAPI()
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

base_url = os.environ.get('BASE_URL')

@app.get('/pokemon/get-all')
def get_all():
    try:
        response = requests.get(base_url)

        if response.status == 200:
            return response.json()
    except:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get('/pokemon/get-pokemon')
def get_pokemon(pokemon: str):
    try:
        response = requests.get(base_url, pokemon)

        if response.status_code == 200:
            return response.json()
        
    except:
        raise HTTPException(status_code=response.status_code, detail=response.text)