""" Uso de los argumentos
    Podemos especificar a traves del nombre del parametro el valor a asignar
    En el primer ejemplo asignamos los argumetos en el orden
    En el segundo ejemplo asignamos los valores de los parametros

"""

def mi_funcion(a, b, c):
    print('El primer argumenro es', a)
    print('El segunfo argumento es', b)
    print('El tercer argumento es', c)


# Forma normal de llamar a la función
mi_funcion(1, 2 ,3)

# Forma alternativa de llamar especificando el parametro
mi_funcion(c=30, a=10, b=20)
