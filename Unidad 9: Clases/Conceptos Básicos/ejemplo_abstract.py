
from abc import ABCMeta, abstractmethod
import math 

class Figura(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(Figura):

    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        return self.ancho * self.altura

    def perimetro(self):
        return 2 * (self.ancho * self.altura)

class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

#Pruebas

r = Rectangulo(3, 5)
print("El área del rectangulo es:",r.area())
print("El perimetro del rectangulo es:",r.perimetro())

print("-------------------------------------------")

c = Circulo(5.0)
print("El área del círculo es:", c.area())
print("El perimetro del rectangulo es:",c.perimetro())

#f = Figura()
