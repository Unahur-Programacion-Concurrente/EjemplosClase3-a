import threading
import time
import random

#def miHilo():
#    print("Arranco: " + threading.current_thread().name)
#    time.sleep(random.randint(1,5))
#    print("\nTerminó: " + threading.current_thread().name)

def miHilo(i):
    threading.current_thread().setName("hilo_"+str(i))
    print("Arranco: " + threading.current_thread().name+"\n")
    time.sleep(random.randint(1,5))
    print("Terminó: " + threading.current_thread().name+"\n")

def main():
    for i in range(random.randint(2,50)):
#        hilo = threading.Thread(target=miHilo)
#        hilo = threading.Thread(target=miHilo,name="hilo #"+str(i))
        hilo = threading.Thread(target=miHilo, args=(i,))

        hilo.start()
    time.sleep(4)

if __name__ == '__main__':
    main()

