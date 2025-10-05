from abc import ABC, abstractmethod

class Triangulo(ABC):
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

   
    @abstractmethod
    def getDescripcion(self):
        pass

    @abstractmethod
    def getSuperficie(self):
        pass

    @abstractmethod
    def dibujate(self):
        pass

    # Getters y setters de todos los lados
    def getLadoA(self):
        return self.__ladoA

    def setLadoA(self, ladoA):
        self.__ladoA = ladoA

    def getLadoB(self):
        return self.__ladoB

    def setLadoB(self, ladoB):
        self.__ladoB = ladoB

    def getLadoC(self):
        return self.__ladoC

    def setLadoC(self, ladoC):
        self.__ladoC = ladoC