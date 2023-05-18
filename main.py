from barbero import *
def main():
    peluqueria = Peluqueria()
    
    peluquero_thread = threading.Thread(target=peluqueria.Peluquero)
    peluquero_thread.start()
        
    clientes_threads = []
    print("Creando clientes", end="\n\n")
    for i in range(10):
        cliente_thread = threading.Thread(target=peluqueria.Cliente)
        clientes_threads.append(cliente_thread)
        cliente_thread.start()  
        time.sleep(3)
        
    for cliente_thread in clientes_threads:
        cliente_thread.join()   
        
    peluquero_thread.join()