# Construir una clase carro e instanciar 2 objetos

class Carro():

    llantas = 5
    
    def __init__(self, tamano, marca, peso, placa):
        self.tamano = tamano
        self.marca = marca
        self.peso = peso
        self.placa = placa

    def acelerar(self):
        print("Estoy acelerando...")

    def frenar(self):
        print("Estoy frenando, casi me choco")


suzuki = Carro("1.5 m","susuki","1 tonelada", "GVY-570")
corsa = Carro("1.5 m","corsa","1 tonelada", "LGB-134")

suzuki.acelerar()
suzuki.acelerar()
suzuki.acelerar()
suzuki.frenar()

corsa.acelerar()
corsa.frenar()
