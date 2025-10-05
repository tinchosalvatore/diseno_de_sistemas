from cliente import Cliente
from empleado import Empleado
from socio import Socio

def main():
    cliente = Cliente("Juan", "12345678", 1)
    empleado = Empleado("Pedro", "87654321", "AD 41252") 
    socio = Socio("Maria", "23456789", 3)

    print("El cliente dice: ")
    print(cliente.identificar())

    print("El empleado dice: ")
    print(empleado.identificar())

    print("El socio dice: ")
    print(socio.identificar())

if __name__ == '__main__':
    main()