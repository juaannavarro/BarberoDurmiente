import threading
import time

class Peluqueria:
    def __init__(self):
        self.peluquero = threading.Semaphore(0)
        self.cliente = threading.Semaphore(0)
        self.silla = threading.Semaphore(3)
        self.control = threading.Semaphore(1)
        
    def cortarPelo(self):
        print("Peluquero cortando pelo")
        time.sleep(2)
        print("Peluquero termino de cortar pelo")
        
    
        
    