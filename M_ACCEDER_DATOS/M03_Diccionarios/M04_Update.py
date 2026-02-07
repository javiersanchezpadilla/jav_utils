""" {}.update(diccionario)

    Actualiza o agrega llaves, modifica valores del diccionario.
    No retorna ningún valor
"""

a = {"x" : 1}
                            # recordar que modifica el diccionario, per
                            # no retorna nada por lo tanto b = None
b = a.update({"y" : 2})     

print(f'b = {b}')
print(f'a = {a}')
