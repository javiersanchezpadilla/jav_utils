""" En Python, get() se utiliza principalmente con diccionarios para acceder a 
    valores de manera segura
    
    mi_diccionario = {"a": 1, "b": 2}
    valor_a = mi_diccionario.get("a")  # Devuelve 1
    valor_c = mi_diccionario.get("c")  # Devuelve None
    valor_c_default = mi_diccionario.get("c", 0)  # Devuelve 0
    """

def convierte_unidades(valor, unidad_origen, unidad_destino):
    """
    Convierte un valor de una unidad a otra.
    
    :param valor: El valor a convertir.
    :param unidad_origen: La unidad del valor original.
    :param unidad_destino: La unidad a la que se desea convertir.
    :return: El valor convertido a la nueva unidad.
    """

    tazas_de_conversion = {
        ('millas', 'kilometros'): 1.60934,  # Millas a Kilómetros
        ('kilometros', 'millas'): 0.621371,  # Kilómetros a Millas
        ('metros', 'centimetros'): 100,      # Metros a Centímetros
        ('centimetros', 'metros'): 0.01,  # Centímetros a Metros
        ('metros', 'milimetros'): 1000,  # Metros a Milímetros
        ('milimetros', 'metros'): 0.001,  # Milímetros a Metros
        ('metros', 'yardas'): 1.09361,  # Metros a Yardas
        ('yardas', 'metros'): 0.9144,  # Yardas a Metros
        ('metros', 'pies'): 3.28084,  # Metros a Pies
        ('pies', 'metros'): 0.3048,  # Pies a Metros
        ('metros', 'pulgadas'): 39.3701,  # Metros a Pulgadas
        ('pulgadas', 'metros'): 0.0254  # Pulgadas a Metros
    }

    if (unidad_origen, unidad_destino) not in tazas_de_conversion:
        raise ValueError(f"No se puede convertir de {unidad_origen} a {unidad_destino}")

    factor_conversion = tazas_de_conversion.get((unidad_origen, unidad_destino))
    conversion = valor * factor_conversion

    return valor * conversion

# Ejemplo de uso
if __name__ == "__main__":
    try:
        valor = 10
        unidad_origen = 'metros'
        unidad_destino = 'centimetros'
        
        resultado = convierte_unidades(valor, unidad_origen, unidad_destino)
        print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}")
    except ValueError as e:
        print(e)