def agregaNombreAArchivo(nombre, apellido):
    c = open("nombrecompleto.txt", "a")
    c.write(nombre + " " + apellido + "\n")
    c.close()

agregaNombreAArchivo("Diego", "Saavedra")

