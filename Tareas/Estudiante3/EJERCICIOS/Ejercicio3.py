# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos

def suma(a,b):
    print ("La suma de {x} + {y} es : {z}".format(x=a,y=b,z=a+b))


def resta(a,b):
     print ("La resta de {x} - {y} es : {z}".format(x=a,y=b,z=a-b))


def multiplicacion(a,b):
     print ("La multiplicacion de {x} * {y} es : {z}".format(x=a,y=b,z=a*b))


def division(a,b):
    if (b > 0 ):
        print ("La divison de {x} / {y} es : {z}".format(x=a,y=b,z=a/b))
    else:
        print ("La divison no se puede realizar ")


def operaciones():
    numero1 = int(input("Ingrese primer numero :"))
    numero2 = int(input("Ingrese segundo numero :"))
    suma(numero1,numero2)
    resta(numero1,numero2)
    multiplicacion(numero1,numero2)
    division(numero1,numero2)
    
operaciones()
