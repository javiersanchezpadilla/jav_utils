numero = 7
numero_con_ceros = str(numero).zfill(5)
otro_numero_con_ceros = f"{numero:03}"

print(numero_con_ceros)  # Output: 00007
print(otro_numero_con_ceros)  # Output: 007

print(f"El número con ceros a la izquierda es: {numero_con_ceros}")
print(f"El otro número con ceros a la izquierda es: {otro_numero_con_ceros}")
print(f"El número original es: {numero}")
