""" Determinar un valor par o impar.
   Este ejemplo muestra cómo determinar si un número es par o impar
   utilizando una función tradicional y una función lambda.
   Se define una función que verifica si un número es divisible por 2,
   y se muestra cómo hacerlo de forma tradicional, con una función lambda
   y también creando la función lambda al vuelo.
   La salida muestra el resultado de cada método."""

# PRimero de la forma tradicional
def es_par(numero):
    return numero % 2 == 0  

print("Es par de la forma tradicional")
print(es_par(4))  # Salida: True
print(es_par(5))  # Salida: False

# Ahora con una función lambda
es_par_lambda = lambda numero: numero % 2 == 0  

print("Es par de la forma lambda")
print(es_par_lambda(4))  # Salida: True
print(es_par_lambda(5))  # Salida: False

# Tambien podemos crear al vuelo la funcion lambda
print("Es par de la forma lambda al vuelo")
print((lambda numero: numero % 2 == 0)(4))  # Salida: True
print((lambda numero: numero % 2 == 0)(5))  # Salida: False

# Otra forma de hacerlo con una función lambda, donde se indica el
# texto de si es par o impar
es_par_impar = lambda numero: "Es par" if numero % 2 == 0 else "Es impar"
print("Es par o impar con lambda")
print(es_par_impar(4))  # Salida: Es par
print(es_par_impar(5))  # Salida: Es impar
print(es_par_impar(0))  # Salida: Es par
print(es_par_impar(-2)) # Salida: Es par

