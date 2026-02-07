""" ZIP()

    Imagina que tienes dos hileras de dientes de metal por separado. 
    Cuando subes el cierre, el mecanismo toma el primer diente del lado 
    izquierdo y lo junta con el primer diente del lado derecho, luego el 
    segundo con el segundo, y así sucesivamente.
    Eso es exactamente lo que hace zip(): toma dos (o más) listas y las 
    une pareja por pareja.

    Ejemplo Práctico: Nombres y Edades
    Imagina que tienes una lista de personas y otra lista con sus edades. 
    Quieres saber a quién le pertenece cada edad.

    Un detalle importante:
    ----------------------
    Si una lista es más larga que la otra, zip es muy justo: se detiene cuando 
    se acaba la lista más corta. Es como si a tu chaqueta le faltaran dientes 
    en un lado; el cierre no puede seguir uniendo si no hay pareja.
"""

nombres = ["Ana", "Betto", "Carla"]
edades = [25, 30, 22]

# Usamos zip para emparejarlos
parejas = zip(nombres, edades)

# Al convertirlo en lista, veremos el resultado:
print(list(parejas))
