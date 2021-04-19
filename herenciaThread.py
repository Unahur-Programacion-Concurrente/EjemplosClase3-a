from threading import Thread

class miHilo(Thread):
    def __init__(self):
        print("miHilo se ha construido")
        Thread.__init__(self)

    def run(self):
        print("El hilo se esta ejecutando")

miTarea = miHilo()
print("Objeto Hilo Creado")

miTarea.start()
print("Arrancando miTarea")

miTarea.join()
print("termino miTarea")


