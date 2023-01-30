"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/24/2023
"""
import framework
from bfs import *
"""from dfs import *
from a_star import *"""
from imageTranslator import *
from imageOutGenerator import *
from getSartFinish import *
#import numpy as np

imagen = '.\mazeInputs\Input.bmp'
size = 200

mazeArray = TranslateImage(size,size,imagen) # array de elementos del laberinto
startPoint = getStart(mazeArray) # coordenadas del punto de inicio (1)
endPoint = getEnd(mazeArray) #coordenadas de los puntos de llegada o goal. (varios puntos)

bfSearch = BFS(maze=mazeArray, start=startPoint, endpoints=endPoint)
path = bfSearch.shortPath()

for i in path:
    mazeArray[i[0]][i[1]] = 6

generateOUT(mazeArray,size,size)


