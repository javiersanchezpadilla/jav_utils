""" ZIP()  Descomprimir

    Vamos a ver cómo hacer el proceso inverso (descomprimir) y luego mostraré
    lo potente que es cuando tienes muchas listas.

    1. El proceso inverso: "Unzip"
    Si zip es subir el cierre de la chaqueta para unir los dientes, "unzip" es 
    bajarlo para separar las hileras nuevamente. En Python, curiosamente, se usa 
    la misma función zip pero con un pequeño truco: un asterisco *.

    Ejemplo práctico: Imagina que recibes una lista de parejas y quieres separar 
    los nombres por un lado y los puntos por otro.

    ¿Qué hace el asterisco *? Imagina que el asterisco es como vaciar una caja 
    sobre la mesa. En lugar de pasarle a zip una sola lista con todo adentro, 
    le pasas los elementos por separado para que él pueda reorganizarlos.

"""

# Tenemos los datos mezclados
datos_juntos = [('Ana', 25), ('Betto', 30), ('Carla', 22)]

# Usamos el asterisco para "desempaquetar"
nombres, edades = zip(*datos_juntos)

print("Nombres:", nombres)
print("Edades:", edades)