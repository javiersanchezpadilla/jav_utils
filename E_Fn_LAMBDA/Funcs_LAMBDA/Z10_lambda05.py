""" El Filtro de Mensajes Largos (filter)

    La función filter() sirve para dejar pasar solo los elementos que cumplen 
    una condición (como un guardia de seguridad).

    Entrada: palabras = ["sol", "computadora", "paz", "programacion"]
    Misión: Crea una lista que solo tenga las palabras con más de 5 letras.
    Pista: largas = list(filter(lambda s: len(s) > 5, palabras))"""

palabras = ["sol", "computadora", "paz", "programacion"]
largas = list(filter(lambda palabra: len(palabra) > 5, palabras))

print('Lista de palabras original', palabras)
print('Lista de palabras con mas de cinco letras', largas)

