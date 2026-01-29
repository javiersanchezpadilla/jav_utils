""" El Multiplicador Condicional

    Crea una lambda que reciba un número: si el número es par, 
    que lo multiplique por 2, si es impar, que lo deje igual.

    Pista: Puedes usar if-else dentro de la lambda: lambda x: x * 2 if x % 2 == 0 else x"""

multiplicador = lambda x: x ** 2 if x % 2 == 0 else x

print(multiplicador(1))
print(multiplicador(2))
print(multiplicador(3))
print(multiplicador(4))
