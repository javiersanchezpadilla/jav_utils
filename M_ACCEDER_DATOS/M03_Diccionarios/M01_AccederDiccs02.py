""" SE debe usar get() para acceder a los miembros de un diccionario"""

usuario = {"nombre" : "Alicia"}

# Aqui el nombre o referencia de la llave es correcto
print(usuario.get("nombre", "Llave no provista"))

# Aqui el nombre de la llave no existe (podemos personalizar el error)
print(usuario.get("edad", "Error llave no existe en el diccionario"))
