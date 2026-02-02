""" No debemos mezclar las variable globales con las variable locales
    En este ejemplo podemos ver como no cambian los valores globales

        x = "GLOBAL"
        y = 10

        def demo(x, y):
            x = "LOCAL"
            y = y + 100
            print('El valor de x en funcion es', x)     # LOCAL
            print('El valor de y en funcion es', y)     # 110

        demo(x, y)
        print('El valor de x es', x)    # GLOBAL
        print('El valor de y es', y)    # 10
"""

x = "GLOBAL"
y = 10

def demo(x, y):  # <-- Cuidado ya que los parametros son iguales a las variable
    x = "LOCAL"
    y = y + 100
    print('El valor de x en funcion es', x)
    print('El valor de y en funcion es', y)
    # solucion 1
    return x, y

# como parte de la solucion 1
x, y = demo(x, y)
print('El valor de x es', x)
print('El valor de y es', y)
