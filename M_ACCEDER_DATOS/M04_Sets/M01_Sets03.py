""" Operaciones con conjuntos INTERSECCIÓN

    (&)     Intersección : Valores iguales entre ambos conjuntos

    Intersección (Intersection): Elementos comunes.
        s1 & s2     o   s1.intersection(s2)
"""

mis_dulces = {"Fresa", "Menta"}
tus_dulces = {"Menta", "Chocolate"}

comunes = mis_dulces & tus_dulces
comunes2 = mis_dulces.intersection(tus_dulces)

print(comunes)      # Resultado: {'Menta'}
print(comunes2)
