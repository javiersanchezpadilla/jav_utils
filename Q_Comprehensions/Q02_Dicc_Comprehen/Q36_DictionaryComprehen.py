""" Directorio de Usuarios

    Tienes una lista de nombres de usuario en minúsculas. 
    Crea un diccionario donde la clave sea el nombre original y el 
    valor sea el nombre con la primera letra en mayúscula (usando .capitalize()).

        usuarios = ["pedro", "lucia", "carlos"]
"""

usuarios = ["pedro", "lucia", "carlos"]

directorio = {usuario: usuario.capitalize() for usuario in usuarios}

print('Lista de ususario original', usuarios)
print('Diccionario', directorio)

