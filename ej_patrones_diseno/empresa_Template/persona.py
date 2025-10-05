# Esto es para poder implementar metodos abstractos en las clases padre (templates en este caso)
from abc import ABC, abstractmethod   

class Persona():

    # Constructor
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni


    # Definimos el esqueleto algoritmico y luego las subclases implementan los metodos restantes
    # Osea que esta es la clase Template (padre)
    def identificar(self):
        frase = f"Me identifico con: {self.getTipoId}. El numero es: {self.getId}"
        return frase
    
    def getNombre(self):
        return self.__nombre
    

    # Metodos abstractos cuya logica deben implmentarla las subclases
    @abstractmethod
    def getTipoId(self):
        pass

    @abstractmethod
    def getId(self):
        pass