"""colores = ["rojo", "verde", "azul","morado"]

for color in colores:
    print(color)

nombres = ["Juan", "Pedro", "Maria"]
#print(nombres[:])
for nombre in reversed(nombres):
    print(nombre)
    if nombre == "Juan":
        print("Si existe en la lista")
    else:
        print("No existe en la lista")
    print(nombre)

numeros = (1,2,3,4,5)
for numero in numeros:
    print(numero)

print(type(numeros))
print(type(nombres))"""


c = 0
while c <= 99:
    c+=1
    print("c vale: ",c)
    break
else:
    print("Se ha completado toda la interacción y c vale", c)
