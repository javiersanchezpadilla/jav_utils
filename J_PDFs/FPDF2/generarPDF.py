""" Tomado del sitio:
    https://www.youtube.com/watch?v=BK35qAVQYSk&t=84s 
    
    Requerimos instalar
    $ pip3 install fpdf pandas
    """
from fpdf import FPDF
from datetime import datetime
import pandas as pd 

# Variable con la ruta del archivo CSV
ruta = "/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/Alumnos.csv"
solo_la_ruta = "/home/javier/Documentos/Programas/Python/jav_utils/J_PDFs/"


# Creamos una clase derivada del FPDF
class PDF(FPDF):
    
    def header(self):
        self.set_font("Arial", "B", 16)     # definimos el tipo de letra

        # Definimos el encabezado ln(nueva linea al final?), align (alineamiento)
        self.cell(0, 10, "Certificado en Python", ln=True, align="C")

        # insertamos diez lineas en blanco
        self.ln(10)

    def footer(self):
        self.set_y(-15) # 15 puntos desde abajo hacia arriba
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Generado el {datetime.now().strftime("%d/%m/%Y")}", align="C")


def genera_certificado(nombre):
    pdf = PDF()             # creamos una instancia de FPDF
    pdf.add_page()          # Agegamos una página
    pdf.set_font("Arial", size=12)

    pdf.ln(30)
    pdf.cell(0, 10, f'Otorgado a: {nombre}', ln=True, align="C")
    pdf.ln(10)

    el_texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
 incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
 ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit \
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"

    pdf.multi_cell(0, 10, el_texto, align="C")
    pdf.ln(20)
    pdf.cell(0, 10, "Firma del instructor", ln=True, align="C")

    # generamos el nombre del archivo
    nombre_archivo = solo_la_ruta
    nombre_archivo = solo_la_ruta + f"certificado_{nombre.replace(' ', '_').lower()}.pdf"

    pdf.output(nombre_archivo)
    print(f"Certificado generado correctamente para {nombre}")


def certificados_csv(ruta_archivo):
    # df = pd.read_csv(ruta_archivo, delimiter=";" )
    # print(df)         # mi error es que estaba usando como separador de campos el (;)
    # print(df.info())  # y no lo estaba indicando (usar delimiter= ";")
    # print(df['Nombre'])
    # print(df.columns)
    try:
        df = pd.read_csv(ruta_archivo, delimiter=";")
        if 'Nombre' not in df.columns:
            print('Tu archivo debe contener una columna llamada: Nombre')
            return
        
        for nombre in df['Nombre']:
            genera_certificado(nombre)
    except FileNotFoundError:
        print(f'El archivo {ruta_archivo} no encontrado')

if __name__ == "__main__":
    certificados_csv(ruta)