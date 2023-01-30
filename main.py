"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/24/2023
"""
import framework
"""from dfs import *
from bfs import *
from a_star import *"""
from imageTranslator import *
from getSartFinish import *
#import numpy as np

mazeArray = TranslateImage() # array de elementos del laberinto
startPoint = getStart(mazeArray) # coordenadas del punto de inicio (1)
endPoint = getEnd(mazeArray) #coordenadas de los puntos de llegada o goal. (varios puntos)