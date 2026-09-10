""" Range no es una lista de valores"""

mi_rango = range(10)
print('El tipo al que pertenece RANGO es:', type(mi_rango))
print('El valor de range es:', mi_rango)

# Si queremos vaciar estos valores en una lista
mi_lista = mi_rango
print('El tipo al que pertenece LISTA es:', type(mi_lista))
print('El valor de LA LISTA es:', mi_lista)

# Convertir correctamente un rango a una lista
mi_lista = list(mi_rango)
print('El tipo al que pertenece LISTA es:', type(mi_lista))
print('El valor de LA LISTA es:', mi_lista)

