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
        for k in range(5):
            time.sleep(random.randint(1,2))
            k += 1
            print(str(threading.current_thread())+" Activa " + str(k)+"\n")
            if not self.continuar:
                break
        print("Termino: " + self.getName()+"\n")

def main():
    hilo = miHilo()
    hilo.start()

    hilo.join(7)
    if hilo.is_alive():
        hilo.terminar()
    else:
        print("El hilo termino antes de 5 segundos")

    print("Termino el hilo principal")


if __name__ == '__main__':
    main()

