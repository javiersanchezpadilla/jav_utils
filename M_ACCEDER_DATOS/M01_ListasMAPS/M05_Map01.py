""" La función map() en Python aplica una función a cada uno de los 
    elementos de una secuencia (como una lista, tupla o rango) y devuelve 
    un objeto ejecutable (iterador) con los resultados.

    Su objetivo principal es transformar datos de forma rápida sin necesidad 
    de escribir un bucle for explícito.
    
    Sintaxis
    
    map ( función, iterable, ...)} 
    
    **) función: La función que quieres ejecutar sobre cada elemento.
    **) iterable: La lista, tupla o secuencia que contiene los datos de 
        entrada.
        
    Ejemplo Práctico 1: Convertir tipos de datos
    Un caso muy común es cuando recibes números como texto (por ejemplo, 
    desde un input()) y necesitas convertirlos a enteros:
"""
# Lista de números en formato texto
numeros_texto = ["1", "2", "3", "4", "5"]

# Aplicamos int a cada elemento de la lista
numeros_enteros = list(map(int, numeros_texto))

print(numeros_enteros)
# Salida: [1, 2, 3, 4, 5]

