import threading
import time
import random

def miHilo(i):
    print("Hilo {}: arranco".format(i))
    time.sleep(random.randint(1,5))
    print("Hilo {}: finalizó".format(i))

def main():
    for i in range(random.randint(2,50)):
        hilo = threading.Thread(target=miHilo, args=(i,))
        hilo.start()
    time.sleep(4)
    print("Cantidad de hilos Activos: {}".format(threading.active_count()))

if __name__ == '__main__':
    main()

