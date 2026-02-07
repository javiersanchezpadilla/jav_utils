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

def demo():
    # Solución 2, mediante el uso de GLOBAL, que es como decirle a python
    # "Oye Python, usa las variables 'x', 'y' que están afuera"
    global x, y    
    y = y + 100
    print('El valor de x en funcion es', x)
    print('El valor de y en funcion es', y)


demo(x, y)
print('El valor de x es', x)
print('El valor de y es', y)
