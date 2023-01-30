"""
Image Translator
desc: Takes an array and generates an image. 
auth: Marco Jurado
"""
import numpy as np
from PIL import Image as pim

"""
Toma un arreglo x y comienza a generar la imagen de output
"""
def generateOUT(x,w,h):
    retorno =[]
    for i in x:
        for j in i:
            if j == 1:
                retorno.append((0,0,0))
            elif j == 0:
                retorno.append((255,255,255))
            elif j == 2:
                retorno.append((255,0,0))
            elif j == 3:
                retorno.append((0,255,0))
            elif j == 6:
                retorno.append((180,0,200))
    newM = pim.new("RGB", (w,h))
    newM.putdata(retorno)
    newM.save('out.bmp')
    print(' >> C O M P L E T A D O!')
    print(' >> (busca el archivo con el nombre de out.bmp)')