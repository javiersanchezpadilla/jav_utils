""" DEQUE.

    El deque tiene un superpoder: puedes decirle que solo acepte, por ejemplo, 
    3 elementos. Si metes un cuarto, el deque echa al más viejo automáticamente 
    para hacer espacio.

    Usa deque cuando necesites agregar o quitar cosas de ambos extremos de 
    manera muy rápida, o cuando quieras un historial que se limpie solo 
    (con maxlen).
"""

from collections import deque

# Solo guarda los últimos 3 mensajes
historial = deque(maxlen=3)

historial.append("Hola")
historial.append("¿Como estás?")
historial.append("Bien")
historial.append("Genial")  # Al entrar este, "Hola" desaparece automáticamente

print(historial)            # deque(['¿Como estás?', 'Bien', 'Genial'], maxlen=3)
