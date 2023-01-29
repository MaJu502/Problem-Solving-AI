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

    # ------------------------------------- Pixel -----------------------------------------------
    temp = []
    M = pim.open(imageInput)
    # ahora que esta abierta la imagen se comienza a reducir de tamano y traducir
    M = M.resize((100,100), pim.NEAREST).convert("RGB")
    tempM = M.getdata()
    # se codifican los items del laberinto
    for r,g,b in tempM:
        if 75 <= r <= 255 and 75 <= g <= 255 and 75 <= b <= 255:
            temp.append((255, 255, 255))
        elif r >= 50 and g >= 50:
            temp.append((255,255,255))
        else:
            temp.append((r, g, b))
    M.putdata(temp)
    M.save('PixelInput.bmp')

    
    # ------------------------------------- Array -----------------------------------------------
    # Ahora que la imagen ya esta pixeleada es momento de generar el array.
    retorno = [] # array donde se guardan los items del laberinto
    w,h = M.width, M.height
    rawArray = np.array(M).tolist()
    
    for row in rawArray:
        linea = []
        for pixel in row:
            if pixel == [0,0,0]:
                linea.append(0)
            elif pixel == [255,255,255]:
                linea.append(1)
            elif pixel[0] >= 200:
                linea.append(2)
            elif pixel[1] >= 200:
                linea.append(3)
            else: 
                linea.append(1)
        retorno.append(linea)

    return retorno