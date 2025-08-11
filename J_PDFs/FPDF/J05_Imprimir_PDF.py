""" Imprimir un documento PDF 
    usando la libreria fpdf
    
    pip3 install fpdf
    """


from fpdf import FPDF

# crear un objeto PDF
pdf = FPDF()

# Agregar una página
pdf.add_page()

# Establecer una fuente
pdf.set_font("Arial", size=15)

# Añadir un título
pdf.cell(200, 10, txt="Imprimir PDF con FPDF", ln=True, align='C')

# Añadir un texto
pdf.cell(50, 10, txt="Este es un ejemplo de cómo imprimir un PDF usando la librería FPDF.", ln=True, align='L')

# Añadir más texto
pdf.multi_cell(50, 10, txt="Puedes personalizar el contenido del PDF como desees.", ln=True, align='L')

# Guardar el PDF en un archivo
pdf.output("pdf_final.pdf")
