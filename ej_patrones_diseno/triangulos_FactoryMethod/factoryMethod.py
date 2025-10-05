from abc import ABC, abstractmethod

class TrianguloFactoryMethod(ABC):
    @abstractmethod
    def createTriangulo(self, ladoA, ladoB, ladoC):
        pass