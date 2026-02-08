""" Podemos asignar valores por ausencia o valores por defecto
    Si al momento de declarar la función declaro un valor por
    ausencia para cada parametro, entonces puedo llamar a la 
    función sin necesidad de indicar algún argumento
"""


def mi_funcion(a, b=10, c=100):
    print('El primer argumenro es', a)
    print('El segunfo argumento es', b)
    print('El tercer argumento es', c)


print('\nForma normal y tradicional de llamar a la función')
mi_funcion(1, 2 ,3)

print('\nForma alternativa de llamar especificando el parametro')
mi_funcion(c=30, a=10, b=20)

print('\nllamando con solo dos argumentos')
mi_funcion(10, 1000)

print('\nLlamando con solo un argumento')
mi_funcion(1)
