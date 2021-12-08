class Padre():
    def __init__(self,nombre):
        self.nombre = nombre
        
    def nombre(self):
        return f"El nombre {self.nombre}"

class Hija(Padre):
    def __init__(self,nombre):
        super().__init__(nombre)

Juan = Hija("Juan")
print(Juan.nombre)

Pedro = Hija("Pedro")
print(Pedro.nombre)