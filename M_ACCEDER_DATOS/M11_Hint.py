""" Podemos definir el tipo de dato usado en cada variable
    esto mediante el uso de 'Hint' (pistas)
    
    Estas pistas son solo estilo de programación
    """

# Esto aunque es correcto podemos enriquecerlo con el uso de los hints
roll = 20
name = 'Javier'
section = 'A'

print(roll)
print(name)
print(section)

# Ahora se mostrará la misma versión pero usando hints
# Como vemos no afecta el funcionamiento, solo le da mas claridad al programar.

rol: int = 20
nombre: str = 'Javier'
seccion: str = 'A'

print(rol)
print(nombre)
print(seccion)


