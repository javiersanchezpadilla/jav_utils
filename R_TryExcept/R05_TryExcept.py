""" El Reto de la Calculadora Blindada

    Vamos a crear una mini calculadora que sume dos números, 
    pero debe ser indestructible.

    1. Pide al usuario el numero1. 
    2. Pide al usuario el numero2. 
    3. Suma ambos y muestra el resultado. 
    4. Misión: Si el usuario ingresa letras o símbolos en 
       cualquiera de los dos números, el programa debe decir: 
       "Error: Solo se permiten números reales".

    Usa float() en lugar de int() por si el usuario quiere poner 
    decimales (como 5.5), y atrapa el error ValueError."""

try:
    numero1 = float(input("Dame el primer valor: "))
    numero2 = float(input("Dame el segundo valor: "))
    resultado = numero1 + numero2
    print("El resultado es", resultado)
except ValueError:
    print("Los valores deben ser numeros flotantes")
