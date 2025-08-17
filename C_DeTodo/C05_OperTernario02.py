""" Uso de los operadores ternarios en Python

    Sintaxis:
    valor_si_verdadero if condicion else valor_si_falso 
"""

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [n for n in numero if n % 2 == 0]
impares = [n for n in numero if n % 2 != 0]

print("Pares:", pares)
print("Impares:", impares)
