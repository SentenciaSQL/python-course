import json

users = {
    "nombre": "Andres",
    "edad": 29,
    "activo": True,
}

with open("datos.json", "w") as file:
    json.dump(users, file)

with open("datos.json", "r") as file:
    users = json.load(file)
    print(users)