""" Beneficios de usar comprensiones de listas:

    ** Concisión: Permiten escribir código más corto y condensar 
       varias líneas de un bucle for en una sola. 
    ** Legibilidad: Para otros programadores de Python, es una forma
       más rápida de entender el código, ya que es una técnica estándar. 
    ** Eficiencia: Suelen ser más rápidas que los bucles for tradicionales. 

    Sintaxis básica:
    [expresión for elemento in iterable if condición]
    - expresión: La operación que se realiza en cada elemento.
    - for elemento in iterable: Itera sobre cada elemento del iterable.
    - if condición (opcional): Filtra los elementos según una condición.
"""

#Ejemplo para obtener el cuadrado de los elementos de una lista
nums = [1, 23, 45, 32, 67, 99]

# Usando un bucle for tradicional
cuadrados = []
for n in nums:
    cuadrados.append(n ** 2)
print("Cuadrados con bucle for tradicional:", cuadrados)

# Usando una comprensión de listas
cuadrados_comp = [n ** 2 for n in nums]
print("Cuadrados con comprensión de listas:", cuadrados_comp)

