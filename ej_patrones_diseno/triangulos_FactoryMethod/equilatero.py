from triangulo import Triangulo

# tres lados iguales
class Equilatero(Triangulo):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)

    def getDescripcion(self):
        return "Soy un Triangulo Equilatero"

    def getSuperficie(self):
        return 0.0  # Placeholder

    def dibujate(self):
        print("Dibujando triángulo equilátero...")  # Placeholder