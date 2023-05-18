from barbero import *
def main():
    peluqueria = Peluqueria()
    print("Peluqueria abierta", end="\n\n")
    
    peluquero_thread = threading.Thread(target=peluqueria.Peluquero)
    peluquero_thread.start()
    
    clientes = ['cliente 1', 'cliente 2', 'cliente 3', 'cliente 4']
    clientes_threads = []
    for cliente in clientes:
        cliente_thread = threading.Thread(target=peluqueria.Cliente, name=cliente)
        clientes_threads.append(cliente_thread)
        cliente_thread.start()  
        time.sleep(3)

    for cliente_thread in clientes_threads:
        cliente_thread.join()   
        
    peluquero_thread.join()