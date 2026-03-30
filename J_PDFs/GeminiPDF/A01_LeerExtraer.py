""" Extraer datos de un PDF

    leer un PDF y crear un PDF son tareas tan distintas que normalmente 
    usamos herramientas diferentes para cada una.

    PyPDF2  (o su versión más moderna pypdf): Para leer, cortar, pegar 
            y extraer partes de archivos existentes.

    FPDF2:  Para crear reportes desde cero (escribir texto, poner imágenes 
            y tablas).

    1. Leer y Extraer partes (pypdf)
    --------------------------------
    Un PDF es como un álbum de fotos pegado con pegamento fuerte. No es como 
    un archivo de Word que puedes editar fácilmente; más bien, tienes que 
    "despegar" las páginas que te sirven.

    Instalación: 
    
            pip3 install pypdf

    Ejemplo: Extraer la primera página de un PDF
"""
from pypdf import PdfReader, PdfWriter

        # 1. Cargamos el archivo original (Leer)
ruta = '/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/MergePDFs' \
       '/DocumentarClases.pdf'
lector = PdfReader(ruta)

        # 2. Creamos un "escritor" vacío para nuestro nuevo archivo
escritor = PdfWriter()

        # 3. Tomamos solo la página tres (es como un indice inicia de 0)
        # 0=Pág.1, 1=Pág.2, 2=Pág.3, 3=Pág.4, etc
primera_pagina = lector.pages[2]
escritor.add_page(primera_pagina)

        # 4. Guardamos el resultado
with open("pagina3.pdf", "wb") as archivo_salida:
    escritor.write(archivo_salida)

print("¡Página extraída con éxito!")
