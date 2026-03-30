""" Manipular textos en pantalla """

# impresiones en pantalla

texto = "    Esta es una cadena de TEXTO para las pruebas    "

print('El texto:', texto)
print('El texto:', texto.strip())

# Para cambiar las primeras letras de cada palabra a mayúsculas
print('El texto:', texto.strip().title())

# Es falso porque los espacios en blanco no son parte del alfabeto
print(texto.isalpha())

# ya sin espacios ahora si es un texto con solo letras
print('cadena solo alpha', 'Unilateral'.isalpha())

# True porque aunque es una cadena solo contiene números
print('Cadena de solo números', '12345'.isalnum())

print('Cadena con inicio de mayúsculas', 'Esta Es Una Prueba'.istitle())


print('Quitar los espacios en blando de la izquierda:', texto.lstrip())
print('Quitar los espacios en blanco de la derecha:', texto.rstrip())
print('Quitar los espacios en ambos lados:', texto.strip())


# INYECCION DE VALORES MEDIANTE FORMAT.
# REEMPLAZANDO CADENAS lstrip, rstrip y strip no solo quita espacios
nueva_cadena = 'www.python.org'

print('Cadena original:', nueva_cadena)
print('Eliminar las w  --> ', nueva_cadena.lstrip('w'))
print('Eliminar org  -->', nueva_cadena.rstrip('org'))
print('Eliminar por toda la cadena las w, los org y los puntos . -->', nueva_cadena.strip('worg.'))

