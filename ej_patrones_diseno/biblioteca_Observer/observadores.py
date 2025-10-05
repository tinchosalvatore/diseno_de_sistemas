from abc import ABC, abstractmethod
from libro import Libro 

# --- Observadores Abstractos ---
class ObservadorLibroMalEstado(ABC):
    @abstractmethod
    def update(self, libro: Libro):
        pass

# --- Observadores Concretos ---
class Administracion(ObservadorLibroMalEstado):
    def update(self, libro: Libro):
        print("Administración: Envío una queja formal...")

class Compras(ObservadorLibroMalEstado):
    def update(self, libro: Libro):
        print(f"Compras: Solicito nueva cotización para '{libro.titulo}'...")

class Stock(ObservadorLibroMalEstado):
    def update(self, libro: Libro):
        print(f"Stock: Doy de baja a '{libro.titulo}' del inventario...")