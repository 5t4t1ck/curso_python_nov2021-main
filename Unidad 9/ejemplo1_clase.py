class Perro():

    animal = "Mamifero"

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def edad(self, anos):
        self.anos = anos
        if self.anos > 1:
            print("Es adulto")
        else:
            print("Es cahorro")
        
    def comida(self, tipo_comida):
        self.comida = tipo_comida
        print("La comida preferia es ", tipo_comida)

Leo = Perro("Leo", "Mestiza")
print(Leo.nombre)
Leo.edad(0.6)

Tobi = Perro("Tobi", "Mestiza")
print(Tobi.nombre, Tobi.animal)
Tobi.comida("Coquetas")

Rocky = Perro("Rocky", "Salchicha")
print(Rocky.nombre)
Rocky.comida("Croquetas")
Rocky.edad(2)

Tobi.animal
Leo.animal

perro1 = Perro("Bethoven", "salchicha")