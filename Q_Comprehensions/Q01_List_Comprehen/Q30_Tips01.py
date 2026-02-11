""" Una forma mas eficienta del manejo de list comprehension"""

puntuaciones = [85, 92, 78, 95, 88, 76, 91]

todos_pasaron = True 
for puntos in puntuaciones:
    if puntos < 60:
        todos_pasaron = False
        break

print(todos_pasaron)

# Una forma mas eficiente es mediante el manejo de list comprehension
print('Mediante el uso de list comprehension')
todos_pasaron_ver2 = all(punto >= 60 for punto in puntuaciones)
print(todos_pasaron_ver2)