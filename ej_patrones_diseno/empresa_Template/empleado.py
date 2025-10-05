from persona import Persona

# Empleado se identifica con un legajo
class Empleado(Persona):
    def __init__(self, nombre, dni, legajo):
        super().__init__(nombre, dni)
        self.__legajo = legajo

    # Métodos abstractos
    def getIdentificacion(self):
        return self.__legajo

    def getTipoId(self):
        return "numero de legajo"

    # Getters y setters 
    def getLegajo(self):
        return self.__legajo

    def setLegajo(self, legajo):
        self.__legajo = legajo