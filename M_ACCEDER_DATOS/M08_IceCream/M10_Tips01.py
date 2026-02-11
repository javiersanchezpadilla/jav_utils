""" Personalizar el mensaje de salida

    Si sientes que la salida de ic() ensucia mucho tu consola con el prefijo 
    ic|, puedes personalizarlo:"""

from icecream import ic
from collections import namedtuple

                        # 1. Creamos el "molde" para nuestras mascotas
Mascota = namedtuple('Mascota', ['nombre', 'especie', 'edad'])

                        # 2. Creamos un par de pacientes
perro = Mascota(nombre="Max", especie="Canino", edad=5)
gato = Mascota(nombre="Luna", especie="Felino", edad=3)

                        # 3. ¡A inspeccionar con IceCream!
ic(perro)
ic(gato.nombre)         # También podemos ver solo una parte

                        # 4. Probemos algo más complejo: una lista de mascotas
pacientes = [perro, gato]
ic(pacientes)

                        # Ahora verás: DEBUG >>> perro: Mascota(...)
ic.configureOutput(prefix='DEBUG >>> ')
ic(perro)
