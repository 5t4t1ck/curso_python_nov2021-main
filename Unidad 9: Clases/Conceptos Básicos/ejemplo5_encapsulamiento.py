"""
Los métodos que permiten acceder al valor de un atributo 
se denominan "getters" (del verbo inglés "get", obtener) 
y los que fijan el valor de un atributo se denominan 
"setters" (del verbo inglés "set", fijar).

Crear una clase Círculo, implementando un método para 
acceder al radio del mismo y otro para modificarlo.
"""

class Circulo:
    
    __pi = 3.141592
    
    def __init__(self, radio):
        self.__radio = radio
    
    def __cuadrado(self, n):
        return n ** 2
    
    def area(self):
        return Circulo.__pi * self.__cuadrado(self.__radio)
    
    def valorRadio(self):
        return self.__radio
    
    def fijaRadio(self, nuevoRadio):
        self.__radio = nuevoRadio

c = Circulo(3)
print(c.area())
print("-------------------")

c.fijaRadio(4)
print(c.valorRadio())
print(c.area())
print("-------------------")