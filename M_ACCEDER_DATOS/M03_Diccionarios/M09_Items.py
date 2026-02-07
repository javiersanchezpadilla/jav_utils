""" {}.items()

    Retorna una vista dinamica del par llave-valor, no modifica el diccionario
"""

a = {"x":1, "y":2, "z":3}

                # Asigna a 'b' una lista de tuplas, donde cada tupla contiene
                # cada uno de los pares llave-valor del diccionario
b = a.items()       

print(f'a = {a}')
print(f'b = {b}')
