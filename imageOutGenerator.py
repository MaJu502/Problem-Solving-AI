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
def generateOUT(x):
    pim.fromarray(Conversion(np.array(x)), 'RGB').save('solvedMaze.bmp')

"""
Toma un arreglo x y comienza a generar la imagen de output
"""
def Conversion(x):
    mapeo = {1: [255, 255, 255], 0: [0, 0, 0], 2: [0, 255, 0], 3: [255, 0, 0]}

    retorno = np.vectorize(mapeo.get)(x)
    return retorno