""" Vamos a intentar evitar el error más famoso de las matemáticas: la división por cero.

El Reto: Pide al usuario que ingrese un número para dividir 100 entre ese número. Si el usuario pone un 0, el programa debe decir: "No se puede dividir por cero".

Pista 1: El error se llama ZeroDivisionError.

Pista 2: Usa esta estructura:

Python

try:
    divisor = int(input("Dime un número para dividir 100: "))
    # Tu código aquí para dividir 100 entre divisor
except ZeroDivisionError:
    # Tu código para el mensaje de error

"""

try:
    divisor = int(input("Dame un numero para dividor 100:"))
    resultado = 100 / divisor
    print("El resultado es", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero un valor")

