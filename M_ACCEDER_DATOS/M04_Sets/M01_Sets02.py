""" Operaciones con conjuntos UNION

    (|)     Unión : Juntar todos los elementos de todos los conjuntos

    Unión (Union): Combina elementos de ambos conjuntos.
        s1 | s2     o   s1.union(s2).
"""

mis_dulces = {"Fresa", "Menta"}
tus_dulces = {"Menta", "Chocolate"}

todos = mis_dulces | tus_dulces
todos2 = mis_dulces.union(tus_dulces)

print(todos) # Resultado: {'Fresa', 'Menta', 'Chocolate'}
print(todos2)
