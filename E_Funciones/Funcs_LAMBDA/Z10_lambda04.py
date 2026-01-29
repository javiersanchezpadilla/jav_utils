""" Lambdas con map y filter

    El verdadero potencial de las funciones lambda aparece cuando las usamos 
    para procesar listas completas.

    Reto: El Convertidor de Moneda (map)
    Imagina que tienes una lista de precios en Dólares y quieres convertirlos 
    a Pesos (suponiendo que 1 dólar = 20 pesos).

    Entrada: precios_usd = [10, 50, 100]

    Misión: Usa map() con una lambda para multiplicar cada precio por 20.

Pista: precios_mxn = list(map(lambda p: p * 20, precios_usd))"""

precios_usd = [10, 50, 100]

precios_mxn = list(map(lambda p: p * 20, precios_usd))

print('Lista en dolares', precios_usd)
print('Lista converida a pesos', precios_mxn)
