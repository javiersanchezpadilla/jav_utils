""" namedtuple (tupla con nombre)

    La Analogía: La Ficha de Biblioteca
    -----------------------------------
    Imagina una tupla normal como un pedazo de papel donde anotaste datos en 
    orden: ("Cien años de soledad", "Gabriel García Márquez", 1967).

    Si alguien lee ese papel, tiene que adivinar: "¿El 1967 es el año de 
    publicación o el número de páginas?".
    Para usarlo en Python, tendrías que recordar que el autor está en la 
    posición [1].

    Una namedtuple es como una ficha de biblioteca impresa. Sigue siendo un 
    papel pequeño y ligero (como la tupla), pero ahora tiene etiquetas claras: 
    Título, Autor y Año.

    Ejemplo Práctico: Coordenadas GPS
    ---------------------------------
    Imagina que estás trabajando con ubicaciones. Usar una tupla normal es 
    confuso, pero un diccionario a veces es "demasiado pesado" para solo dos 
    números.

    Característica  Diccionario {}                  namedtuple
    ------------------------------------------------------------------------------
    Memoria         Consume más espacio.            Muy ligera (como una tupla).
    Escritura       "datos["nombre"] (más largo).   datos.nombre (más limpio).
    Inmutabilidad   Puedes cambiar los valores.     No se puede cambiar (es segura).

    ¿Cuándo usarla en la vida real?
    -------------------------------
    Es perfecta para cuando tienes datos que no van a cambiar durante el programa, 
    pero quieres que tu código sea fácil de leer para otros.

    EL EJEMPLO 02 ES MAS SENCILLO DE ENTENDER
"""
from collections import namedtuple

# 1. Definimos el "molde" de nuestra ficha
# Le decimos que se llamará 'Punto' y tendrá 'x' e 'y'
Punto = namedtuple('Punto', ['x', 'y'])

# 2. Creamos un punto real
mi_ubicacion = Punto(x=10, y=25)

# 3. ¡Aquí está la magia! Puedes acceder por nombre, no solo por posición
print(f"Estoy en la coordenada X: {mi_ubicacion.x}")
print(f"Estoy en la coordenada Y: {mi_ubicacion.y}")

# 4. Pero sigue siendo una tupla, así que esto también funciona:
print(f"En la posición 0 está: {mi_ubicacion[0]}")
