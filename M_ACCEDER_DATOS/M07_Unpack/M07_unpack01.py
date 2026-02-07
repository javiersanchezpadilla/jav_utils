""" DESEMPAQUETADO

    El Desempaquetado (o Unpacking) en Python es una de las funciones más 
    elegantes del lenguaje.
    
    La Analogía: El Kit de Muebles para Armar
    -----------------------------------------
    Imagina que compras un mueble en una tienda. El mueble viene dentro de 
    una sola caja grande (la lista o tupla). Para poder usar las piezas, 
    tienes que abrir la caja y sacar cada parte (tornillos, tablas, patas) 
    para ponerlas sobre el suelo por separado.

    Eso es el unpacking: tomar los elementos que están "atrapados" dentro de 
    una colección y asignarlos a variables individuales en una sola línea.
    
    Si tienes una tupla con 3 elementos, puedes "repartirlos" en 3 variables de 
    una sola vez.    

    Regla de oro: 
    -------------
    Normalmente, debes tener la misma cantidad de variables a la izquierda que 
    elementos hay dentro de la caja a la derecha.
    
    """
coordenadas = (10, 20)          # La "caja" (tupla)

x, y = coordenadas              # El desempaquetado (sacamos las piezas)

print(f"La X vale {x} y la Y vale {y}")
