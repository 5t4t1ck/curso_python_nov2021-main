class cuadrilatero():
    def __init__(self,lados):
        self.lados = lados
        self.suma_angulos = 360

    def perimetro(self):
        return sum(self.lados)

class cuadrado(cuadrilatero):
    def __init__(self,lados):
        super().__init__(lados)

cuadrado_1 = cuadrado([4,4,4,4])
perimetro_1 = cuadrado_1.perimetro()

print(cuadrado_1.lados)
print(perimetro_1)