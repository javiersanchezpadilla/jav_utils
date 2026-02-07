""" Desempaquetado en Bucle for

    Esto lo vimos un poco cuando hablamos de zip. Es súper útil para leer 
    listas que contienen tuplas (como una agenda).
"""
                    # Lista de tuplas (Nombre, Edad)
usuarios = [("Ana", 25), ("Beto", 30), ("Carla", 22)]

                    # Desempaquetamos directamente en el ciclo
for nombre, edad in usuarios:
    print(f"{nombre} tiene {edad} años.")
