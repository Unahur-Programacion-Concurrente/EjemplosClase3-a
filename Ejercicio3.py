import threading
import time
import random

class miHilo(threading.Thread):
    name = ""
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setName(name)

    def run(self):
        print("Arranco: " + self.getName()+"\n")
        time.sleep(random.randint(1,5))
        print("Terminó: " + self.getName() + " - Cantidad de Hilos Activos ="+str(threading.active_count())+"\n")

def main():
    cantHilos = random.randint(2,50)
    hilos = []
    for i in range(cantHilos):
        hilo = miHilo("hilo_"+str(i))
        hilo.start()
        hilos.append(hilo)

    print("Hay "+str(threading.active_count())+" hilos")
    time.sleep(3)
    print("Ahora hay "+str(threading.active_count())+" hilos")

#   Ejercicio 4
#    for h in hilos:
#        h.join()
#    print("Finalmente hay "+str(threading.active_count())+" hilos")

if __name__ == '__main__':
    main()

