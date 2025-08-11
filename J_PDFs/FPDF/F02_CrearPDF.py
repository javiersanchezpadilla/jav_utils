""" PAra este ejercicio se necesita instalar la librería FPDF y 
    ademas la libreria streamlit para poder visualizar el PDF

    pip3 install fpdf streamlit

    Video tomado de youtube: https://www.youtube.com/watch?v=0-zXp2MZ-aY
"""

# Importamos las librerías necesarias
from fpdf import FPDF
import streamlit as st

# Creamos una clase heredada de FPDF
class PDF(FPDF):

    """ Modificamos la clase FPDF para agregar encabezado y pie de página """
    def header(self):
        if hasattr(self, 'titulo_de_documento'):
            # Si existe un título, lo usamos
            self.set_title(self.titulo_de_documento)
                      # familia  estilo tamaño
            self.set_font("Arial", "B", 12)
            # Añadimos el título al encabezado
            #         w   h       texto             border ln  align
            self.cell(0, 10, self.titulo_de_documento, 0,   1,  "C")
            # width=0       inicia desde el inicio de la página hasta el margen derecho
            # height=10     La celda tiene una altura de 10 puntos
            # text          es el texto que se desplegará
            # border=0      Indica que la celda no tendrá borde
            # ln=1          El cursor no se queda en la misma linea, avanza una nueva linea 
            #               0 no hace salto de línea, 1 hace salto de línea
            # align='C'     Alinea el texto al centro

    def footer(self):
        # Posicionamos el cursor a 15 pixeles del final de la página hacia arriba
        self.set_y(-15)
        # Establecemos la fuente para el pie de página
        self.set_font("Arial", "I", 8)
        # Añadimos el número de página
        #         w   h    texto  Fn de la clase border ln  align
        self.cell(0, 10, f"Página {self.page_no()}", 0,  0, "C")

    def chapter_title(self, title, fuente='Arial', tamanio_fuente=12):
        """ Añade un título de capítulo """
        self.set_font(fuente, "B", tamanio_fuente)
        #         w  h  texto border ln  align   ln=1 aplicamos salto de línea
        self.cell(0, 10, title, 0,    1, "L")
        self.ln(10) # Añadimos un salto de línea de 10 puntos por debajo del título

    def chapter_body(self, texto_cuerpo, fuente='Arial', tamanio_fuente=12):
        """ Añade el cuerpo del capítulo """
        self.set_font(fuente, "", tamanio_fuente)
        # Añadimos el texto del cuerpo
        #                w  h  texto         border ln  align
        self.multi_cell(0, 10, texto_cuerpo)
        self.ln()   


def create_pdf(nombre_archivo, titulo_documento, autor, capitulos, ruta_de_imagenes=None):
    """ Crea un PDF con los capítulos proporcionados """
    pdf = PDF()
    pdf.document_title = titulo_documento

    # Añadimos una página al PDF
    pdf.add_page()

    if autor:
        # Establecemos el autor del documento
        pdf.set_author(autor)

    # Esto es opcional, por si establecemos una ruta de una imagen para el doumento
    if ruta_de_imagenes:
        # Establecemos la ruta de la imagen si se proporciona
        #         ruta de la imagen  La posicion  ancho de la imagen menos 20 pixeles
        pdf.image(ruta_de_imagenes, x=10, y=25,   w=pdf.w -20) 
        pdf.ln(120)  # Añadimos un salto de línea para separar la imagen del contenido

    for capitulo in capitulos:
        titulo, cuerpo, font, tamanio = 


# <<<<<<<<<<<<<            PENDIENTE, HASTA AQUI VOY DEL MINUTO 8:50      >>>>>>>>>>>>>>>><<