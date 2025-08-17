""" Salida esperada:

    Antes de ejecutar la función
    Hola, Python!!
    Después de ejecutar la función

    El decorador añade funcionalidad antes y después de la ejecución de 
    la función saluda.
    Esto permite reutilizar el decorador en otras funciones sin modificar 
    su código original.
    Los decoradores son una herramienta poderosa en Python para mejorar 
    la modularidad y reutilización del código.

"""

def decorador (funcion):
    def nueva_funcion():
        print( "Antes de ejecutar la función")
        funcion()
        print( "Después de ejecutar la función")
    return nueva_funcion


@decorador
def saluda():
    print ("Hola, Python!!")

saluda()

