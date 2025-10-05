from subject import Subject
from observadores import ObservadorLibroMalEstado
from libro import Libro
from typing import List

class AlarmaLibro(Subject):

    # Inicializamos el "ArrayList" de los observadores
    def __init__(self):
        self._observadores: List[ObservadorLibroMalEstado] = []

# Agregar un observador a la Lista
    def attach(self, observador: ObservadorLibroMalEstado) -> None:
        self._observadores.append(observador)

# Quita a un observador de la lista.
    def detach(self, observador: ObservadorLibroMalEstado) -> None:
        self._observadores.remove(observador)


    def notify(self, libro: Libro) -> None:
        for observador in self._observadores:
            observador.update(libro)