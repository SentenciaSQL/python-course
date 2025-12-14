user = {
    "name": "Andres",
    "age": 25,
    "greet": "Hola Mundo",
    "numbers": [1, 2, 3]
}

# .get()
print(user.get("name"))

# in
print('name' in user)
print('name' in user.keys())
print(user.keys())
print('Andres' in user.values())
print(user.values())

print(user.items())

