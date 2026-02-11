""" No rompe tu código (Inspección en cadena)

    A diferencia de print(), que devuelve "nada" (None), ic() devuelve 
    el mismo valor que imprime. Esto te permite meterlo en medio de una 
    operación:

"""
from icecream import ic 

# Con print esto daría error al intentar sumar
# Con ic, imprime el valor y permite que la suma continúe
resultado = ic(10) + ic(20) 

# Pantalla:
# ic| 10
# ic| 20

