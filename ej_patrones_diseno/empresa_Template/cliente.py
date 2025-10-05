from persona import Persona

# Cliente se identifica con un numero de cliente
class Cliente (Persona):  
    def __init__(self, nombre, dni, numero_de_cliente):
        super().__init__(nombre, dni) # heredamos de persona, super() llama al constructor de la clase Padre (Persona)
        self.__numero_de_cliente = numero_de_cliente

    def getId(self):  # lo devolvemos como string porque asi lo hizo la profesora en su ejerciico en Java
        return str(self.__numero_de_cliente)  
    
    def getTipoId(self):
        return "numero de cliente"
    
    def getNumeroDeCliente(self):
        return self.__numero_de_cliente
    
    def setNumeroDeCliente(self, numero_de_cliente):
        self.__numero_de_cliente = numero_de_cliente