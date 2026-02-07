""" LA TUPLA INMUTABLE MUTABLE

    Al igual que con la lista, el diccionario es mutable. Esto significa que 
    puedes cambiar sus valores, agregar nuevas etiquetas (llaves) o quitarlas, 
    y la tupla no se quejará porque la "caja de archivos" sigue siendo la misma.

   ¿Qué es lo que NO puedes hacer?
   -------------------------------
    Para que quede clarísimo qué es lo que protege la tupla, intenta imaginar esto:

    SÍ PUEDES: Cambiar el contenido de la caja (el diccionario).
    NO PUEDES: Quitar la caja y poner una nueva.

    Si intentas hacer esto, Python lanzará un error: 

    Python te dirá: "Oye, me prometiste que en la posición 1 siempre estaría ese 
    objeto específico, no me lo cambies por otro".

    Estructura      ¿Es mutable?        Qué pasa dentro de una Tupla?
    ------------------------------------------------------------------
    Enteros/Texto       No              No se pueden cambiar.
    Listas              Sí              Se pueden modificar sus elementos.
    DiccionarioS        Sí              se pueden cambiar/añadir llaves y valores.
    Otras Tuplas        No              Son totalmente fijas.

    Un consejo de "buena práctica":
    -------------------------------
    Aunque Python permite meter cosas mutables dentro de tuplas, a veces puede 
    ser confuso para otros programadores que esperan que una tupla sea 100% 
    fija. Úsalo con sabiduría, principalmente cuando la "estructura" deba ser 
    fija pero los "datos" necesiten actualizarse.
"""

# Una tupla que representa un servidor
# Posición 0: Nombre del servidor (Texto - Inmutable)
# Posición 1: Configuración (Diccionario - Mutable)
servidor = ("Servidor_Proyectos", {"ip": "192.168.1.1", "estado": "activo"})

print("Antes:", servidor)

# 1. Modificamos un valor dentro del diccionario
servidor[1]["estado"] = "mantenimiento"

# 2. Agregamos una nueva llave-valor al diccionario
servidor[1]["puerto"] = 8080

print("Después:", servidor)
