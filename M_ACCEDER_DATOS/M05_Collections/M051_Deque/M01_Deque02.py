""" EJEMPLO 02

    Imagina que estás programando el sistema de turnos de un banco. 
    Normalmente, la gente llega y se forma al final (append). 
    Pero, si llega una persona de la tercera edad, tiene prioridad y debe ir 
    al principio de la fila (appendleft).

"""
from collections import deque

fila = deque(["Juan", "Maria"])

# Llega alguien joven
fila.append("Pedro") 

# Llega alguien con prioridad
fila.appendleft("Abuelita Elena")

print(list(fila))
# Resultado: ['Abuelita Elena', 'Juan', 'Maria', 'Pedro']
