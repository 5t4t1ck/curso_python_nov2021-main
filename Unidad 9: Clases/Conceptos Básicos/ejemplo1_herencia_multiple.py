class Padre():
    def cocinar(self):
        print("El padre cocina para su familia")

class Madre():
    def conducir(self):
        print("La madre conduce a la escuela")

class Hijo(Padre, Madre):
    def querer(self):
        print("Ama a sus padres")

class Hija(Padre, Madre):
    def llorar(self):
        print("llorar")
    
c=Hijo()
c.conducir()
c.cocinar()
c.querer()

print("-------------")
e=Hija()
e.cocinar()
e.conducir()
e.llorar()



