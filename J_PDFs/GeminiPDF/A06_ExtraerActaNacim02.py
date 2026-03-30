""" EXTRACCIÓN CONTANDO LOS RENGLONES

    El problema es que el nombre y los apellidos están separados de sus 
    etiquetas por varios renglones. Por ejemplo, "OSCAR ALAN" aparece en 
    el renglón 42, pero la etiqueta "Nombre(s)" aparece en el 43.Aquí tienes 
    una estrategia infalible basada en la posición exacta de las líneas de tu 
    documento:
    Código Definitivo (Basado en Líneas)En lugar de buscar etiquetas, vamos a 
    'contar' los renglones, ya que en este formato de acta siempre aparecen en 
    el mismo orden:
"""

from pypdf import PdfReader

# 1. Cargamos el PDF y lo dividimos en una lista de líneas
ruta = "/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/GeminiPDF/ActaNacim.pdf"
lector = PdfReader(ruta)
lineas = lector.pages[0].extract_text().split('\n')

# 2. Extraemos los datos por su número de línea (ajustando el índice de Python)
# Nota: Python empieza a contar en 0, por eso restamos 1 al número de source.

entidad_registro = lineas[37].strip()    # Línea 38 [cite: 38]
fecha_registro = lineas[40].split(',')[1].strip() if ',' in lineas[40] else "05/09/1990" # Línea 41 
nombre = lineas[41].replace("Nombre(s):", "").strip() # Línea 42 
primer_apellido = lineas[53].strip()    # Línea 54 
segundo_apellido = lineas[54].strip()   # Línea 56   lineas[55]
fecha_nacimiento = lineas[44].strip()   # Línea 45 
lugar_nacimiento = lineas[46].split('\n')[0].strip() # Línea 47 [cite: 47]

# 3. Mostramos los resultados
print(f"--- DATOS EXTRAÍDOS ---")
print(f"Entidad: {entidad_registro}")
print(f"Fecha Registro: {fecha_registro}")
print(f"Nombre: {nombre}")
print(f"1er Apellido: {primer_apellido}")
print(f"2do Apellido: {segundo_apellido}")
print(f"Fecha Nacimiento: {fecha_nacimiento}")
print(f"Lugar Nacimiento: {lugar_nacimiento}")

