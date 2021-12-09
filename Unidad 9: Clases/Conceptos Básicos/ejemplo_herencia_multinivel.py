### herencia múltiple ###

class Abuelo():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "Esta clase es: {}".format(self.nombre)

class Padre(Abuelo):

    def __init__(self,nombre, apellido, edad):
        #self.nombre = nombre
        #self.apellido = apellido
        Abuelo.__init__(self,nombre, apellido)
        self.edad = edad

    def __str__(self):
        return Abuelo.__str__(self)

class Nieta(Padre):

    def __init__(self, nombre, apellido, edad, ano_nacimiento):
        #self.nombre = nombre
        #self.apellido = apellido
        #self.edad = edad
        super().__init__(nombre, apellido, edad)
        self.año_nacimiento = ano_nacimiento

    def __str__(self):
        """ Utilizo esta clase para mostrar el tipo de herencia"""
        return super().__str__()

usuario1 = Abuelo("Jose","Jaramillo")
#print(dir(usuario1))
usuario2 = Padre("Juan", "Martinez", 40)
#print(dir(usuario2))
usuario3 = Nieta("Luisa", "Martinez", 20, 2002)
#print(dir(usuario3))