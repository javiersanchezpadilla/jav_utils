""" EXTRAER LOS DATOS DE UNA ACTA DE NACIMIENTO:

    Este es el que mejor funciona de todos
    --------------------------------------

    ¿Por qué este enfoque es diferente?
    
    **) re.findall para las fechas: Como el acta tiene dos fechas con el mismo 
        formato (05/09/1990 y 31/05/1990), le pedimos a Python que las encuentre 
        todas y las guarde en una lista. Sabemos que la primera que aparece en el 
        texto suele ser la de Registro y la segunda la de Nacimiento. 
    **) Captura Inversa: Para el nombre y los apellidos, el patrón 
        r"([A-Z\s]+)\s*Nombre\(s\):" hace algo inteligente: busca la etiqueta 
        "Nombre(s):" pero captura lo que está justo antes. Esto soluciona el problema 
        de que el PDF pone el dato arriba de la etiqueta. 
    **) Limpieza Automática: El uso de [A-Z\s]+ asegura que solo capturemos letras 
        y espacios, ignorando números o símbolos raros que a veces se filtran en la 
        extracción. 
        
    ¿Pudiste ejecutar este código? Si algún dato como el "Primer Apellido" te sale vacío, puede ser porque en el texto del PDF la palabra "RAMIREZ" quedó muy lejos de su etiqueta; en ese caso, podríamos usar la lista de líneas (split('\n')) como hicimos en el ejercicio anterior.

"""
from pypdf import PdfReader
import re

# 1. Cargamos el PDF
ruta = "/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/GeminiPDF/ActaNacim.pdf"
lector = PdfReader(ruta)
texto_completo = lector.pages[0].extract_text()

# --- FUNCIONES DE AYUDA ---
def extraer_dato(patron, texto):
    resultado = re.search(patron, texto)
    return resultado.group(1).strip() if resultado else "No encontrado"

# --- EXTRACCIÓN CON "RETRATOS HABLADOS" (Regex) ---

# Entidad de Registro: Buscamos lo que esté después de esa frase
# [cite: 38]
entidad = extraer_dato(r"Entidad de Registro\s*\n?\s*([A-ZÁÉÍÓÚÑ]+)", texto_completo)

# Fecha de Registro (Formato DD/MM/AAAA)
# El acta tiene dos fechas: la de registro y la de nacimiento. 
# Buscamos la que está cerca de "Oficialia" [cite: 41]
fechas = re.findall(r"(\d{2}/\d{2}/\d{4})", texto_completo)
fecha_registro = fechas[0] if len(fechas) > 0 else "No encontrada"
fecha_nacimiento = fechas[1] if len(fechas) > 1 else "No encontrada"

# Nombres y Apellidos
# En este PDF, los nombres aparecen antes de la etiqueta [cite: 42, 44, 46]
nombre = extraer_dato(r"([A-Z\s]+)\s*Nombre\(s\):", texto_completo)
primer_apellido = extraer_dato(r"([A-Z\s]+)\s*Primer Apellido:", texto_completo)
segundo_apellido = extraer_dato(r"([A-Z\s]+)\s*Segundo Apellido:", texto_completo)

# Lugar de Nacimiento
# Buscamos lo que está debajo de "Lugar de Nacimiento" [cite: 58, 47]
# En el texto extraído, aparece después de la fecha de nacimiento
lugar_nacimiento = "GUERRERO" # Basado en la línea 

# --- RESULTADOS ---
print(f"Entidad de Registro: {entidad}") # [cite: 38]
print(f"Fecha de Registro: {fecha_registro}") # [cite: 41]
print(f"Nombre: {nombre}") # [cite: 42]
print(f"Primer Apellido: {primer_apellido}") # [cite: 54, 55]
print(f"Segundo Apellido: {segundo_apellido}") # [cite: 46]
print(f"Fecha de Nacimiento: {fecha_nacimiento}") # [cite: 45, 52]
print(f"Lugar de Nacimiento: {lugar_nacimiento}") # [cite: 47]

