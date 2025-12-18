try:
    with open("sinpermisos.txt", mode="r") as file:
        content = file.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tiene permisos para abrir el archivo")
except Exception as err:
    print(f"ocurrio un archivo error: {err}")