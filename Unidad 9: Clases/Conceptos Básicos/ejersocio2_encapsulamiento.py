"""
Crear una clase Triangulo, implementando método 
para acceder al radio del mismo y 
otro para modificarlo.
"""

class Triangulo:

    def __init__(self, base, altura):
        self.__base = base
        self.altura = altura

    def area(self):
        return self.__base * self.altura

    def valorBase(self):
        return self.__base

    def fijarBase(self, nuevaBase):
        self.__base = nuevaBase

p = Triangulo(2,4)
print(p.area())
print(p.valorBase())
print("------------------")
p.fijarBase(4)
print(p.area())
print("------------------")
