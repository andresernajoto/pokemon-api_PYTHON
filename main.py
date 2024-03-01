import os
import requests

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from os.path import join, dirname

app = FastAPI(title='Pokemon API')
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base_url = os.environ.get('BASE_URL')

@app.get('/pokemon/get-all')
def get_all():
    try:
        pokemon_route = base_url + 'pokemon/'

        response = requests.get(pokemon_route)

        return response.json()
    except:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get('/pokemon/get-pokemon')
def get_pokemon(pokemon: str):
    try:
        pokemon_route = base_url + 'pokemon/' + pokemon.strip()

        response = requests.get(pokemon_route)
        
        return response.json()
    except:
        raise HTTPException(status_code=response.status_code, detail=response.text)