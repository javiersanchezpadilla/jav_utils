""" UN DICCIONARIO GUARDA PARES DE CLAVE :  VALOR

    Se usa cuando necesitas identificar datos por nombre
    Usa diccioario para estados o configuraciones

    jugador = { "nombre" : "Alex, "vidas": 100, "nivel" : 5}

    print(jugador["vida"])      # 100

"""
contactos = {}

for i in range(2):
    nombre = input("Introduce el nombre :")
    telefono = input("Introduce telefono: ")
    contactos[nombre] = telefono

print("Your contacts:")
for nombre, telefono in contactos.items():
    print(nombre, "->", telefono)
