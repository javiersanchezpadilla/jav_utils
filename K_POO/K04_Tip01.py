""" Si solo usamos las clases para almacenar datos, tal como se muestra
    en el ejemplo

    class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre 


    usuario01 = Usuario(1, 'Karla')
    print(usuario01.__dict__)   # {'id': 1, 'nombre': 'Karla'}

    Podemos hacerlo de una forma mas eficiente
    Donde se inicializa (__init__) de forma automatica

    Si queremos ver la información como un diccionario debemos importar 'asdict'
"""

from dataclasses import dataclass, asdict 

@dataclass
class Usuario:
    id: int
    nombre: str 
    es_admin: bool = False 


usuario01 = Usuario(1, 'Karla')
print(usuario01)

# Podemos comparar automaticamente
usuario02 = Usuario(1, 'Karla')
print(usuario01 == usuario02)

# PAra ver la información como un diccionario importamos 'asdict'
print(asdict(usuario01))


