import io

c = open("chanchito.txt", "w")

c.write( '\nagregamos una nueva linea a nuestro archivo 0')
c.write( '\nagregamos una nueva linea a nuestro archivo 1')
c.write( '\nagregamos una nueva linea a nuestro archivo 2')
c.write( '\nagregamos una nueva linea a nuestro archivo 3')

c.close()

x = open("chanchito.txt")

print(x.read())

x.close()

y = open("chanchito.txt")

leer = y.read()

for x in leer:
    print(x)

y.close()