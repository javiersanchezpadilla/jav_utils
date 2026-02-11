""" Registro de Mascotas

    Imagina que trabajas en una veterinaria. Vamos a usar una namedtuple 
    para crear la ficha de cada mascota y luego usaremos ic() para 
    inspeccionar qué hay dentro.

    ¿Qué verás en tu pantalla?
    --------------------------
    Lo increíble de ic() es que te mostrará algo así:

    ic| perro: Mascota(nombre='Max', especie='Canino', edad=5)
    ic| gato.nombre: 'Luna'
    ic| pacientes: [Mascota(nombre='Max', ...), Mascota(nombre='Luna', ...)]

    ¿Por qué esta combinación es tan buena?
    ---------------------------------------
    A) Claridad Total: Al usar namedtuple, los datos ya vienen con etiquetas. 
       Al usar ic(), Python te dice exactamente a qué variable pertenecen esas 
       etiquetas.
    B) Ahorro de tiempo: Si usaras print(), tendrías que escribir: 
       print(f"Datos del perro: {perro}"). Con IceCream solo escribes 
       ic(perro) y él hace todo el trabajo de formateo por ti.
    C) Detección de tipos: Si por error a la edad le pasas un texto en lugar 
       de un número, ic() te lo mostrará con comillas '5', ayudándote a ver el
       error de inmediato.
"""

from icecream import ic
from collections import namedtuple

# 1. Creamos el "molde" para nuestras mascotas
Mascota = namedtuple('Mascota', ['nombre', 'especie', 'edad'])

# 2. Creamos un par de pacientes
perro = Mascota(nombre="Max", especie="Canino", edad=5)
gato = Mascota(nombre="Luna", especie="Felino", edad=3)

# 3. ¡A inspeccionar con IceCream!
ic(perro)
ic(gato.nombre) # También podemos ver solo una parte

# 4. Probemos algo más complejo: una lista de mascotas
pacientes = [perro, gato]
ic(pacientes)