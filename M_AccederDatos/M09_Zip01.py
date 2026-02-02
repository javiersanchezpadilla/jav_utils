""" Debemos aprender a usar ZIP

    Con ZIP vamos a ir accediendo al cada elemento de la lista en el mismo
    orden

    Para crear diccionarios a partir de listas ZIP siempre creara o tomara 
    la lista con menos elementos para no crear conflicto de elementos faltaamtes
"""

nombres = [ 'Ana', 'Pedro', 'Karla']
edades = [23, 20, 45]

# ESta es la forma comun cuando vamos iniciando pero no es la mejor manera
for i in range(len(nombres)):
    print(nombres[i], edades[i])

# Esta es la mejor manera usando ZIP
for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

# Si queremos a partir de las dos listas crear un diccionario
# dict    
mi_diccionario = dict(zip(nombres, edades))
print(mi_diccionario)
