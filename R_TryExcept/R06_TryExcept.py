""" El Bloque Maestro: try, except y finally

    Para terminar de ser un experto en manejo de errores, 
    existe una pieza final llamada finally.

    El bloque finally es especial porque siempre se ejecuta, 
    pase lo que pase. No importa si hubo un error o si todo 
    salió bien; el código dentro de finally se activará al final. 
    Se usa mucho para "limpiar", como cerrar un archivo o apagar una conexión.

"""

try:                                    # Intentar leer el archivo...
    archivo = open("datos.txt", "r")
    
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Limpieza finalizada: El programa terminó de intentarlo.")
    