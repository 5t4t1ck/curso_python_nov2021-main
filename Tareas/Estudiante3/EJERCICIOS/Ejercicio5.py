"""
Realiza un programa que reciba una cantidad de minutos y 
muestre por pantalla a cuantas horas y minutos corresponde
"""

minutos = int(input("Ingrese la cantidad de minutos :"))
min = minutos%60
horas = int(minutos/60)

print ("El valor ingresado es {t} minutos, en horas {horas} y {min} minutos".format(t=minutos,horas=horas,min=min))


