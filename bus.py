import threading

from memory import memory
from threading import Lock
from time import sleep

lock = Lock()

class bus:
    __instance=None

    @staticmethod
    # Creación de la instancia del bus
    def instantiate():
        if bus.__instance==None:
            with threading.Lock():
                if bus.__instance==None:
                    bus.__instance=bus()
                else:
                    print("Error: bus instance not created, currently exists")
        return bus.__instance

    # Inicializar los procesadores
    def __init__(this):
        this.memory=memory.instantiate()
        this.process_control_1=""
        this.process_control_2=""
        this.process_control_3=""
        this.process_control_4=""
        this.misses=""

    # Leer valores del procesador
    def read_data(this, direction_memory, number):
        block=()
        i=1
        while(i<5):
            lock.acquire()
            if i==1 and i!=number:
                block = this.process_control_1.read_data(direction_memory, True)
                print("Procesador", number, "| Revisando si el procesador 1 tiene el dato: ", block)
            elif i==2 and i!=number:
                block = this.process_control_2.read_data(direction_memory, True)
                print("Procesador", number, "| Revisando si el procesador 2 tiene el dato: ", block)
            elif i==3 and i!=number:
                block = this.process_control_3.read_data(direction_memory, True)
                print("Procesador", number, "| Revisando si el procesador 3 tiene el dato: ", block)
            elif i==4 and i!=number:
                block = this.process_control_4.read_data(direction_memory, True)
                print("Procesador", number, "| Revisando si el procesador 4 tiene el dato: ", block)

            if len(block)!=0:
                lock.release()
                return block
            i+=1
            lock.release()

        # Retardo por lectura a memoria (miss)
        #print("Procesador", number, "| Inicio del retardo por lectura a memoria")
        #sleep(4)
        this.misses = ("P"+str(number), "read", direction_memory)
        value=this.memory.read_data(direction_memory)
        #print("Procesador", number, "| Fin del retardo por lectura a memoria")
        return ("E", value)

    # Refresco los valores del procesador
    def set_process_control(this, number, process_control):
        if number==1:
            this.process_control_1=process_control
        elif number==2:
            this.process_control_2=process_control
        elif number==3:
            this.process_control_3=process_control
        elif number==4:
            this.process_control_4=process_control
            
    # Escribir dato en memoria
    def write_memory_data(this, direction_memory, value, number):
        # Retardo por escritura a memoria (miss)
        #print("Procesador", number, "| Inicio del retardo por escritura a memoria")
        #sleep(4)  
        this.misses = ("P"+str(number), "write", direction_memory, value)
        this.memory.write_data(direction_memory, value)
        #print("Procesador", number, "| Fin del retardo por escritura a memoria"
        #return this.memory.read_data(direction_memory)
    
    # Invalidar datos
    def invalidate_all(this, direction_memory, number):
        i=1
        while(i<5):
            if i==1 and i!=number:
                this.process_control_1.invalidate_instr(direction_memory)
            elif i==2 and i!=number:
                this.process_control_2.invalidate_instr(direction_memory)
            elif i==3 and i!=number:
                this.process_control_3.invalidate_instr(direction_memory)
            elif i==4 and i!=number:
                this.process_control_4.invalidate_instr(direction_memory)
            i+=1
