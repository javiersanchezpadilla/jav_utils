""" EXTRAYENDO UN CORREO ELECTRONICO.

    ¿Cómo hacerlo de forma más "Profesional"? (RegEx)
    Si el dato que buscas tiene un formato fijo (como un RFC, un correo 
    electrónico o una fecha), lo mejor es usar Expresiones Regulares (re). 
    Es como darle a Python una "foto" de cómo se ve el dato para que lo 
    busque por su forma.

    Ejemplo para extraer un correo electrónico:

    Consideraciones Importantes:
    PDFs de Imagen (Escaneados): Si el PDF es una foto (no puedes seleccionar 
    el texto con el mouse), pypdf no podrá leerlo. En ese caso necesitarías 
    herramientas de OCR (Reconocimiento Óptico de Caracteres) como pytesseract.

    Limpieza de datos: A veces el texto viene con saltos de línea extraños. 
    Siempre es bueno usar .strip() para limpiar espacios al principio y al final.
"""

import re
from pypdf import PdfReader

lector = PdfReader("archivo.pdf")
texto = lector.pages[0].extract_text()

# Buscamos algo que tenga formato de email: texto + @ + texto + . + texto
patron_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

resultado = re.search(patron_email, texto)

if resultado:
    mi_variable_email = resultado.group()
    print(f"Email encontrado: {mi_variable_email}")
