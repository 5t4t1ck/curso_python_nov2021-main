lista = [1,2,3,4,55,-24,-13]

menor = "init"

for x in lista:
    if menor == "init":
        menor = x
    else:
        menor = x if x < menor else menor

print("menor es:", menor)