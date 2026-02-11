"""
    PAra instalarlo se requiere 
        $ pip3 install icecream

    Si estás cansado de usar print() para revisar qué está pasando dentro 
    de tu código, IceCream (ic) te va a encantar. Es como pasar de usar 
    una linterna vieja a encender los reflectores de un estadio.

    Imagina que estás revisando una caja llena de cables.
    Con print(), es como si pegaras una etiqueta que solo dice "5 voltios". 
    Al rato, ves la etiqueta y no recuerdas de qué cable era ese valor.
    Con IceCream, el post-it dice automáticamente: "Cable Rojo de la Fuente: 
    5 voltios". Te dice el nombre de la variable y el valor al mismo tiempo 
    sin que tú se lo pidas.


"""
suma = 10 + 20

# Cuando tienes muchos print(), ver un montón de números en la pantalla 
# es confuso porque no sabes a qué variable pertenecen.
print(suma) # En la pantalla solo sale: 30

from icecream import ic

nombre = "Javier"
edad = 30

ic(nombre)              # ic| nombre: 'Javier'
ic(edad)                # ic| edad: 30
