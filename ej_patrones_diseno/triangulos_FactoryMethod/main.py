from trianguloFactory import TrianguloFactory


def main():
    factory = TrianguloFactory()

    triangulo1 = factory.createTriangulo(10, 10, 10)   # Equilátero
    triangulo2 = factory.createTriangulo(3, 4, 5)      # Escaleno
    triangulo3 = factory.createTriangulo(5, 5, 8)      # Isósceles
    
    
    for triangulo in [triangulo1, triangulo2, triangulo3]:    
        print(triangulo.getDescripcion())
        

if __name__ == '__main__':
    main()