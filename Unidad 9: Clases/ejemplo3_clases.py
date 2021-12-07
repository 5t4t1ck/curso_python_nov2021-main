class Pelota():

    def __init__(self,nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

    def __str__(self):
        return f"La pelota que creaste es de {self.nombre}, en la ciudad {self.ciudad}"

pelota1 = Pelota("futbool","Loja")
print(pelota1)

pelota2 = Pelota("baloncesto","Cuenca")
print(pelota2)

pelota3 = Pelota("tenis","Quito")
print(pelota3)