import dis
counter = 0

def funcion():
    global counter
    counter += 1

dis.dis(funcion)
