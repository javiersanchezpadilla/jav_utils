""" Desarrollando una calculadora"""

def calcular(valor_inicial, **operacion_valor):
    valor_inicial += operacion_valor['sumar']
    valor_inicial *= operacion_valor['multiplicar']
    valor_inicial -= operacion_valor['restar']
    return valor_inicial


print(calcular(10, sumar=10, multiplicar=3, restar=1))

