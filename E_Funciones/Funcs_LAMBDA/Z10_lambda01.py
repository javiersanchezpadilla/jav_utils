""" ¿Qué es una función lambda?
    Es una función anónima (no tiene nombre) y se escribe en una sola línea. 
    Se usan para tareas rápidas y sencillas que no necesitan una estructura 
    completa de función con def.

    La estructura es:

            lambda argumentos : expresión
            
    Ejemplo Práctico: El Sumador
    Si quisiéramos una función que sume 10 a cualquier número:

"""
# Ambas funciones hacen lo mismo, pero la versión con lambda es más concisa.

def sumar_diez(n):                      # Forma tradicional (def):
    return n + 10

sumar_diez_lambda = lambda n : n + 10   # Forma con lambda


print(sumar_diez(5))                    # Resultado: 15
print(sumar_diez_lambda(5))             # Resultado: 15

