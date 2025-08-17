""" Ejemplo del desarrollo del juego FizzBuzz
    El juego FizzBuzz es un juego de palabras que se utiliza a menudo 
    para enseñar programación y lógica.
    Las reglas son las siguientes:
    - Si el número es divisible por 3, se imprime "Fizz".
    - Si el número es divisible por 5, se imprime "Buzz".
    - Si el número es divisible por ambos, se imprime "FizzBuzz".
    - En caso contrario, se imprime el número.
"""

for i in range(1, 21): # Iteramos del 1 al 20
    if i % 3 == 0 and i % 5 == 0:  # Divisible por 3 y 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Divisible por 3
        print("Fizz")
    elif i % 5 == 0:  # Divisible por 5
        print("Buzz")
    else:  # No divisible por 3 ni por 5
        print(i)

# Salida esperada:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7