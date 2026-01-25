""" En este programa se importa el módulo P01_metodo_all_
    que contiene el método especial __all__.py
    y se utiliza para importar solo las funciones definidas en __all__.
    Se importan las funciones f1 y f2, pero no f3 ni f4"""

# from P_MetEspeciales_DUNDERS.P01_metodo_all_ import *
from P01_metodo_all_ import *

f1()
f2()

# f3()  # Esto generará un error porque f3 no está en __all__
# f4()  # Esto generará un error porque f4 no está en __all__
print(f"TASA_IMPUESTOS: {TASA_IMPUESTOS}")