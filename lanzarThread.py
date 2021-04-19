import threading
import time
import random

def ejecutarHilo(i):
    print("Hilo {} iniciado".format(i))
    retardo = random.randint(1,10)
    time.sleep(retardo)
    print("\nHilo {} finalizado".format(i))

for i in range(10):
    hilo = threading.Thread(target=ejecutarHilo, args=(i,))
    hilo.start()


