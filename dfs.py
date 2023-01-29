"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/27/2023
"""
from framework import framework

class dfs(framework):
    def __init__(self,maze):
        self.maze = maze # array with maze info
        self.start = self.getStart(self,maze) 
        self.goal = self.getGoals(self,maze)



    """
    Algoritmo para encontrar el punto inicial en el arreglo
    recorriendo con for buscando el numero correspondiente
    """
    def getStart(self,m):
        for line in m:
            # cada linea 
            for i in line:
                # cada numero
                if i == 2:
                    return (m.index(line), line.index(i)) # retorna la ubicacion en el array del start
                

    """
    Algoritmo para encontrar los puntos de goal en el arreglo
    recorriendo con for buscando el numero correspondiente
    """
    def getGoals(self,m):
        retorno = []
        for line in m:
            # cada linea 
            for i in line:
                # cada numero
                if i == 3:
                    retorno.append(m.index(line), line.index(i)) # retorna la ubicacion en el array de los goals
        return retorno

    """
    mueve al agente a todas las branches posibles
    """
    def searching(self,maze):

        pass

    """\watch
    algoritmo depth fist
    recibe el arreglo del laberinto (maze) y la posicion actual 
    del agente en conjunto con los ultimos espacios visitados asi 
    como los espacios a los cuales se puede mover (frontera).
    """
    def DepthFirstSearch(self, maze, pI, last, frontier):
        last.append(pI) 



        # actions for up, down, left, right movements
        tempX