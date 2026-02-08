""" SOBRE ESCRIBIR FUNCIONES CON FUNCIONES LAMBDA

    Sobre escritura de una función de un método
    -------------------------------------------
    En este ejemplo se sobre escribira una función de un método 
    Se sobre escribira la función sleep(), reemplazando su comportamiento
    aquí solo desplegará el texto sin hacer el retardo del tiempo.
"""
import time 

# Se sobre escribe la función SLEEP()
time.sleep = lambda x: print('Saltando Durmiendo (sleep)')

# Al intentar ejecutar solo realizará lo definido en la sobre escritura
time.sleep(12)
