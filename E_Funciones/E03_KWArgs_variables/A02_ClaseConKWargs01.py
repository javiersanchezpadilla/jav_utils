""" VEamos un ejemplo sencillo donde asignamos adecuadamente los valores de los
    kwargs, en este ejemplo no nos equivocaremos y ademas estamos obligados a 
    pasar todos y cada uno de los valores iniciales 
"""

class Carro:
    def __init__(self, **kwargs):
        self.marca = kwargs['marca']
        self.modelo = kwargs['modelo'] 
        self.color = kwargs['color']
        self.puertas = kwargs['puertas']
        # self.modelo = kwargs['marka']   # ERROR!!!! no existe marka (con 'k')


mi_carro = Carro(marca='Nissan', modelo=2025, color='rojo', puertas=2)
print(mi_carro.marca)
print(mi_carro.modelo)
print(mi_carro.color)
print(mi_carro.puertas)
