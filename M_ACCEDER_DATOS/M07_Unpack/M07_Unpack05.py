""" LA mejor forma de acceder a los datos.

    En este ejercicios accederemos a los datos de dos maneras, la tradicional
    y mediante desempaquetamiento.
"""

usuarios = [ (101, "Alicia", "Admin", True),
             (102, "Bob", "User", False),
             (103, "Cherlie", "User", True)]

# Accediendo de la forma tradicional
for renglon in usuarios:
    user_id = renglon[0]
    username = renglon[1]
    role = renglon[2]
    esta_activo = renglon[3]

    if esta_activo:
        print(f'{username} ({role}) esta activo')

    # Esta es la mejor practica para acceder a los datos.
print('\nMEjorando la experiencia desempaquetando:')
for renglon, user_id, username, esta_activo in usuarios:

    if esta_activo:
        print(f'{username} ({role}) esta activo')


