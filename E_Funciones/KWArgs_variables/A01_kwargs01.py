""" Manejo de **kwargs Key Word Aguments

    Argumentos ilimitados de llave valor (Diccionarios)"""

def calcular(**kwargs):
    print(kwargs)           # {'sumar': 10, 'multiplicar': 3, 'restar': 1}
    print(type(kwargs))     # <class 'dict'>


calcular(sumar=10, multiplicar=3, restar=1)
