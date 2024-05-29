import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = "cbb020f3aa57af9ce38bd32dccb5ddb8"
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = '4278'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Driller'


@pytest.mark.parametrize('key, value', [('name', 'Driller'), ('trainer_id', TRAINER_ID), ('id', '28611')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value