""" Forma de uso de la funcion enumerate para iterar sobre una lista
    Enumerate es una función incorporada en Python que permite iterar 
    sobre un iterable (como una cadena, lista o una tupla) y convertirlos 
    en una tupla.

    enumerate(iterable, start=0)

    - iterable: una colección de elementos (lista, tupla, etc.) que se va a iterar.
    - start: el valor inicial del índice (opcional, por defecto es 0).
    
    El resultado de enumerate es un objeto iterable que contiene tuplas con
    el índice y el elemento correspondiente.
    Para convertirlo en una lista, se puede usar la función list().
    
    En este ejercicio se utilizará una lista de nombres y se aplicará enumerate
    para obtener el índice y el nombre de cada persona.
    El resultado será una lista de tuplas donde cada tupla contiene el índice
    y el nombre de la persona correspondiente.
"""

nombres = ['Juan', 'Ana', 'Luis', 'María', 'Pedro']

# Esta es la foma tradicional de indicar los indices de una lista
indice = 1
for nombre in nombres:
    print(f"{indice}. {nombre}")
    indice += 1


# Así imprime el objeto creado por enumerate
print("\n")
print(enumerate(nombres, start=1))  # <enumerate object at 0x...>

# Ahora mediente la funcion enumerate podemos obtener una tupla por valor 
# con el indice y el valor de cada elemento, el cual se puede convertir a una lista
print("\n")
print(list(enumerate(nombres)))

# Metodo alternativo para imprimir el indice y el valor de cada elemento (inicia en cero)
print("\n")
for indice, nombre in enumerate(nombres):
    print(f"{indice}. {nombre}")

# Metodo alternativo para imprimir el indice y el valor de cada elemento (inicia en diez)
print("\n")
for indice, nombre in enumerate(nombres, start=10):
    print(f"{indice}. {nombre}")