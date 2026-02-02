""" PRograma que aplique un filtro de dibujo animado a la camara

    Para poder usarlo instalar
        $ pip install opencv-python

    Para poder comprobar que está correctamente instalada pordemo ejecutar
    dentro de un programa

        print(cv2.__version__)
"""

import cv2 
import numpy as np 

# print(cv2.__version__)
def cartoon_filter(img):
    img_color = cv2.bilateralFilter(img, d=9, sigmaColor=300,
                                    sigmaSpace=300)
    img_gra = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, blockSize=9, C=2)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    output_frame = cartoon_filter(frame)

    cv2.imshow('Filtro de dibujo animado, output_frame')




