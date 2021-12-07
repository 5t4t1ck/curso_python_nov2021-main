# Crear una clase Mounstro e instanciar un objeto Mounstro.

class Monster():

    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def saludar(self):
        print("Hey soy un ",self.nombre)

mounstrito = Monster("Sullivan","Asustador")
mainc = Monster("Maik Whasowsky", "Ayudante")

mounstrito.saludar()
mainc.saludar()