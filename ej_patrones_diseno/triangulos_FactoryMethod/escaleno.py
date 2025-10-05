from triangulo import Triangulo

class Escaleno(Triangulo):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)

    def getDescripcion(self):
        return "Soy un Triangulo Escaleno"

    def getSuperficie(self):
        return 0.0

    def dibujate(self):
        print("Dibujando triángulo escaleno...")