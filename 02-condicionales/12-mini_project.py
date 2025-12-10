name = input("Nombre del candidato: ")
experience = int(input("Experiencia del candidato: "))
skills = input("Ingrese sus habilidades separadas por comas (ej. Python, Laravel, Golang, Django, etc.): ")
skills = skills.split(",")

evaluate_skills = "Python" in skills or "Django" in skills

if evaluate_skills:
    if experience >= 3:
        result = "Candidato optiomo"
    elif experience >=  1:
        result = "Buen optiomo"
    else:
        result = "Posible Candidato"
else:
    result = "No apto, se guardara CV para futuras ofertas"

print(f"el candidato {name} es: {result}")