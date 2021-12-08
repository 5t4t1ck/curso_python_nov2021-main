# https://docs.hektorprofe.net/python/herencia-en-la-poo/ejercicios/

class Vehiculo():
    
    def __init__(self, color, ruedas, matricula, creacion, dueño):
        self.color = color
        self.ruedas = ruedas
        self.matricula = matricula
        self.creacion = creacion
        self.dueño = dueño

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)
print(c)
