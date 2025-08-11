""" Este ejemplo muestra el uso de un if en una asigación de una variable

    La linea de insteres en este ejemplo es la que contiene el if, que se usa para
    validar si el segundo número es cero antes de realizar la división.

                           vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv     
    return self.a / self.b if self.b != 0 else "Error: División por cero
    
"""

class Calculadora:
    def __init__(self, a, b, operacion):
        self.a = a
        self.b = b
        self.operacion = operacion

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        # if self.b == 0:   # Esta es una foma de hacerlo, pero no es la mejor
        #     return "Error: División por cero"
        # return self.a / self.b

        return self.a / self.b if self.b != 0 else "Error: División por cero"   # <---- Esta es la linea de interes
    


prueba = Calculadora(10, 5, "sumar")
print(prueba.sumar())  # Imprime: 15

prueba = Calculadora(10, 5, "restar")
print(prueba.restar())  # Imprime: 5

prueba = Calculadora(10, 5, "multiplicar")
print(prueba.multiplicar())  # Imprime: 50

prueba = Calculadora(10, 0, "dividir")
print(prueba.dividir())  # Imprime: Error: División por cero