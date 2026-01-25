""" multiplicar dos números con una función lambda"""

def multiplicar(x, y):
    return x * y



print("Multiplicacion de la forma tradicional")
print(multiplicar(5, 3))  # Salida: 15

print("Multiplicacion de la forma lambda")
multiplicar_lambda = lambda x, y: x * y
print(multiplicar_lambda(5, 3))  # Salida: 15

# Tambien podesmos crear al vuelo la funcion lambda
print("Multiplicacion de la forma lambda al vuelo")
print((lambda x, y: x * y)(5, 3))  # Salida: 15
