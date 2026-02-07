""" Resumen rápido:
    ----------------
    namedtuple      Crea objetos pequeños que se comportan como tuplas pero 
                    tienen nombres para sus campos.
    Legibilidad     Hace que tu código parezca escrito en inglés/español natural
                    en lugar de usar números de posición.
    Regla de oro    Si tus datos no deben cambiar (inmutables) y quieres que se 
                    entiendan a primera vista, usa una namedtuple.

"""
from collections import namedtuple

Usuario = namedtuple('Usuario', 'nombre edad profesion')
persona = Usuario('Javier', 30, 'Programador')

print(f"{persona.nombre} es {persona.profesion}.")
# Es mucho más claro que decir persona[0] y persona[2]