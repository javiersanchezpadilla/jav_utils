""" SOBRE ESCRIBIR FUNCIONES CON FUNCIONES LAMBDA

    Sobre escritura de un método de clase
    -------------------------------------
    En este ejemplo se sobre escribira un método por una función LAMBDA
"""

class Usuario:
    def nombre(self):
        return "Función Original de la clase"
    

            # Aquí sobre escribimos el método
Usuario.nombre = lambda self:"Funcion sobre esrita con lambda"

print(Usuario().nombre())
