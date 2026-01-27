""" Redondeo de valores en pantalla"""

# formatear salidas de valores con f-string
a = 10.34 * 1.0255
b = a * 100000
print(a)
print(f'El valor formateado es: {a:.2f}')

valor_corto = round(a, 2)
print('El valor redondeado es:', valor_corto)

# con separador de miles y decimales
print(f'El valor formateado con comas y decimales es: {b:,.2f}')

