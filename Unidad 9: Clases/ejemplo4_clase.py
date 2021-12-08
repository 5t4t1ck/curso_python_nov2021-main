class Usuario():

    def __init__(self, nombre, apellido, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña

    def saludar(self):
        print("Hola, mi nombre es {} {}, mi contraseña es: {}".format(self.nombre, self.apellido,self.contraseña))

usuario = Usuario("Diego", "Saavedra", None)
usuario.saludar()

usuario1 = Usuario("Felipe", "García", None)
usuario1.saludar()
