import threading
import time

class Peluqueria:
    def __init__(self):
        self.control = threading.Semaphore(1)
        self.peluquero = threading.Semaphore(0)
        self.cliente = threading.Semaphore(0)
        self.silla = threading.Semaphore(4)
        self.clientes_cortados = []
        self.clientes_peluqueria = []

        
    def cortarPelo(self):
        print("Peluquero cortando el pelo ")
        time.sleep(2)
        cliente_cortado = threading.current_thread().name
        self.clientes_cortados.append(cliente_cortado)
        print(f'El barbero termino de cortar el pelo a {cliente_cortado}')
        
    def Cliente(self):
        cliente = threading.current_thread().name
        self.clientes_peluqueria.append(cliente)
        print(f'{cliente} entra a la peluqueria', end="\n\n")        
        self.control.acquire()
        if self.silla._value > 0 and self.silla._value <= 4:
            print('------Hay sillas disponibles------')
            self.silla.acquire()
            print(f"{cliente} se sienta en la silla de espera")
            time.sleep(3)
            self.control.release()
            self.cliente.release()
            if len(self.clientes_peluqueria) == 1:
                
                print(f"{cliente} despierta al peluquero")
                time.sleep(3)
                self.peluquero.acquire()
                self.silla.release()
                print(f"{cliente} deja la silla de espera")
                time.sleep(3)
                print(f"{cliente} se sienta en la silla del peluquero")
                self.cortarPelo()
                print(f'{cliente} se va de la peluqueria', end="\n\n")
            else:
                time.sleep(3)  
                self.peluquero.acquire()
                self.silla.release()
                print(f"{cliente} deja la silla de espera")
                time.sleep(3)
                print(f"{cliente} se sienta en la silla del peluquero")
                self.cortarPelo()
                print(f'{cliente} se va de la peluqueria', end="\n\n")
        elif self.silla._value >= 5:
            self.control.release()
            print("No hay sillas disponibles")
        time.sleep(3)
            
    def Peluquero(self):
        if self.cliente._value == 0:
            print("Peluquero durmiendo", end="\n\n")
        while True:
            self.cliente.acquire()
            self.peluquero.release()
            print("Peluquero disponible")
            time.sleep(3)
            
            

            




