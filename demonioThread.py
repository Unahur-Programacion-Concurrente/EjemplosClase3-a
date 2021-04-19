import threading
import time

def hiloStandard():
    print("hiloStandard iniciado")
    time.sleep(20)
    print("hiloStandard finalizado")

def hiloDemonio():
    while True:
        print("Haciendo algo en backgrond")
        time.sleep(2)

hiloStd = threading.Thread(target=hiloStandard)

hiloDmn = threading.Thread(target=hiloDemonio)
hiloDmn.setDaemon(True)

hiloDmn.start()
hiloStd.start()


print("Hilo principal Termino")


