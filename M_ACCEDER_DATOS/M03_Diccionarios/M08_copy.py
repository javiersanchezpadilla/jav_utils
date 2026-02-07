""" {}.copy()

    Crea una copia superficial, no modifica o altera el diccionario inicial,
    retorna un nuevo diccionario

"""

a = {"x":1, "y":2}

                    # Crea un nuevo diccionario (una nueva copia del original) 
                    # en una nueva localidad de memoria
b = a.copy()     
b["x"] = 99

print(f'b = {b}')
print(f'a = {a}')
