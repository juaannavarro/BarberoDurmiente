import threading
import time

class Peluqueria:
    def __init__(self):
        self.peluquero = threading.Semaphore(0)
        self.cliente = threading.Semaphore(0)
        self.silla = threading.Semaphore(4)
        self.control = threading.Semaphore(1)
        
    def cortarPelo(self):
        print("Peluquero cortando pelo")
        time.sleep(1)
        print("Peluquero termino de cortar pelo")
        
    def Cliente(self):
        print("Cliente ha llegado")
        self.control.acquire()
        
        if self.silla._value > 0:
            self.silla.acquire()
            print("Cliente se sienta en la silla de espera")
            self.control.release()
            self.cliente.release()
            print("Cliente despertando al peluquero")    
            self.peluquero.acquire()
            self.silla.release()
            print("Cliente deja la silla de espera")
            self.cortarPelo()
        else:
            self.control.release()
            print("No hay sillas disponibles")
        time.sleep(4)
            
    def Peluquero(self):
        while True:
            self.cliente.acquire()
            self.peluquero.release()
            time.sleep(4)
            
            

    
    
