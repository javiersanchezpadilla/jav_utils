""" aparentemene requiere el uso de la librería re
pip3 install re"""


mi_password = input("Ingrese la contraseña: ")

if (len(mi_password) >= 8  and
    re.search(r"[A-Z]", pwd) and        # Busca al menos una mayúscula
    re.search(r"\d", pwd) and           # Busca al menos un número
    re.search(r"[!\"#$%()*]", pwd)):    # Busca al menos un carácter especial
    print("Contraseña segura")

else:
    print("Contraseña insegura")
    print("Debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial.")
