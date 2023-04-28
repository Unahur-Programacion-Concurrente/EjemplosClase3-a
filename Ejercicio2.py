import threading
import time
import random

class miHilo(threading.Thread):
    name = ""
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setName(name)

#   Ejemplo que mezcla strings
#   def run(self):
#       print("Arranco: " + self.getName()+"\n")
#       time.sleep(random.randint(1,5))
#       print("Terminó: " + self.getName(), end=" - ")
#       print("Cantidad de Hilos ="+str(threading.active_count()), end="\n")

#para que no se desordenen los strings:
    def run(self):
        print("Arranco: " + self.getName()+"\n")
        time.sleep(random.randint(1,5))
        print("Terminó: " + self.getName() + " - Cantidad de Hilos Activos ="+str(threading.active_count())+"\n")

def main():
    for i in range(random.randint(2,50)):
        hilo = miHilo("hilo_"+str(i))
        hilo.start()
    time.sleep(4)


if __name__ == '__main__':
    main()

