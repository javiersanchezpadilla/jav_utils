""" DESEMPAQUETADO DE *ARGS

    La Analogía: El Chef y el Pedido Abierto
    ----------------------------------------
    
    Imagina que eres un Chef.

    **kwargs (Keyword arguments)    Es cuando el cliente es más específico: 
                                    "Quiero que el tomate sea orgánico, la 
                                    lechuga romana y el aderezo César". Te está 
                                    dando una llave (el tipo de ingrediente) y 
                                    un valor (la especificación). Esto llega a 
                                    ti como un diccionario.

    El uso de **kwargs (El diccionario de opciones)
    -----------------------------------------------
    Los dos asteriscos sirven para recibir argumentos con nombre (como etiquetas).
    Python los guarda en un diccionario.         

    ¿Por qué es útil? 
    -----------------
    Porque puedes agregar opciones nuevas (como arma="Espada") sin tener que 
    cambiar la definición de la función.                          

"""

def configurar_personaje(**detalles):
    # 'detalles' es un diccionario
    for etiqueta, valor in detalles.items():
        print(f"{etiqueta.capitalize()}: {valor}")

configurar_personaje(nombre="Aragorn", clase="Guerrero", nivel=50)
