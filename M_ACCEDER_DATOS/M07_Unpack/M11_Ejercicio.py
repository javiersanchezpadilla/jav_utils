""" Vamos a construir esa "Función Maestra".

    Imagina que eres el dueño de un Restaurante de Lujo. Tu función será el 
    Maître (el encargado de recibir los pedidos).

    El Escenario:
    -------------
    El Maître debe recibir:
    1) El número de la mesa (un argumento normal).
    2) Una lista de platos que pidieron (usaremos *args).
    3) Instrucciones especiales como "sin cebolla" o "término medio" 
       (usaremos **kwargs).

    El orden de los ingredientes dentro de los paréntesis es sagrado:

    ¿Qué aprendemos con este ejercicio?
    -----------------------------------
    1) Flexibilidad total: La mesa 5 pidió 3 platos, pero la mesa 12 solo uno. 
       ¡La función no se rompió! Gracias a *args, se adapta al tamaño del 
       hambre del cliente.
    2) Etiquetas dinámicas: En la mesa 12 inventamos la nota sin_cebolla. 
       No tuvimos que avisarle a la función antes; **kwargs creó esa etiqueta 
       en el momento.

    El orden importa: Si intentas poner los platos antes del número de mesa, 
    Python se confundirá. El orden siempre es: Fijos -> Múltiples -> Etiquetas.

    Un truco extra de profesional:
    ------------------------------
    ¿Qué pasa si tienes los platos en una lista y las notas en un diccionario? 
    ¡Puedes usar el desempaquetado que aprendimos antes para llamar a tu función
    maestra!

        lista_comida = ["Sopa", "Ensalada"]
        notas_chef = {"alergia": "nueces", "urgencia": "alta"}

        # Usamos * para la lista y ** para el diccionario
        recibir_pedido(20, *lista_comida, **notas_chef)

"""

def recibir_pedido(mesa, *platos, **detalles):
    print(f"--- COMANDA MESA {mesa} ---")
    
    # 1. Procesamos los platos (*args)
    print("\nPlatos pedidos:")
    for plato in platos:
        print(f" > {plato}")
    
    # 2. Procesamos los detalles especiales (**kwargs)
    if detalles:
        print("\nNotas especiales para el Chef:")
        for clave, valor in detalles.items():
            # Reemplazamos el guion bajo por espacio para que se vea mejor
            nota = clave.replace("_", " ")
            print(f" * {nota}: {valor}")
    else:
        print("\nSin notas especiales.")
    
    print("-" * 25)

# A cocinar! 

# Pedido 1: Mesa 5, pide 3 cosas, una nota especial
recibir_pedido(5, "Pasta", "Pizza", "Vino", termino_de_la_pasta="al dente")

# Pedido 2: Mesa 12, pide 1 cosa, 2 notas especiales
recibir_pedido(12, "Hamburguesa", sin_cebolla=True, con_papas_extra=True)
