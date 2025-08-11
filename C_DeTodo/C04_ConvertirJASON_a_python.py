""" PAra este ejercicios no se requiere instalar la libreria json,
    ya que es parte de la librería estándar de Python.
"""

import json

json_string = "Hola mundo"
json_int = "541"
json_float = "3.14"
json_list = "[1, 2, 3, 4, 5]"
json_dict = '{"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}'
json_bool = "true"
json_none = "null"

# Convertir JSON a Python
python_string = json_string   # Para cadenas, no es necesario convertir
python_int = json.loads(json_int)
python_float = json.loads(json_float)
python_list = json.loads(json_list)
python_dict = json.loads(json_dict)     
python_bool = json.loads(json_bool)
python_none = json.loads(json_none)

# Imprimir los resultados
print("Cadena:", python_string)
print("Entero:", python_int)
print("Flotante:", python_float)
print("Lista:", python_list)
print("Diccionario:", python_dict)
print("Booleano:", python_bool)
print("Nulo:", python_none)


