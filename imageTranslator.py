"""
Image Translator
desc: Takes a bmp image loaded to the program and generates a maze that the 
AI can work with. 
auth: Marco Jurado
"""
import numpy as np
from PIL import Image as pim

#constants
cellSize = 10 # size given to the cells created in the maze
imageInput = '.\mazeInputs\Input.bmp' #image given by user
imageOut = 'solvedMaze.bmp' #image given to the user with solution marked

"""
Toma una imagen y la comienza a traducir para generar el array
"""
def TranslateImage():
    retorno = []
    M = pim.open(imageInput)
    # ahora que esta abierta la imagen se comienza a reducir de tamano y traducir
    M = M.resize((100,100), pim.NEAREST).convert("RGB")
    tempM = M.getdata()

    # se codifican los items del laberinto
    for r,g,b in tempM:
        if 75 <= r <= 255 and 75 <= g <= 255 and 75 <= b <= 255:
            retorno.append((255, 255, 255))
        elif r >= 50 and g >= 50:
            retorno.append((255,255,255))
        else:
            retorno.append((r, g, b))
    
    M.putdata(retorno)
    M.save('PixelInput.bmp')

    #return (TransformToWeights(np.array(M)))

"""
Toma un arreglo x y lo traduce de un arreglo generado con numpy 
a un arreglo donde tiene los valores definidos para el laberinto
siendo estos: 
    0 - blanco
    1- negro
    2 - inicio
    3 - final
"""
def TransformToWeights(x):
    x[np.isin(x, [0,1,2,3])] = 0
    return x.tolist()