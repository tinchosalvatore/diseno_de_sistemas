from abc import ABC, abstractmethod
from observadores import ObservadorLibroMalEstado

#  La interfaz del Sujeto define los métodos para gestionar observadores. 
class Subject(ABC):

    @abstractmethod
    def attach(self, observador: ObservadorLibroMalEstado) -> None:
        """Agrega un observador para que sea notificado."""
        pass

    @abstractmethod
    def detach(self, observador: ObservadorLibroMalEstado) -> None:
        """Quita a un observador de la lista de notificaciones."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notifica a todos los observadores suscritos."""
        pass