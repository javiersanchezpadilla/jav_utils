""" DICTINARY COMPREHENSION

    En lugar de corchetes [], usamos llaves {} y separamos la clave del valor con dos puntos:

        { clave: valor for elemento in iterable }

    El Cuadrado de los Números
    Imagina que quieres un diccionario donde la clave sea el número y el valor sea su cuadrado.

"""

                                        # Con un ciclo for tradicional

numeros = [1, 2, 3, 4]
cuadrados = {}

for n in numeros:
    cuadrados[n] = n * n

print(cuadrados)                        # {1: 1, 2: 4, 3: 9, 4: 16}

                                        # Usando dictionary comprehension

cuadrados_list_comprehen = {n: n * n for n in [1, 2, 3, 4]}
print(cuadrados_list_comprehen) # {1: 1, 2: 4, 3: 9, 4: 16}                    


