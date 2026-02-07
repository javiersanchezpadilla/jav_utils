""" Al unir los diccinarios podemos segmentar la instrucción

    Recordar que los diccionarios no admiten llaves repetidas, por lo que
    la última que se reconoce es la que gana y se queda como valida
    en este ejemplo se sobreescriben las llaves, por eso las variables se
    llaman 'sobreescribe...', el resultado es:

        {'timeout': 10, 'debug': True}
"""


valores_por_defecto = {"timeout": 30, "debug": False}
sobreescribe_por_entorno = {"timeout": 10}
sobreescribe_por_usuario = {"debug": True}

config = valores_por_defecto \
    | sobreescribe_por_entorno \
    | sobreescribe_por_usuario

print(config)
