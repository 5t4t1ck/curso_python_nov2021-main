"""
Escribir una función que encuentre el elemento menor de una lista
"""
lista = [1,2,3, -5, -24, 13]
menor = "init"


for x in lista:
    if menor == "init":
        menor = x
        #print(x)
    else:
        menor = x if x < menor else menor
        #print(menor)
print(menor)