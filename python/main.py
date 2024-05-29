import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = "cbb020f3aa57af9ce38bd32dccb5ddb8"
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "texiker807@huleos.com",
    "password": "1234554321Q"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Driller",
    "photo": "https://dolnikov.ru/pokemons/albums/459.png"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)