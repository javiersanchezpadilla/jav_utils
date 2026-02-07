""" Podemos unir diccionarios de dos maneras

    Recordemos que los diccionarios no admiten llaves duplicadas así
    que cuando se superponen gana la última escrita ('b' se superpone)
    Por eso el resultado de la union será
    
        {'host': 'Localhost', 'puerto': 9000, 'debug': True}
"""

a = {"host":"Localhost", "puerto":8000}
b = {"puerto":9000, "debug":True}

# LA FORMA TRADICIONAL
# Primera forma de unir diccioarios mediante ZIP
# {'host': 'Localhost', 'puerto': 9000, 'debug': True}
# Recordemos que los diccinarios no admiten llaves repetidas
unidos = {**a, **b}
print('Unidos de forma tradiccional')
print(unidos)

# LA MEJOR MANERA ( a partir de Python 3.9)
print('Unidos como conjuntos')
unidos2 = a | b 
print(unidos2)

# PARA UNIR UN DICCIONARIO EN OTRO a |= b  equivale a = a + b
print('Unidos como adicion al conjunto')
a |= b
print(a)
