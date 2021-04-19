import threading
import time

def algunHilo():
    print("\nHilo actual: {}".format(threading.current_thread()))
    print("\nHilo principal: {}".format(threading.main_thread()))

hilos = []

for i in range(3):
    hilo = threading.Thread(target=algunHilo)
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()
