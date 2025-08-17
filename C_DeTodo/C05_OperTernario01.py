""" USo del operador ternario  

    Sintaxis:
    valor_si_verdadero if condicion else valor_si_falso 
"""

# lo normal es usar un if ... else de la siguiente forma

edad = 18
if edad >= 18:
    mensaje = "Eres mayor de edad"
else:
    mensaje = "Eres menor de edad"

print(mensaje)

# PODEMOS SIMPLIFICARLO USANDO EL OPERADOR TERNARIO
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)
