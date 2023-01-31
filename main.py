"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/24/2023
"""
import framework
from bfs import *
from dfs import *
from a_star import *
from imageTranslator import *
from imageOutGenerator import *
from getSartFinish import *
#import numpy as np
imagen = ''
print("""
    Que imagen deseas resolver:
        1. normal
        2. turing
""")
inputIM = input(' > ingresa la opcion que deseas: ')
if inputIM == '1':
    imagen = '.\mazeInputs\Input.bmp'
elif inputIM == '2': 
    imagen = '.\mazeInputs\Turing.png'

size = 0
print("""
    Que resolucion deseas para la digitalizacion de la imagen?:
        1. normal
        2. avanzado (recomendado para turing)
""")
inputsz = input(' > ingresa la opcion que deseas: ')
if inputsz == '1':
    size = 100
elif inputsz == '2': 
    size = 500

mazeArray = TranslateImage(size,size,imagen) # array de elementos del laberinto
startPoint = getStart(mazeArray) # coordenadas del punto de inicio (1)
endPoint = getEnd(mazeArray) #coordenadas de los puntos de llegada o goal. (varios puntos)
path = []

print("""
    Que algoritmo deseas para resolver el laberinto?
        1. BFS
        2. DFS
        3. A* (Manhattan heuristic)
        4. A* (Manhattan heuristic)
""")
algor = input(' > ingresa la opcion que deseas: ')
print(' >> P R O C E S A N D O ...')
if algor == '1':
    # bfs
    bfSearch = BFS(maze=mazeArray, start=startPoint, endpoints=endPoint)
    path = bfSearch.shortPath()
elif algor == '2':
    # dfs
    dfSearch = DFS(maze=mazeArray, start=startPoint, endpoints=endPoint)
    path = dfSearch.shortPath()


elif algor == '2' and inputIM == '2':
    # bfs turing
    dfSearch = DFS(maze=mazeArray, start=startPoint, endpoints=endPoint)
    path = dfSearch.path
elif algor == '1' and inputIM == '2':
    # bfs turing
    dfSearch = DFS(maze=mazeArray, start=startPoint, endpoints=endPoint)
    path = dfSearch.path


elif algor == '3':
    # a*
    ASMSearch = ASTARM(maze=mazeArray, start=startPoint, endpoints=endPoint)
    path = ASMSearch.graphSearch()
elif algor == '4':
    # a*
    ASESearch = ASTARE(maze=mazeArray, start=startPoint, endpoints=endPoint)
    path = ASESearch.graphSearch()




for i in path:
    mazeArray[i[0]][i[1]] = 6

generateOUT(mazeArray,size,size)