
class Libro():
    # atributos
    titulo = ""
    estado = ""
# por ser un ejemplo del patron de diseño Observer no ponemos mas atributos
    
# Constructor
    def __init__(self, titulo, estado):
        self.titulo = titulo
        self.estado = estado


# getter and setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo