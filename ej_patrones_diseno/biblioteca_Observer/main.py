# Vamos a crear un libro con estado "MALO", para que salte la notificacion del Observador

from libro import Libro
from alarmaLibro import AlarmaLibro
from observadores import Stock
from observadores import Compras
from observadores import Administracion
from biblioteca import Biblioteca

def main():
	# Creacion de alarma (esta dentro de la biblioteca) y attatch de sus observadores a la alarma que esta puntualmente
	# dentro de la biblioteca
	b = Biblioteca()
	b.alarma.attach(Stock())
	b.alarma.attach(Compras())
	b.alarma.attach(Administracion())

	libro = Libro("El Principito", "MALO")


	b.devuelveLibro(libro)    # Alguien devuelve el libro principito en mal estado


if __name__ == '__main__':
    main()
