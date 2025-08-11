from fpdf import FPDF

# Crear un objeto PDF, podemos personalizar el tamaño y orientación si es necesario
# ---------------------------------------------------------
# fpdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
# ---------------------------------------------------------
# orientation   'P' es para retrato, 'L' para paisaje
# unit          'mm' es milímetros, 'cm' es centímetros, 'in' es pulgadas, 'pt' es puntos
#               un punto es 1/72 de pulgada equivalent a 0.35 mm
# format        'A4' es un tamaño estándar, también puedes usar 'Letter', 'Legal', 'A3'. 'A5'
#               incluso podemos usar un formato personalizado, digamos (100, 150) <-- Es una tupla 
#               pdf = FPDF('P', 'mm', (100, 150))

pdf = FPDF()

pdf.add_page()

# Set font
# 'I' italicas, 'U' subrayado, 'B' negrita, 'BI' negrita e italicas 
# 'Times' es una fuente predefinida, 'Arial' es otra, 'Courier' es monoespaciada
pdf.set_font('Arial', 'B', 16)


# Move to 8 cm to the right
pdf.cell(80)

# Centered text in a framed 20*10 mm cell and line break

# fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
# Aquí w es el ancho de la celda, h es la altura, txt es el texto a mostrar
# border:       0 sin borde, 1 con borde, 2 con borde doble
# ln            indica donde debe ir la posición del cursor después de la celda
#               0 a la derecha, 1 al inicino de la siguiente línea, 2 abajo
# align         puede ser 'L' para izquierda, 'C' para centro, 'R' 'D' para derecha
# fill          indica si la celda debe ser rellenada (True) o transparente (False)
# link          permite agregar un enlace al texto, si es necesario
pdf.cell(10, 10, 'Title', 1, 1, 'C')

pdf.output('tuto3.pdf', 'F')