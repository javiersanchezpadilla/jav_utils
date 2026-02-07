""" {}.pop(llave)

    Elimina el par llave-valor; retorna el Valor y modifica el diccionario
"""

a = {"x":1, "y":2}
b = a.pop("x")      # Elimina el par con llave 'x' y retorna el valor '1'

print(f'b = {b}')
print(f'a = {a}')
