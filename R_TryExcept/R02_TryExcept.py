""" El error de las letras (ValueError)

    Imagina que pides la edad al usuario. Si el usuario escribe "veinte" 
    en lugar de 20, Python lanza un ValueError.
"""

try:
    edad = int(input("Ingresa tu edad en números: "))
    print(f"En 10 años tendrás {edad + 10}")
except ValueError:
    print("¡Cuidado! Solo puedes ingresar números.")
    