""" Este ejemplo muestra cómo usar la librería pyttsx3 para convertir texto a voz.
   Se inicializa el motor de texto a voz, se configuran las propiedades de velocidad y
   volumen, y se utiliza el método `say` para pronunciar un texto específico.
   Finalmente, se llama a `runAndWait` para que el motor procese la solicitud
   y pronuncie el texto.
   Asegúrate de tener instalada la librería pyttsx3 antes de ejecutar este código.
   Puedes instalarla usando el comando: pip3 install pyttsx3
"""

import pyttsx3

motor = pyttsx3.init()
motor.setProperty('rate', 140)    # Velocidad de habla
motor.setProperty('volume', 0.7)  # Volumen (0.0 a 1.0)

motor.say("Hola, esté es un ejemplo de texto a voz.")
motor.runAndWait()
