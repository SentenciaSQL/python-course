import csv

with open("datos.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Andres", 37])
    writer.writerow(["Jose", 25])
    writer.writerow(["Leandro", 29])

with open("datos.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)