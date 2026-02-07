""" Operaciones con conjuntos DIFERENCIA SIMETRICA  

    Diferencia Simétrica: Elementos en s1 o s2, pero no en ambos.
    s1 ^ s2     o   s1.symmetric_difference(s2)

"""

mis_dulces = {"Fresa", "Menta"}
tus_dulces = {"Menta", "Chocolate"}

distintos = mis_dulces ^ tus_dulces
distintos2 = mis_dulces.symmetric_difference(tus_dulces)

print(distintos) # Resultado: {'Chocolate', 'Fresa'}
print(distintos2)
