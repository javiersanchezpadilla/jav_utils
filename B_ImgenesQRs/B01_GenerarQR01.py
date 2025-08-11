""" Para este ejemplo, se requiere instalar la librería qrcode
pip3 install qrcode[pil] """

import qrcode

url = "https://www.python.org"

img = qrcode.make(url)
img.save("python_qr.png")

