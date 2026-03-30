""" Crear reporte PDF

    2. Crear Reportes desde cero (fpdf2)
    ------------------------------------
    Para generar una factura o un reporte con tus datos, fpdf2 es la opción 
    más amigable. Es como tener una hoja de papel en blanco y decirle a 
    Python: "Escribe esto aquí, baja 10 cm, pon una imagen allá".

    Instalación: 

            pip3 install fpdf2

    Ejemplo: Crear un reporte sencillo
"""
from fpdf import FPDF

# 1. Creamos el objeto del PDF
pdf = FPDF()
pdf.add_page()

# 2. Configuramos la fuente (Tipo, Estilo, Tamaño)
pdf.set_font("Arial", "B", 16)

# 3. Escribimos un título (Celda)
pdf.cell(40, 10, "Reporte de Ventas - Marzo 2026")

# 4. Bajamos de línea y escribimos texto normal
pdf.ln(20) # Salto de línea de 20 unidades
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Este es un reporte generado automáticamente con Python y la librería FPDF2.")

# 5. Guardar el archivo
pdf.output("mi_reporte.pdf")

print("¡Reporte creado!")
