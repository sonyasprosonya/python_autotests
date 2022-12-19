import requests
import json

token = '047808d6851c39fdd3697c9808328525'
# создать покемона
response1 = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "name": "Material Gworl", 
    "photo": "https://w7.pngwing.com/pngs/277/568/png-transparent-pink-m-animated-cartoon-others-magenta-pink-m-pokemon.png"
})

response1_pretty = json.dumps(response1.json(), indent=4, ensure_ascii=False)
print(response1_pretty)

# изменить покемона
response2 = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": 2547,
    "name": "Chuu",
    "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmNGwnhNyZz6K2dn9v_tr49bF89lbfsHJT-A&usqp=CAU"
})

response2_pretty = json.dumps(response2.json(), indent=4, ensure_ascii=False)
print(response2_pretty)

# поймать покемона в покебол
response3 = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": 2547
})

response3_pretty = json.dumps(response3.json(), indent=4, ensure_ascii=False)
print(response3_pretty)
