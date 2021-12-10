# Calcular el perimetro y area de un circulo dado su radio
PI = 3.141592
def perimetro(radio):
    return 2*PI*radio


def area (radio):

    return PI*radio**2

r = int(input("Ingrese el radio: "))
print ("El perimetro es: ",perimetro(r))
print ("El area es: ",area(r))

