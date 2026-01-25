""" Manejo de Errores (try-except)

    ¿Te ha pasado que tu programa se detiene de golpe porque alguien escribió 
    una letra en lugar de un número? El Manejo de Errores sirve para que tu 
    código sea "indestructible".

    Ejemplo práctico: Imagina un programa que divide 100 entre un número que 
    el usuario elija. Si el usuario pone 0, ¡el programa deja de funcionar!

    La Estructura "Escudo"
    Funciona como una red de seguridad:

    try: Aquí pones el código que "podría" fallar.

    except: Aquí pones qué hacer si ocurre un error específico.

"""

try:
    numero = int(input("Dime un número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")
except ValueError:
    print("¡Error! Debes ingresar un número, no letras.")
