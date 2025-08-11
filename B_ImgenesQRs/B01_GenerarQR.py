""" PAra este ejemplo, se requiere instalar la librería qrcode
pip3 install qrcode[pil] """

import qrcode

def generar_qr(texto, nombre_archivo):
    """Genera un código QR a partir del texto proporcionado y lo guarda en un archivo."""
    # Crear una instancia de QRCode
    qr = qrcode.QRCode(
        version=1,  # Controla el tamaño del QR
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
        box_size=10,  # Tamaño de cada caja del QR
        border=4,  # Ancho del borde
    )
    
    # Agregar el texto al QR
    qr.add_data(texto)
    qr.make(fit=True)  # Ajustar el tamaño del QR

    # Crear una imagen del QR
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen en un archivo
    img.save(nombre_archivo)


# Ejemplo de uso
if __name__ == "__main__":
    texto = "https://www.ejemplo.com"
    nombre_archivo = "codigo_qr.png"
    
    generar_qr(texto, nombre_archivo)
    print(f"Código QR generado y guardado como {nombre_archivo}")
