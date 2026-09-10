"""  Como debemos copiar las listas en Python

    Cuando creamos una asignación, realmente lo que estamos haciendo no es crear
    una nueva lista, realmente estamos apuntando a la misma dirección de memoria
    del objeto lista, por lo que afectemos afectará a ambas vaiables ya que hacen 
    referencia al mismo objeto en memoria.

"""

carrito = ['teclado', 'ratón', 'monitor']

# El erro tipico es declarar una variable y 'asignar' la lista
copia = carrito 
copia.append('engrapadora')

print(carrito)

# Forma correcta de copiar una lista mediante el método copy
otra_copia = carrito.copy()
otra_copia.append('Lapiz')
otra_copia.append('Mouse Pad')


print('Lista original', carrito)
print('Lista copiada', otra_copia)
