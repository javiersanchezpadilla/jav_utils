""" Podemos asignar valores por ausencia o valores por defecto

    En este ejemplo declaro cada uno de los valores por ausencia
    para cada parametro de la función, lo cual nos permite si
    lo deseamos poder llamar a la función sin necesidad de indicar
    ningún argumento.
"""


def mi_funcion(a=1, b=2, c=3):
    print('El primer argumenro es', a)
    print('El segunfo argumento es', b)
    print('El tercer argumento es', c)


print('\nForma normal y tradicional de llamar a la función')
mi_funcion(10, 20 ,30)

print('\nForma alternativa de llamar especificando el parametro')
mi_funcion(c=30, a=10, b=20)

print('\nllamando con solo dos argumentos')
mi_funcion(10, 1000)

print('\nLlamando con solo un argumento')
mi_funcion(1)

print('\nLlamando la función sin argumentos')
mi_funcion()
