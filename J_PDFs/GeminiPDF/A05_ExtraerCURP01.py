""" EXTRAER DATOS DE LA CURP

    ¿Por qué lo hicimos así?
    Nombre: Según el documento, el nombre OSCAR ALAN RAMIREZ CORDOVA aparece 
    debajo de la etiqueta "Nombre". El código busca esa palabra y corta el 
    texto hasta donde empieza la siguiente etiqueta ("Entidad") para no traer 
    basura.Clave: 
    Para la clave RACO900531HGRMRS04, usamos una Expresión Regular (re). Es 
    más seguro porque las claves CURP siempre tienen esa misma estructura de 
    letras y números, así que Python la encuentra sin importar en qué parte de 
    la hoja esté.Entidad: 
    Buscamos la frase exacta "Entidad de registro:" y tomamos lo que está en 
    esa misma línea, que en este caso es GUERRERO.Un consejo prácticoEn tu 
    archivo, el nombre aparece dos veces. Si notas que el código extrae texto 
    extra, puedes ajustar el .split() para que sea más preciso.

    La palabra <import re> es la abreviatura de Regular Expressions 
    (Expresiones Regulares). Al escribir import re, le estás pidiendo a Python 
    que saque de su caja de herramientas un "escáner de patrones" especializado.

    La Analogía: El Detective y el Retrato Hablado
    Imagina que estás buscando a una persona en una multitud:

    Búsqueda normal (split o in): Es como buscar a alguien solo si sabes su nombre 
    exacto: "Busca a Oscar Alan". Si el nombre tiene un espacio de más o una letra 
    distinta, no lo encuentras.

    Expresiones Regulares (re): Es como darle al detective un retrato hablado o una 
    descripción física: "Busca a alguien que mida 1.80m, use lentes rojos y tenga una 
    cicatriz en la frente". No necesitas saber su nombre; el detective encontrará a c
    ualquiera que encaje con esa descripción.

    ¿Por qué lo usamos para la CURP?
    La clave es RACO900531HGRMRS04. Nota que tiene una estructura muy específica:

    1)  4 letras al inicio.
    2)  6 números (la fecha).
    3)  6 letras más.
    4)  2 números al final.

    En lugar de decirle a Python: "Busca el texto RACO900531...", usamos re para decirle: 
    "Busca cualquier texto que tenga 4 letras, luego 6 números, luego 6 letras y 2 números".


"""
from pypdf import PdfReader

# 1. Cargamos el lector con tu archivo CURP.pdf
ruta = "/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/GeminiPDF/CURP.pdf"

lector = PdfReader(ruta)
texto = lector.pages[0].extract_text()

# 2. Definimos funciones de limpieza para evitar espacios extra
def limpiar(texto_sucio):
    return texto_sucio.strip()

# --- EXTRACCIÓN DE DATOS ---
# El nombre aparece después de la etiqueta 'Nombre' [cite: 5, 7]
# En este PDF específico, el nombre está en la línea siguiente o después de un espacio
if "Nombre" in texto:
    # Dividimos y tomamos lo que sigue a la etiqueta 
    nombre_completo = texto.split("Nombre")[1].split("Entidad")[0]
    nombre_variable = limpiar(nombre_completo)

# La Clave (CURP) suele estar cerca de la parte superior [cite: 3, 4]
# Buscamos la cadena que tiene el formato de la CURP 
import re
patron_curp = r'[A-Z]{4}\d{6}[A-Z]{6}\d{2}'
resultado_curp = re.search(patron_curp, texto)
if resultado_curp:
    clave_variable = resultado_curp.group()

# La Entidad de registro 
if "Entidad de registro:" in texto:
    entidad_texto = texto.split("Entidad de registro:")[1].split("\n")[0]
    entidad_variable = limpiar(entidad_texto)

# --- RESULTADOS ---
print(f"Nombre extraído: {nombre_variable}")
print(f"Clave extraída: {clave_variable}")
print(f"Entidad: {entidad_variable}")

