"""
    Para lograrlo, el proceso tiene tres pasos:

    1)  Cargar el PDF.
    2)  Extraer todo el texto de la página donde está el dato.
    3)  Filtrar ese texto para quedarnos solo con lo que necesitamos.

    La Analogía: El Tamiz de Arena
    Imagina que el texto de un PDF es un balde lleno de arena (palabras). 
    Lo que tú quieres es una pequeña pepita de oro (tu dato específico). 
    Para encontrarla, pasamos toda la arena por un tamiz (un filtro de código) 
    que deja pasar la arena y se queda solo con el oro.

    Ejemplo Práctico: Extrayendo un 'Folio'
    Supongamos que tienes un PDF y quieres guardar el número de folio que 
    siempre viene después de la palabra "Folio:".

    Se requiere: pip install pypdf

    ADVERTENCIA!!! Antes de ejecutar verificar que exista un documento con 
    una factura que cumpla lo que se marca aqui, de momento no funciona.
"""

from pypdf import PdfReader

# 1. Cargamos el documento
lector = PdfReader("factura_ejemplo.pdf")

# 2. Obtenemos el texto de la primera página
pagina = lector.pages[0]
texto_completo = pagina.extract_text()

# 3. Buscamos el dato específico
# Supongamos que el texto dice: "... El número de Folio: 12345 corresponde a..."
palabra_clave = "Folio:"

if palabra_clave in texto_completo:
    # Dividimos el texto donde aparece la palabra clave y tomamos lo que sigue
    partes = texto_completo.split(palabra_clave)
    
    # Tomamos la parte de la derecha [1] y limpiamos espacios
    # Usamos .split()[0] para agarrar solo la primera palabra después de 'Folio:'
    dato_extraido = partes[1].split()[0]
    
    # ¡Ya lo tenemos en una variable!
    print(f"El dato guardado en la variable es: {dato_extraido}")
else:
    print("No se encontró la palabra clave.")