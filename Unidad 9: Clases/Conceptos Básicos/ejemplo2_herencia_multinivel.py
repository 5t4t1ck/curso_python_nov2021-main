"""
Crear 3 Clases para la explicación de la herencia multiple y multinivel
"""

class Abuelo_perrito():

    def __str__(self):
        return "puedo ladrar"
    

class Padre_perrito(Abuelo_perrito):

    def __str__(self):
        return Abuelo_perrito.__str__(self)

    def comer(self):
        print("puedo comer")

class Perro1(Padre_perrito):

    def __str__(self):
        return Padre_perrito.__str__(self)

    def jugar(self):
        print("puedo jugar")

class Perro2(Padre_perrito):

    def __str__(self):
        return Padre_perrito.__str__(self)

    def morder(self):
        print("puedo morder")

Wolf = Perro1()
Wolf.comer()
Wolf.jugar()
print(Wolf.__str__())

print("---")
Worlf1 = Perro2()
Worlf1.comer()
Worlf1.morder()
print(Wolf.__str__())