""" Diccionario de Cubos

    Crea un diccionario donde las claves sean los números del 1 al 5 
    y los valores sean esos números elevados al cubo (n ^ 3).
    
    Pista: Usa range(1, 6) y el operador de potencia **3."""

diccionario_al_cubo = {x: x ** 3 for x in range(1, 6)}

print('El diccionario es:', diccionario_al_cubo)
