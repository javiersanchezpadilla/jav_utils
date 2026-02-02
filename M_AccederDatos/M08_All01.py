""" En el siguiente problema queremos compronar si todos los archivos terminan
    con la extension '.jpg', lo tradicional seria resolverlo mediante un ciclo 
    sin embargo existe otra solución mediante la funcion ALL y el uso de
    comprehension lists
"""

archivos = ['examen.jpg', 'paisaje01.jpg', 'cancion.mp3', 'atardecer.jpg']

# Forma tradicional de resolver la validación
todos_son_imagenes = True 
for nombre_archivo in archivos:
    if not nombre_archivo.endswith('.jpg'):
        todos_son_imagenes = False
        break 

print(todos_son_imagenes)

# Forma recomendada de hacerlo mediant la funcion ALL y COMPREHENSION LISTS
todos_son_imagenes_ver02 = all(archivo.endswith('.jpg') for archivo in archivos)
print(todos_son_imagenes_ver02)
