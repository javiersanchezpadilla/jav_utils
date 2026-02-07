""" Operaciones con conjuntos DIFERENCIA

    (-)     Diferencia A - B: Lo que esxiste en 'A' pero no en 'B'

    Diferencia (Difference): Elementos en s1 pero no en s2.
        s1 - s2     o   s1.difference(s2)
"""

mis_dulces = {"Fresa", "Menta"}
tus_dulces = {"Menta", "Chocolate"}

unicos_mios = mis_dulces - tus_dulces
unicos_mios2 = mis_dulces.difference(tus_dulces)

print(unicos_mios) # Resultado: {'Fresa'}
print(unicos_mios2)
