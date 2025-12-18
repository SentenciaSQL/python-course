# Realive path
with open("fileFolder/relative.txt", mode="r") as my_file:
    print(my_file.readlines())

# absolute path
with open("C:/Users/PC/Documents/python/python-course/archivos/archivo.txt", mode="r") as my_file:
    print(my_file.readlines())