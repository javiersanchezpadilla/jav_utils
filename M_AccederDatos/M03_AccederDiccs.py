""" Acceder a los diccionarios 'a lo bruto' puede costar muy caro   
    cuando accedemos a un elemento llave, y esté no existe en automatico
    tendremos un error, para evitar esto, debemos usar la funcion 
    
        get(elemento)



"""

datos = {"precio": 100}

# nos manda un error, debido a que la clave "cantidad" no existe
# --------------------------------------------------------------
# line 13, in <module>
#     print(datos["cantidad"])
#           ~~~~~^^^^^^^^^^^^
# print(datos["cantidad"])

# PAra evitar este error debemos usar un acceso seguro a traves de 'get'
# en caso de no existir, retornará simplemente None como resultado
print(datos.get("cantidad"))

