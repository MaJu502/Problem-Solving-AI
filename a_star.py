"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/27/2023
"""
import numpy as np
from framework import framework

class ASTARM(framework):
    def __init__(self,maze,start,endpoints):
        self.maze, self.start, self.end = maze, start, endpoints
        self.h, self.w = len(maze), len(maze[0])
        self.fronteras = []
        self.visited = []
        self.path = [] 


    """
    Resuelve el laberinto buscando paths que lleguen a una casilla con el numero
    3 siendo este el numero asignado a la casilla verde en la imagen del 
    laberinto.
    """
    def graphSearch(self):
        # se calcula la F (heuristica) del start point
        startX,startY = self.start
        self.fronteras = [(startX,startY, self.manhat(self.start))]

        while self.fronteras:
            # mientras existan fronteras

            temp = 0
            lowestF = min(self.fronteras, key=lambda x: x[2]) # la cord que tiene la heuristica más baja de todos. 

            for i, item in enumerate(self.fronteras):
                if item == lowestF:
                    temp = i

            now = self.fronteras.pop(temp) # la ubicacion actual del agente
            self.path.append((now[0],now[1]))
            
            self.nowFronteras = [] # reset a vecinos
            laX,laY,laF = now
            self.getFronterasREMIX((laX,laY)) # fronteras

            for vecino in self.nowFronteras:
                X,Y = vecino
                if self.goalTest((X,Y)):
                    self.path.append((X,Y))
                    return self.path
                    
                tempF = self.manhat((X,Y))
                self.fronteras.append((X,Y,tempF))
        return self.path

    
    """
    Toma las cordenadas de las posiciones del punto de llegada y el punto actual 
    del agente para determinar la distancia de la heuristica de manhattan. 
    https://www.101computing.net/manhattan-distance-calculator/
    maze => laberinto array
    s =>  punto actual en el mapa del agente.
    """
    def manhat(self, s):
        xG,yG = self.end[0]
        xA,yA = s

        x = xA - xG
        y = yG - yA

        return ((x + y) - 1 * min(x,y) + 1)


    """
    Comprueba si la posicion es goal
    """
    def goalTest(self, s):
        if s in self.end:
            return True
        else: 
            False
    
    """
    Realiza el siguiente movimiento en el laberinto para poder ir avanzando
    en las fronteras exploradas. Esto al mismo tiempo anade nuevas casillas
    en la lista de fronteras del agente. Normal = no backtracing.
    """
    def getMoreFontiersNormal(self,x):
        X,Y = x # coordenadas X y Y del punto actual desde el que se buscan nuevas fronteras.a
        # frontera arriba (y-1 pues se va a la linea de arriba)
        if Y > 0:
            if self.action(X,Y-1):
                self.result(0,(X,Y-1))
        # frontera abajo (y+1 pues va a la linea de abajo)
        if self.h -1 > Y:
            # mientras la cord en Y sea menor a al ultimo indice de linea en el arreglo
            if self.action(X,Y+1):
                self.result(0,(X,Y+1))
        # frontera izquierda (x-1 pues va a la columna de la izquierda)
        if X > 0:
            if self.action(X-1,Y):
                self.result(0,(X-1,Y))
        # frontera derecha (x+1 pues va a la columna de la derecha)
        if self.w -1 > X:
            if self.action(X+1,Y):
                self.result(0,(X+1,Y))

    """
    Fronteras de la posicion actual. 
    """
    def getFronterasREMIX(self,x):
        retorno = []
        X,Y = x # coordenadas X y Y del punto actual desde el que se buscan nuevas fronteras.a
        # frontera arriba (y-1 pues se va a la linea de arriba)

        if Y > 0:
            if self.action(X,Y-1):
                self.result(3,(X,Y-1))
        # frontera abajo (y+1 pues va a la linea de abajo)
        if self.h -1 > Y:
            # mientras la cord en Y sea menor a al ultimo indice de linea en el arreglo
            if self.action(X,Y+1):
                self.result(3,(X,Y+1))
        # frontera izquierda (x-1 pues va a la columna de la izquierda)
        if X > 0:
            if self.action(X-1,Y):
                self.result(3,(X-1,Y))
        # frontera derecha (x+1 pues va a la columna de la derecha)
        if self.w -1 > X:
            if self.action(X+1,Y):
                self.result(3,(X+1,Y))
        
    

    """
    se mueve a las cordenadas que queremos evaluar y devuelve True si dicha 
    casilla no es pared.
    """
    def action(self, x, y):
        if self.maze[x][y] == 1:
            return False
        else: return True

    """
    verifica el resultado del movimiento.
    type(s) son:
        - 0 ==> default
        - 1 ==> for backtrace
        - 2 ==> backtraced
    """
    def result(self, typ, s):
        if typ == 2:
            self.path.append(s)
            self.agentNow = self.backtracing[s]
        elif typ == 3:
            if self.checkNotVisited(s):
                self.visited.append(s)
                self.nowFronteras.append(s)
        else:
            if self.checkNotVisited(s):
                self.visited.append(s)
                self.fronteras.append(s)
                if typ == 1:
                    self.backtracing[s] = self.agentNow
    
    """
    Verifica si el estado ya fue visitado
    """
    def checkNotVisited(self,s):
        if s in self.visited:
            return False # ya fue visitado
        else:
            return True # no ha sido visitado, es posible utilizarlo para encontrar fronteras.
    
    def stepCost(self, **kargs):
        pass
    
    def pathCost(self, s):
        return len(s)-1


class ASTARE(framework):
    def __init__(self,maze,start,endpoints):
        self.maze, self.start, self.end = maze, start, endpoints
        self.h, self.w = len(maze), len(maze[0])
        self.fronteras = []
        self.visited = []
        self.path = [] 


    """
    Resuelve el laberinto buscando paths que lleguen a una casilla con el numero
    3 siendo este el numero asignado a la casilla verde en la imagen del 
    laberinto.
    """
    def graphSearch(self):
        # se calcula la F (heuristica) del start point
        startX,startY = self.start
        self.fronteras = [(startX,startY, self.euclid(self.start))]

        while self.fronteras:
            # mientras existan fronteras

            temp = 0
            lowestF = min(self.fronteras, key=lambda x: x[2]) # la cord que tiene la heuristica más baja de todos. 

            for i, item in enumerate(self.fronteras):
                if item == lowestF:
                    temp = i

            now = self.fronteras.pop(temp) # la ubicacion actual del agente
            self.path.append((now[0],now[1]))
            
            self.nowFronteras = [] # reset a vecinos
            laX,laY,laF = now
            self.getFronterasREMIX((laX,laY)) # fronteras

            for vecino in self.nowFronteras:
                X,Y = vecino
                if self.goalTest((X,Y)):
                    self.path.append((X,Y))
                    return self.path
                    
                tempF = self.euclid((X,Y))
                self.fronteras.append((X,Y,tempF))
        return self.path

    
    """
    Toma las cordenadas de las posiciones del punto de llegada y el punto actual 
    del agente para determinar la distancia de la heuristica de euclid.
    https://github.com/brean/python-pathfinding/blob/main/pathfinding/core/heuristic.py
    maze => laberinto array
    s =>  punto actual en el mapa del agente.
    """
    def euclid(self, s):
        xG,yG = self.end[0]
        xA,yA = s

        x = xA - xG
        y = yG - yA

        return int(np.sqrt(x**2 + y**2)) + 1


    """
    Comprueba si la posicion es goal
    """
    def goalTest(self, s):
        if s in self.end:
            return True
        else: 
            False
    
    """
    Realiza el siguiente movimiento en el laberinto para poder ir avanzando
    en las fronteras exploradas. Esto al mismo tiempo anade nuevas casillas
    en la lista de fronteras del agente. Normal = no backtracing.
    """
    def getMoreFontiersNormal(self,x):
        X,Y = x # coordenadas X y Y del punto actual desde el que se buscan nuevas fronteras.a
        # frontera arriba (y-1 pues se va a la linea de arriba)
        if Y > 0:
            if self.action(X,Y-1):
                self.result(0,(X,Y-1))
        # frontera abajo (y+1 pues va a la linea de abajo)
        if self.h -1 > Y:
            # mientras la cord en Y sea menor a al ultimo indice de linea en el arreglo
            if self.action(X,Y+1):
                self.result(0,(X,Y+1))
        # frontera izquierda (x-1 pues va a la columna de la izquierda)
        if X > 0:
            if self.action(X-1,Y):
                self.result(0,(X-1,Y))
        # frontera derecha (x+1 pues va a la columna de la derecha)
        if self.w -1 > X:
            if self.action(X+1,Y):
                self.result(0,(X+1,Y))

    """
    Fronteras de la posicion actual. 
    """
    def getFronterasREMIX(self,x):
        retorno = []
        X,Y = x # coordenadas X y Y del punto actual desde el que se buscan nuevas fronteras.a
        # frontera arriba (y-1 pues se va a la linea de arriba)

        if Y > 0:
            if self.action(X,Y-1):
                self.result(3,(X,Y-1))
        # frontera abajo (y+1 pues va a la linea de abajo)
        if self.h -1 > Y:
            # mientras la cord en Y sea menor a al ultimo indice de linea en el arreglo
            if self.action(X,Y+1):
                self.result(3,(X,Y+1))
        # frontera izquierda (x-1 pues va a la columna de la izquierda)
        if X > 0:
            if self.action(X-1,Y):
                self.result(3,(X-1,Y))
        # frontera derecha (x+1 pues va a la columna de la derecha)
        if self.w -1 > X:
            if self.action(X+1,Y):
                self.result(3,(X+1,Y))
        
    

    """
    se mueve a las cordenadas que queremos evaluar y devuelve True si dicha 
    casilla no es pared.
    """
    def action(self, x, y):
        if self.maze[x][y] == 1:
            return False
        else: return True

    """
    verifica el resultado del movimiento.
    type(s) son:
        - 0 ==> default
        - 1 ==> for backtrace
        - 2 ==> backtraced
    """
    def result(self, typ, s):
        if typ == 2:
            self.path.append(s)
            self.agentNow = self.backtracing[s]
        elif typ == 3:
            if self.checkNotVisited(s):
                self.visited.append(s)
                self.nowFronteras.append(s)
        else:
            if self.checkNotVisited(s):
                self.visited.append(s)
                self.fronteras.append(s)
                if typ == 1:
                    self.backtracing[s] = self.agentNow
    
    """
    Verifica si el estado ya fue visitado
    """
    def checkNotVisited(self,s):
        if s in self.visited:
            return False # ya fue visitado
        else:
            return True # no ha sido visitado, es posible utilizarlo para encontrar fronteras.
    
    def stepCost(self, **kargs):
        pass
    
    def pathCost(self, s):
        return len(s)-1