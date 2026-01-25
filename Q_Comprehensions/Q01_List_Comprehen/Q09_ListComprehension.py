""" Limpieza de Correos
    Imagina que recibes una lista de correos pero algunos tienen espacios 
    al principio o al final por error. Crea una lista limpia usando el método 
    .strip() de las cadenas de texto.

    Objetivo: Quitar los espacios en blanco de cada elemento.

    [ expresión_final for elemento in lista_original if condicion ]
"""

correos = [" user1@gmail.com", "user2@yahoo.com ", " user3@outlook.com "]
correos_sin_espacios = [x.strip() for x in correos]

print('Lista de correos originales', correos)
print('Lista de correos corregidos', correos_sin_espacios)

