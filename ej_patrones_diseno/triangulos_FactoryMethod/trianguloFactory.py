from factoryMethod import TrianguloFactoryMethod
from equilatero import Equilatero
from escaleno import Escaleno
from isosceles import Isosceles


# Clase Factory, da las opciones variadas para los tres tipos de Triángulos
class TrianguloFactory(TrianguloFactoryMethod):

    # Este es el metodo abstracto para crear triangulos, a eleccion de la subclase que llama al metodo
    def createTriangulo(self, ladoA, ladoB, ladoC):
        if ladoA == ladoB == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)