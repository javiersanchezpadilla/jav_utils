""" En esta segudna versión usaremos la funcion get, de tal manera, que si
    el ususario al momento de crear el objeto, omite agregar uno de los
    atributos esperados, de form automatica le asigna como valor None
"""

class Carro:
    def __init__(self, **kwargs):
        self.marca = kwargs.get('marca')
        self.modelo = kwargs.get('modelo')
        self.color = kwargs.get('color')
        self.puertas = kwargs.get('puertas')

    def __str__(self):
        res = f'Marca {self.marca}, Modelo {self.modelo}, Color {self.color} Puertas {self.puertas}'
        return res

mi_carro = Carro(marca='Nissan', modelo=2025, color='rojo', puertas=2)
mi_carro2 = Carro(marca='Volcho')

print(mi_carro)
print(mi_carro2)
