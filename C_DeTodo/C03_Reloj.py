""" El siguiente ejemplo es para el desarrollo de un reloj
    la principal característica es que se actualiza cada segundo
    pero vamos a hacer que la hoja se imprima en la misma posicion
    
                          ||||||||
                          vvvvvvvv
    usando print(Mensaje, end="\r")  por defecto end= "\n"

    \r representa el carácter de retorno de carro (carriage return). 
    Este carácter mueve el cursor al principio de la línea actual, 
    sin avanzar a la siguiente línea. Es decir, no crea una nueva línea, 
    sino que posiciona el cursor al inicio de la línea donde ya se encuentr
"""

import time

def reloj():
    while True:
        hora_actual = time.strftime("%H:%M:%S")
        print(hora_actual, end="\r")  # Imprime la hora en la misma posición
        time.sleep(1)  # Espera un segundo antes de actualizar  

reloj()
