class Auto:

    rueda = 4

    def desplazamiento(self):

        print("El auto se esta desplazando sobre 4 ruedas")

class Moto:

    rueda = 2

    def desplazamiento(self):

        print("La moto se esta desplazando sobre 2 ruedas")

carrito = Auto()
print("El carro tiene: ",carrito.rueda)
carrito.desplazamiento()
print("---------------------------")
motito = Moto()
print("La moto tiene: ",motito.rueda)
motito.desplazamiento()