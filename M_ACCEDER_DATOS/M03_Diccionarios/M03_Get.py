""" {}.get(llave, retorno).

    Regresa el valor en caso de existir, en otro caso no marca error, esto es,
    si la llave buscada no existe no interrumpe el progama, podemos adema 
    especificar el valor de retorno en caso de no existir la llave"""

a = {"x" : 10}
b = a.get("x", 0)
c =  a.get("y", None)

print(f'b = {b}')
print(f'c = {c}')
