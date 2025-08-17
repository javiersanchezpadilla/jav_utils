""" Los decoradores son funciones que permiten modificar el 
    comportamiento de otras funciones o métodos.
    Se utilizan para añadir funcionalidades adicionales a una 
    función sin modificar su código original.
    En Python, los decoradores se aplican utilizando el símbolo 
    "@" antes de la definición de la función.
"""
def decorador(funcion):
    """ Decorador que imprime un mensaje antes de ejecutar la función """
    def funcion_decorada(*args, **kwargs):
        print("Ejecutando la función decorada...")
        resultado = funcion(*args, **kwargs)
        print("Función decorada ejecutada.")
        return resultado
    return funcion_decorada

@decorador  # Aplicando el decorador a la función
def funcion_principal():
    """ Función principal que será decorada """
    print("Esta es la función principal.")  

# Llamada a la función decorada
funcion_principal()
# Salida esperada:
# Ejecutando la función decorada...
# Esta es la función principal.
# Función decorada ejecutada.
# El decorador añade funcionalidad antes y después de la ejecución de la función principal. 