"""
Universidad del Valle de Guatemala
Inteligencia Artificial 2023
Marco Jurado
created 1/27/2023
"""
from abc import ABC, abstractmethod

class framework(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # defined function action(s) => [a1,a2,a3,a4,...,ax]
    @abstractmethod
    def action(self,s):
        pass

    # defined function results(s,a) => s
    @abstractmethod
    def results(self, s, a):
        """Devuelve Array de nodos visitados en el estado actual"""
        pass

    # defined function goalTest(s) => [True, False]
    @abstractmethod
    def goalTests(self, s):
        pass

    # defined function stepCost(s,a,s) => R
    @abstractmethod
    def stepCost(self, **kargs):
        pass

    # defined function pathCost(s1, s2,...,sn) => R
    @abstractmethod
    def pathCost(self, s):
        pass

