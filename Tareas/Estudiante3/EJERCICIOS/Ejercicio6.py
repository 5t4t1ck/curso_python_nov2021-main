"""
Calcular el area y el perimetro de un rentagulo para ello debemos crear
las siguientes variables
alto(int)
ancho(int)
"""
alto = float(input("Ingrese el alto del retangulo   : "))
ancho = float(input("Ingrese el ancho del rectangulo: "))

area = alto * ancho
perimetro = 2*alto + 2*ancho

print ("El area del rectangulo es     : ",area)
print ("El perimetro del rectangulo es: ",perimetro)


