import threading
import time
import random

def miHilo(i):
    print("Hilo {}: arranco".format(i))
    time.sleep(random.randint(1,5))
    print("Hilo {}: finalizó".format(i))

def main():
    for i in range(4):
        hilo = threading.Thread(target=miHilo, args=(i,))
        hilo.start()
    print("Hilos: {}".format(threading.enumerate()))

if __name__ == '__main__':
    main()

