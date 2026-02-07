# Mi lista "Caja de Herramientas"
mi_lista_mixta = [
    42,                         # 1. Entero (int)
    True,                       # 2. Booleano (bool)
    "Hola Python",              # 3. Texto (str)
    [10, 20, 30],               # 4. Una lista dentro de otra (list)
    {"nombre": "Ana", "id": 1}, # 5. Diccionario (dict)
    (5, 9),                     # 6. Tupla (tuple) - inmutable
    {1, 2, 3}                   # 7. Conjunto (set) - sin repetidos
]

# Vamos a ver qué hay adentro con un pequeño truco
for elemento in mi_lista_mixta:
    print(f"Valor: {elemento}  ---> Tipo: {type(elemento)}")
