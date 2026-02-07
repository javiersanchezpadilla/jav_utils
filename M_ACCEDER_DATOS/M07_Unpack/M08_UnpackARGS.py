""" DESEMPAQUETADO DE *ARGS

    La Analogía: El Chef y el Pedido Abierto
    ----------------------------------------
    
    Imagina que eres un Chef.

    *args (Argumentos)              Es como si un cliente te dijera: "Tráeme 
                                    una ensalada con estos ingredientes" y te 
                                    da una lista que puede tener 3 cosas o 10.
                                    No sabes cuántas son, pero todas van al 
                                    mismo plato (una tupla).

    El uso de *args (La lista infinita)
    -----------------------------------
    Se usa cuando no sabes cuántos datos te van a enviar. El asterisco "empaqueta"
    todo lo que recibe en una tupla.                                    

"""

def sumar_todos(*numeros):
                                # 'numeros' es una tupla con todo lo que enviamos
    total = sum(numeros)
    print(f"Sumando {len(numeros)} valores, el total es: {total}")


sumar_todos(10, 20)             # Funciona con 2
sumar_todos(5, 5, 5, 5, 5)      # Funciona con 5
