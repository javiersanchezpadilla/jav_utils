""" Protegiendo varios errores a la vez

    A veces, un código puede fallar por más de una razón. 
    En el ejemplo anterior, ¿qué pasaría si el usuario escribe "Hola" 
    en lugar de un número? El programa volvería a fallar, pero esta 
    vez con un ValueError.
"""

try:
    divisor = int(input("Dame un numero para dividor 100:"))
    resultado = 100 / divisor
    print("El resultado es", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero un valor")

except ValueError:
    print("El valor no puede ser un texto, debe ser un número")
