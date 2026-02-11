""" Saber "por dónde va" el programa

    A veces solo quieres saber si el código entró a un if o a una función.
    Si llamas a ic() vacío, te dice el archivo, la línea y la hora exacta."""

from icecream import ic 


def mi_funcion():
    ic()                    # Te dirá: ic| mi_archivo.py:3 in mi_funcion()

mi_funcion()
