""" El Desempaquetado al revés (Pasar datos a una función)

    Esto es lo más común. Imagina que ya tienes una lista o un diccionario y 
    quieres pasárselos a una función que pide argumentos separados.

    Resumen:
    --------
    A) En la definición de la función (def...): Los asteriscos empaquetan 
       (juntan todo en una tupla o diccionario).
    B) Al llamar a la función: Los asteriscos desempaquetan (reparten los 
       elementos de una lista o diccionario en los huecos de la función).

    REGLA DE ORO:
    ------------
    Si usas ambos en una función, el orden siempre es:
    1) Argumentos normales.
    2) *args
    3) **kwargs
    
"""
def presentarse(nombre, edad):
    print(f"Hola, soy {nombre} y tengo {edad} años.")

# Tenemos los datos en una lista
datos_lista = ["Javier", 30]


            # En lugar de: presentarse(datos_lista[0], datos_lista[1])
            # Usamos el desempaquetado, de esta manera al desempaquetar
            # la lista el elemento datos_lista[0] se asigna al primer parametro
            # y el elemento datos_lista[1] se asigna al segundo parametro
            # Entonces ¿Qué pasó ahí? El asterisco "rompió" la lista y entregó 
            # los elementos uno por uno a la función.
presentarse(*datos_lista)
