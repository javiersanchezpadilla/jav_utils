""" Funcion qie revibe una palabra y la
    imprime en forma de pirámide """

def imprimir_piramide(palabra):
    """ Imprime la palabra en forma de pirámide """
    longitud = len(palabra)
    for i in range(longitud):
        print(palabra[:i + 1])
              

palabra_de_ejemplo = "Python"
imprimir_piramide(palabra_de_ejemplo)
# Salida esperada:
# P
# Py
# Pyt
# Pyth
# Pytho
# Python            