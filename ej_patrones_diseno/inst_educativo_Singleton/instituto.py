

# Singleton indica que haya una unica instancia de la clase que funcione como un variable global
class InstitutoEducativo:
    _instance = None

    def __init__(self):
        # Simulamos constructor privado lanzando un error si se intenta usar directamente
        raise RuntimeError("Use getInstance() para crear una instancia.")
    # De esta manera no permitimos crear instancias directamente y controlamos la cantidad con la variable _instance


# Gestiona la creacion de la unica instancia (Singleton)
    @classmethod
    def get_instance(cls):
        if cls._instance is None:   # Si no existe la crea
            cls._instance = super().__new__(cls)
        return cls._instance   # Si existe, retorna la instancia ya existente