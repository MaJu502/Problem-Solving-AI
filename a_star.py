"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/27/2023
"""
import numpy as np
from framework import framework
import math

class ASTARM(framework):
    def __init__(self,maze,start,endpoints):
        self.maze, self.start, self.end = maze, start, endpoints
        self.h, self.w = len(maze), len(maze[0])
        self.fronteras = [self.start]
        self.visited = []
        self.path = [] 


    """
    Resuelve el laberinto buscando paths que lleguen a una casilla con el numero
    3 siendo este el numero asignado a la casilla verde en la imagen del 
    laberinto.
    """
    def solve(self):
        try:
            while self.fronteras:
                # mientras existan fronteras
                now = self.fronteras.pop(0) # la ubicacion actual del agente
                self.path.append(now) # se anade la casilla al path
                if self.goalTest(now): # compobar si se ha llegado a una casilla de goal (no. 3)
                    return self.path # path completo
                self.getMoreFontiersNormal(now)
        except Exception as e:
            raise Exception(' >> No se ha logrado encontrar una solucion para el laberinto.')
    

    """
    busca el camino mas corto dentro del laberinto utilizando los caminos y
    backtracing.
    """
    def shortPath(self):
        self.fronteras, self.visited, self.backtracing = [self.start], [self.start], {self.start: None}
        try:
            while self.fronteras:
                # mientras existan fronteras
                self.agentNow = self.fronteras.pop(0) # la ubicacion actual del agente
                if self.goalTest(self.agentNow): # comrpobar si se ha llegado a una casilla de goal (no. 3)
                    self.path = [self.start]
                    while self.agentNow != self.start:
                        self.result(2, self.agentNow)
                    self.path.reverse() # se voltea el arreglo para empezar por el punto de llegada (backtrace)
                    return self.path
                self.getMoreFontiersShort(self.agentNow)
        except Exception as e:
            raise Exception(' >> No se ha logrado encontrar una solucion para el laberinto.')



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
    Realiza el siguiente movimiento en el laberinto para poder ir avanzando
    en las fronteras exploradas. Este metodo funciona para el backtrace dentro
    del laberinto.
    """
    def getMoreFontiersShort(self,s):
        X,Y = s # coordenadas X y Y del punto actual desde el que se buscan nuevas fronteras.
        # frontera arriba (y-1 pues se va a la linea de arriba)
        if Y > 0:
            if self.action(X,Y-1):
                self.result(1,(X,Y-1))
        # frontera abajo (y+1 pues va a la linea de abajo)
        if self.h -1 > Y:
            # mientras la cord en Y sea menor a al ultimo indice de linea en el arreglo
            if self.action(X,Y+1):
                self.result(1,(X,Y+1))
        # frontera izquierda (x-1 pues va a la columna de la izquierda)
        if X > 0:
            if self.action(X-1,Y):
                self.result(1,(X-1,Y))
        # frontera derecha (x+1 pues va a la columna de la derecha)
        if self.w -1 > X:
            if self.action(X+1,Y):
                self.result(1,(X+1,Y))



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
        
class ASTART(framework):
    def __init__(self,maze,start,endpoints):
        self.maze, self.start, self.end = maze, start, endpoints
        self.h, self.w = len(maze), len(maze[0])
        self.fronteras = [self.start]
        self.visited = []
        self.path = []
        


    """
    Resuelve el laberinto buscando paths que lleguen a una casilla con el numero
    3 siendo este el numero asignado a la casilla verde en la imagen del 
    laberinto.
    """
    def solve(self):
        try:
            while self.fronteras:
                # mientras existan fronteras
                now = self.fronteras.pop(0) # la ubicacion actual del agente
                self.path.append(now) # se anade la casilla al path
                if self.goalTest(now): # compobar si se ha llegado a una casilla de goal (no. 3)
                    return self.path # path completo
                self.getMoreFontiersNormal(now)
        except Exception as e:
            raise Exception(' >> No se ha logrado encontrar una solucion para el laberinto.')
    

    """
    busca el camino mas corto dentro del laberinto utilizando los caminos y
    backtracing.
    """
    def shortPath(self):
        self.fronteras, self.visited, self.backtracing = [self.start], [self.start], {self.start: None}
        try:
            while self.fronteras:
                # mientras existan fronteras
                self.agentNow = self.fronteras.pop(0) # la ubicacion actual del agente
                if self.goalTest(self.agentNow): # comrpobar si se ha llegado a una casilla de goal (no. 3)
                    self.path = [self.start]
                    while self.agentNow != self.start:
                        self.result(2, self.agentNow)
                    self.path.reverse() # se voltea el arreglo para empezar por el punto de llegada (backtrace)
                    return self.path
                self.getMoreFontiersShort(self.agentNow)
        except Exception as e:
            raise Exception(' >> No se ha logrado encontrar una solucion para el laberinto.')



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
    Realiza el siguiente movimiento en el laberinto para poder ir avanzando
    en las fronteras exploradas. Este metodo funciona para el backtrace dentro
    del laberinto.
    """
    def getMoreFontiersShort(self,s):
        X,Y = s # coordenadas X y Y del punto actual desde el que se buscan nuevas fronteras.
        # frontera arriba (y-1 pues se va a la linea de arriba)
        if Y > 0:
            if self.action(X,Y-1):
                self.result(1,(X,Y-1))
        # frontera abajo (y+1 pues va a la linea de abajo)
        if self.h -1 > Y:
            # mientras la cord en Y sea menor a al ultimo indice de linea en el arreglo
            if self.action(X,Y+1):
                self.result(1,(X,Y+1))
        # frontera izquierda (x-1 pues va a la columna de la izquierda)
        if X > 0:
            if self.action(X-1,Y):
                self.result(1,(X-1,Y))
        # frontera derecha (x+1 pues va a la columna de la derecha)
        if self.w -1 > X:
            if self.action(X+1,Y):
                self.result(1,(X+1,Y))



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