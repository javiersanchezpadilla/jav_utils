""" BUSCAMOS LOS DATOS POR NÚMERO DE LINEA:

    El Nombre: En lugar de buscar la palabra "Nombre" (que en tu archivo está 
    sola en la línea 5 ), fuimos directamente a la línea 7, donde está el 
    texto completo OSCAR ALAN RAMIREZ CORDOVA.La Entidad: Al separar el PDF 
    en una lista de líneas, podemos buscar específicamente la que dice "Entidad 
    de registro: GUERRERO". Al usar .split(":"), cortamos la etiqueta y nos 
    quedamos solo con la palabra GUERRERO.La Clave: Seguimos usando re porque 
    la clave RACO900531HGRMRS04 está en una posición un poco aislada  y es más 
    fácil que el "detective" la encuentre por su forma de letras y números
"""

from pypdf import PdfReader
import re

# 1. Cargamos el PDF
ruta = "/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/GeminiPDF/CURP.pdf"
lector = PdfReader(ruta)
# Extraemos el texto y lo dividimos por líneas para poder "contarlas"
lineas = lector.pages[0].extract_text().split('\n')

# 2. Extraer el Nombre
# En tu archivo, el nombre aparece en la línea 7 y se repite en la 12
# Usamos la línea 7 [índice 6 en Python]
nombre_variable = lineas[6].strip() #[cite: 7]

# 3. Extraer la Clave (CURP)
# Usamos el "retrato hablado" que ya conocemos (re) porque es lo más seguro
texto_completo = "\n".join(lineas)
patron_curp = r'[A-Z]{4}\d{6}[A-Z]{6}\d{2}'
busqueda_curp = re.search(patron_curp, texto_completo)
clave_variable = busqueda_curp.group() if busqueda_curp else "No encontrada" # [cite: 3]

# 4. Extraer la Entidad de registro
# Buscamos la línea que contiene "Entidad de registro:"
entidad_variable = "No encontrada"
for linea in lineas:
    if "Entidad de registro:" in linea:
        # Dividimos la línea por los dos puntos y tomamos lo que está a la derecha
        entidad_variable = linea.split("Entidad de registro:")[1].strip() # [cite: 8]
        break

# --- RESULTADOS ---
print(f"Nombre: {nombre_variable}")
print(f"Clave: {clave_variable}")
print(f"Entidad: {entidad_variable}")
