from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get('/pokemon/get-all')
def get_all():
    try:
        base_url = 'https://pokeapi.co/api/v2/'

        response = requests.get(base_url)

        if response.status == 200:
            return response.json()
    except:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get('/pokemon/get-pokemon')
def get_pokemon(pokemon: str):
    try:
        base_url = 'https://pokeapi.co/api/v2/'

        response = requests.get(base_url, pokemon)

        if response.status_code == 200:
            return response.json()
        
    except:
        raise HTTPException(status_code=response.status_code, detail=response.text)