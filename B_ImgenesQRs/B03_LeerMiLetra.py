""" Para este ejercicio se requiere instalar
    sudo apt install tesseract-ocr  <-- Permite leer OCR
    pip3 install pytesseract        <-- P ermite usar tesseract desde Python  
    pip3 install Pillow             <-- Permite manejar imágenes desde Python

"""

import pytesseract
from PIL import Image

# Abrimos la imagen, usamos Image.open y le pasamos la ruta de la imagen donde
# se escribió a mano el texto
imagen = Image.open("B_ImgenesQRs/mi_letra.png")

# Usamos pytesseract.image_to_string  <-- para extraer el texto de la imagen
# podemos usar "spa"nish" para español o "eng" para inglés
texto = pytesseract.image_to_string(imagen, lang="spa")
print ("El texto leído de la imagen es:")
print(texto)


# Si queremos guardar el texto en un archivo de texto
# with open("B_ImgenesQRs/texto_leido.txt", "w") as archivo:
#     archivo.write(texto)
# print("El texto se ha guardado en B_ImgenesQRs/texto_leido.txt")