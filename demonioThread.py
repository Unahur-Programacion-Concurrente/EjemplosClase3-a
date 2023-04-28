import threading
import time

def hiloStandard():
    print("hiloStandard iniciado")
    time.sleep(20)
    print("hiloStandard finalizado")

def hiloDemonio():
    while True:
        print("Haciendo algo en background")
        time.sleep(2)

hiloStd = threading.Thread(target=hiloStandard)

hiloDmn = threading.Thread(target=hiloDemonio, daemon=True)
# hiloDmn.setDaemon(False)

hiloDmn.start()
hiloStd.start()


print("Hilo principal Termino")


