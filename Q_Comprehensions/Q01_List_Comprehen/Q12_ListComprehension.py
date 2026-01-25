""" Par o Impar (Textual)
    Convierte una lista de números en una lista de palabras que digan 
    si el número es "Par" o "Impar".

    Entrada: numeros = [1, 2, 3, 4, 5]
    Pista: Usa x % 2 == 0.

    [ valor_si_se_cumple if condicion else valor_si_no for elemento in lista ]
"""

numeros = [1, 2, 3, 4, 5]
par_impar = ["Par" if numero % 2 == 0 else "Impar" for numero in numeros]

print('Lista de numeros original', numeros)
print('textos de los valores', par_impar)
