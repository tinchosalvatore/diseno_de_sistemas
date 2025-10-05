from libro import Libro
from alarmaLibro import AlarmaLibro

class Biblioteca():

    def __init__(self):
        self.alarma = AlarmaLibro()


# Evalua el estado en el que fue devuleto el libro
# si es malo, le pide a SU alarma que notifique a los observadores
    def devuelveLibro(self, libro: Libro):
        print(f"Evento: Se ha devuelto el libro '{libro.titulo}'.")
        if libro.estado.upper() == "MALO":
            # Usamos la instancia de alarma que pertenece a la biblioteca
            self.alarma.notify(libro)
        else:
            print(f"Estado del libro '{libro.titulo}': OK.")