""" DEQUE (Double Ended Queue) (Cola doble).

    deque (que se pronuncia como "deck" en inglés) es una herramienta 
    fantástica. 
    Un deque, es como un tubo abierto por ambos lados. Puedes meter o sacar 
    pelotas tanto por la izquierda como por la derecha con la misma facilidad 
    y velocidad.

    ¿Por qué usar deque en lugar de una lista normal?
    -------------------------------------------------
    Aunque una lista normal tiene el método insert(0, valor), es lenta porque 
    tiene que desplazar todos los elementos a la derecha. El deque es un 
    especialista en velocidad:

    Métodos:
    --------
    append(x)       Agrega al final (derecha).
    appendleft(x)   Agrega al inicio (izquierda). ¡Súper rápido!
    pop()           Saca el último elemento.
    popleft()       Saca el primer elemento.

"""
from collections import deque 

# 1. Creas el "tubo" con los números 1, 2 y 3 adentro
d = deque([1, 2, 3])

# 2. Usas appendleft(0)
# Esto es como meter un 0 por el lado izquierdo del tubo
d.appendleft(0)


print(d)
