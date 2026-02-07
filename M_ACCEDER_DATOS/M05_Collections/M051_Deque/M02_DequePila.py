""" Vamos a crear un sistema de "Deshacer" (Undo). 

    Este es el ejemplo perfecto porque, cuando presionas Ctrl + Z en tu 
    computadora, el sistema busca la última acción que hiciste para borrarla.

    La Analogía: La Pila de Platos
    ------------------------------
    Imagina que cada acción que haces es un plato que pones en una pila.
    A) Si escribes una palabra, pones un plato.
    B) Si borras un párrafo, pones otro plato encima.
    C) Cuando quieres "Deshacer", simplemente quitas el plato que está hasta 
       arriba (el más reciente).

    Ejemplo Práctico: Editor de Texto Simple
    Usaremos deque para guardar las acciones. Como el deque es muy rápido para 
    sacar cosas de los extremos, es ideal para esto.

    ¿Por qué esto es mejor que una lista?
    -------------------------------------
    En este ejemplo usamos .pop() (que las listas también tienen), pero imagina 
    que quieres hacer un sistema de "Registro de Logs" donde solo quieres ver 
    los primeros que entraron. Ahí usarías .popleft().

    .pop()      Saca el de la derecha (el último en entrar). Ideal para Deshacer.
    .popleft()  Saca el de la izquierda (el primero en entrar). Ideal para Filas 
                de espera.

"""

from collections import deque

# 1. Creamos nuestro historial (máximo 5 acciones para no gastar memoria)
historial = deque(maxlen=5)

def realizar_accion(texto):
    print(f"Escribiendo: '{texto}'")
    historial.append(texto)

def deshacer():
    if historial:
        accion_eliminada = historial.pop() # Sacamos la ÚLTIMA acción
        print(f"--- Deshacer: Se eliminó '{accion_eliminada}' ---")
    else:
        print("Nada que deshacer.")

                                # --- Simulando el uso ---
realizar_accion("Hola")
realizar_accion("¿Cómo estás?")
realizar_accion("Hoy es viernes")

print("\nHistorial actual:", list(historial))

deshacer()                      # Esto quitará "Hoy es viernes"

print("Historial después de deshacer:", list(historial))
