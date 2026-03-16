""" Usaremos un for con un else para calculra números primos"""

numero = 29

if numero > 1:      # Los números primos son mayores a 1
    # Verifica los factores
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, 'No es un número primo')
    else:
        print(numero, 'Es un numero primo')

