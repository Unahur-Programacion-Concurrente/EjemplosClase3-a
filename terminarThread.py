import threading
import time
import random

class miHilo(threading.Thread):
    def __init__(self):
        super().__init__()
        self.continuar = True

    def terminar(self):
        self.continuar = False

    def run(self):
        print("Arranco: " + self.getName()+"\n")
        k = 0
        while self.continuar:
            time.sleep(random.randint(1,2))
            k += 1
            print(str(threading.current_thread())+" Activa " + str(k)+"\n")
        print("Termino: " + self.getName()+"\n")

def main():
    hilo = miHilo()
    hilo.start()
    time.sleep(5)

    hilo.terminar()


if __name__ == '__main__':
    main()

