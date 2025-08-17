""" PAra este ejercicio se requiere instalar la libreria
    pip3 install pyfiglet
    Esta libreria permite generar arte ASCII de manera sencilla
"""

import pyfiglet

print("Generando arte ASCII..., oprima 'exit' para salir")

while True:
    texto = input("Ingrese el texto a convertir en arte ASCII: ")
    if texto.lower() == 'exit':
        print("Saliendo del generador de arte ASCII.")
        break
    
    # Generar arte ASCII
    ascii_art = pyfiglet.figlet_format(texto)
    
    # Mostrar el resultado
    print(ascii_art)
    print("Arte ASCII generado con éxito.\n")
    print("Ingrese otro texto o 'exit' para salir.")    

