import threading
import time

class Peluqueria:
    def __init__(self):
        self.peluquero = threading.Semaphore(0)
        self.cliente = threading.Semaphore(0)
        self.silla = threading.Semaphore(3)
        self.control = threading.Semaphore(1)
        
    def cortarPelo(self):
        print("Peluquero cortando el pelo")
        time.sleep(3)
        print("Peluquero termina de cortar el pelo")
        
    def Cliente(self):
        print("Cliente llega a la peluqueria")
        self.control.acquire()
        
        if self.silla._value > 0 and self.silla._value <= 3:
            print('------Hay sillas disponibles------')
            self.silla.acquire()
            print("Cliente se sienta en la silla de espera")
            time.sleep(3)
            self.control.release()
            if self.peluquero._value == 0:
                self.cliente.release()
                print("Cliente despierta al peluquero")
                time.sleep(3)
                self.peluquero.acquire()
                self.silla.release()
                print("Cliente deja la silla de espera")
                time.sleep(3)
                print("Cliente se sienta en la silla del peluquero")
                self.Peluquero()
            else:
                time.sleep(3)  
                self.peluquero.acquire()
                self.silla.release()
                print("Cliente deja la silla de espera")
                time.sleep(3)
                self.cortarPelo()
        elif self.silla._value >= 4:
            self.control.release()
            print("No hay sillas disponibles")
        time.sleep(3)
            
    def Peluquero(self):
        if self.cliente._value == 0:
            print("Peluquero durmiendo", end="\n\n")
        while True:
            self.cliente.acquire()
            self.peluquero.release()
            self.cortarPelo()
            self.silla.release()
            time.sleep(3)
            
            
def main():
    peluqueria = Peluqueria()
    
    peluquero_thread = threading.Thread(target=peluqueria.Peluquero)
    peluquero_thread.start()
    
    clientes_threads = []
    for i in range(10):
        cliente_thread = threading.Thread(target=peluqueria.Cliente)
        clientes_threads.append(cliente_thread)
        cliente_thread.start()  
        
        time.sleep(3)
        
    for cliente_thread in clientes_threads:
        cliente_thread.join()   
        
    peluquero_thread.join()
            

if __name__ == "__main__":
    main()    
    


