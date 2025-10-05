from persona import Persona

# Socio se identifica con un numero de socio
class Socio(Persona):
    def __init__(self, nombre, dni, numero_de_socio):
        super().__init__(nombre, dni)
        self.__numero_de_socio = numero_de_socio

    # Implementación del método abstracto
    def getIdentificacion(self):
        return str(self.__numero_de_socio)

    # Implementación del método abstracto
    def getTipoId(self):
        return "numero de socio"

    # Getter y setter (opcional, pero lo incluimos por consistencia)
    def getNumeroDeSocio(self):
        return self.__numero_de_socio

    def setNumeroDeSocio(self, numero_de_socio):
        self.__numero_de_socio = numero_de_socio