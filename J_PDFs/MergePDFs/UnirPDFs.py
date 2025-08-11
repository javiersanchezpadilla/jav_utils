""" Para este ejercicio se requiere instalar
    pip3 install PyPDF2

    Ejemplo tomado de: https://www.youtube.com/watch?v=kt0R-Txqhg4&t=239s

    En este ejemplo para ejecutar debemos desde consola ejecutar el programa
    con argumentos de la siguiente manera

    $ python3 UnirPDFs.py archivoPDF1.pdf archivoPDF2.pef archivoPDF3.pdf     
    En la ruta donde ejecutemos el archvo debemos tener los archvos PDFs a 
    combinar o unir entre si
"""

import PyPDF2
import sys

# Esta linea permite tomar los argumentos asignados desde la consola, como
# minimo toma uno hasta n
input = sys.argv[1:]

def pdf_combinador(lista_de_pdfs):
    combina_pdf = PyPDF2.PdfFileMerger()

    # unimos los archivos PDF
    for pdf in lista_de_pdfs:
        print(pdf)
        combina_pdf.append(pdf)

    # una vez unidos, ahora los guardamos como uno solo
    combina_pdf.write('archivo_final_pdf.pdf')


pdf_combinador()
