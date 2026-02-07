""" insertamos en la lista 'a' el valor 'pera', luego asignamos un elemento
    a la variable 'b' (lo que se asigna es un elemento de la lista 'PERA'),
    si asignamos a la variable 'c' el primer elemento de la variable 'b' (que
    es una cadena PERA), el valor b[0] es la letra 'P' """

a = ['uva', 'lima']
a.append('pera')
b = a[2].upper()
c = b[0]

print(c)        
