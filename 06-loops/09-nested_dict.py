nested_dict = {
    "Persona1": { "Nombre": "Andres", "edad": 30, "ciudad": "Santo Domingo" },
    "Persona2": { "Nombre": "Ricardo", "edad": 29, "ciudad": "Ciudad de Mexico" },
    "Persona3": { "Nombre": "Ana", "edad": 34, "ciudad": "San Juan" },
}

for key, value in nested_dict.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")