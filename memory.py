import threading

class memory:
    __instance=None

    @staticmethod
    def instantiate():
        if memory.__instance==None:
            with threading.Lock():
                if memory.__instance==None:
                    memory.__instance=memory()
                else:
                    print("Error: memory instance not created, currently exists")
        return memory.__instance

    # Inicializar memoria
    def __init__(this):
        this.memory=["0x0000", "0x0001", "0x0002", "0x0003",
                       "0x0004", "0x0005", "0x0006", "0x0007"]

    # Leer dato de la memoria
    def read_data(this, direction_memory):
        for i in range(len(this.memory)):
            if i==direction_memory:
                return this.memory[i]

    # Escribir dato en memoria
    def write_data(this, direction_memory, data):
        print("-- Escribiendo en memoria - direccion:", direction_memory, "dato:", data, "--")
        for i in range(len(this.memory)):
            if i==direction_memory:
                this.memory[i]=data
                return this.memory[i]
            