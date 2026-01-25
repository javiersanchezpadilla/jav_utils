""" Este ejercicio es para practicar el uso de los métodos especiales en Python,
    en este caso el método __all__.py
    Este método especial se utiliza para definir qué nombres se exportan cuando
    se utiliza la instrucción from module import *.
    Si no se define __all__, se exportan todos los nombres que no comienzan con
    un guion bajo (_).
    Si se define __all__, solo se exportan los nombres que están en la lista __all__.
    En este caso, se define __all__ para exportar solo la función bajar"""

def f1():
    print("Función f1")

def f2():
    print("Función f2")

def f3():
    print("Función f3") 

def f4():
    print("Función f4")

# Definimos una constante
TASA_IMPUESTOS = 0.15

# Definimos __all__ para exportar solo f1 y f2 y la constante TASA_IMPUESTOS
# al hacer esto cuando se haga from P01_metodo_all_ import *
# solo se importarán f1 y f2, no f3 ni f4
__all__ = ['f1', 'f2', 'TASA_IMPUESTOS']
