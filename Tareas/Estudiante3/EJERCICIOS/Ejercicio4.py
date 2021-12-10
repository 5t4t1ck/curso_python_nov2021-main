"""Escribir un programa que le pida una palabra al usuario, 
para luego imprimirla 1000 veces, con espacios intermedios
"""
palabra=input("Ingrese una palabra: ")
nuevoString = palabra
conteo = 1
while (conteo <= 1000):
   nuevoString = nuevoString + palabra + " "
   conteo +=1
print("La palabra ingresada es: ",nuevoString)