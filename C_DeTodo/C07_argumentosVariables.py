def promedio(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    if cantidad == 0:
        return 0
    return suma / cantidad

# Ejemplo de uso de la función promedio
resultado = promedio(10, 20, 30, 40, 50)
print(f"El promedio es: {resultado}")

# El promedio es: 30.0
# La función promedio calcula el promedio de una cantidad variable de números.
# Utiliza *args para aceptar un número variable de argumentos y calcula el promedio.
# Si no se pasan números, devuelve 0.
