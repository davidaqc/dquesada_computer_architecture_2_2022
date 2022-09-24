from cache import cache
from bus import bus

class control:
    #Genero e inicializo componentes
    def __init__(this, number):
        this.cache=cache()
        this.cache_state=this.cache.cache_memory
        this.cache_state
        this.bus=bus.instantiate()
        this.bus.set_process_control(number, this)
        this.number=number
        this.misses=""
        
    #Lee las instrucciones
    def read_data(this, direction_memory, request=False):
        block=""
        i=0
        # correspondencia set one way (directa)
        if direction_memory%4==0:
            if this.cache_state["0"]["dir"]==direction_memory and this.cache_state["0"]["state"]!="I":
                block=this.cache.read_data(direction_memory)
                i=0
        elif direction_memory%4==1:
            if this.cache_state["1"]["dir"]==direction_memory and this.cache_state["1"]["state"]!="I":
                block=this.cache.read_data(direction_memory)
                i=1
        elif direction_memory%4==2:
            if this.cache_state["2"]["dir"]==direction_memory and this.cache_state["2"]["state"]!="I":
                block=this.cache.read_data(direction_memory)
                i=2
        elif direction_memory%4==3:
            if this.cache_state["3"]["dir"]==direction_memory and this.cache_state["3"]["state"]!="I":
                block=this.cache.read_data(direction_memory)
                i=3

        if isinstance(block, str) and not request:
            print ("Procesador", this.number, "| Dato invalido, revisar bus")
            return this.check_bus_data(direction_memory)
        elif not isinstance(block, str) and request:
            replacement_state="S"
            if block["state"]=="E" or block["state"]=="M":
                replacement_local_state=""
                if block["state"]=="E":
                    replacement_local_state="S"
                elif block["state"]=="M":
                    replacement_local_state="S"
                    this.bus.write_memory_data(direction_memory, block["value"], this.number)
                    this.misses = ("P"+str(this.number), "write", direction_memory, block["value"])
                this.cache.change_state(direction_memory, replacement_local_state, i)
            return (replacement_state, block["value"])
        elif not isinstance(block, str):
            return block["value"]
        else:
            return ()

    # Revisa el bus de datos
    def check_bus_data(this, direction_memory):
        block=this.bus.read_data(direction_memory, this.number)

        if block[0] == "E":
            # Retardo por lectura a memoria (miss)
            #print("Procesador", number, "| Inicio del retardo por lectura a memoria")
            #sleep(4)
            #print("Procesador", number, "| Fin del retardo por lectura a memoria")
            this.misses = ("P"+str(this.number-1), "read", direction_memory)

        i=this.replacement_policy(direction_memory)
        this.cache.write_data(block[1], i, direction_memory, block[0])
        return block

    # Escribe los datos
    def write_data(this, direction_memory, data):
        block=0
        if direction_memory%4==0:
            block=0
        elif direction_memory%4==1:
            block=1
        elif direction_memory%4==2:
            block=2
        elif direction_memory%4==3:
            block=3

        this.bus.invalidate_all(direction_memory, this.number)
        return this.cache.write_data(data, block, direction_memory, "M")

    # Politica de remplazo
    def replacement_policy(this, direction_memory):

        # correspondencia set one way (directa)
        if direction_memory%4==0:
            if this.cache_state["0"]["state"] != "M":
                i = 0
        elif direction_memory%4==1:
            if this.cache_state["1"]["state"] != "M":
                i = 1
        elif direction_memory%4==2:
            if this.cache_state["2"]["state"] != "M":
                i = 2
        elif direction_memory%4==3:
            if this.cache_state["3"]["state"] != "M":
                i = 3

        # ...........
        if direction_memory%4==0:
            if this.cache_state["0"]["state"] == "M":
                i = 0
                block=this.cache.read_data(this.cache_state[str(i)]["dir"])
                this.bus.write_memory_data(this.cache_state[str(i)]["dir"], block["value"], this.number)
                # Retardo por escritura a memoria (miss)
                #print("Procesador", number, "| Inicio del retardo por escritura a memoria")
                #sleep(4) 
                #print("Procesador", number, "| Fin del retardo por escritura a memoria"
                this.misses = ("P"+str(this.number), "write", direction_memory, block["value"])
        elif direction_memory%4==1:
            if this.cache_state["1"]["state"] == "M":
                i = 1
                block=this.cache.read_data(this.cache_state[str(i)]["dir"])
                this.bus.write_memory_data(this.cache_state[str(i)]["dir"], block["value"], this.number)
                this.misses = ("P"+str(this.number), "write", direction_memory, block["value"])
        elif direction_memory%4==2:
            if this.cache_state["2"]["state"] == "M":
                i = 2
                block=this.cache.read_data(this.cache_state[str(i)]["dir"])
                this.bus.write_memory_data(this.cache_state[str(i)]["dir"], block["value"], this.number)
                this.misses = ("P"+str(this.number), "write", direction_memory, block["value"])
        elif direction_memory%4==3:
            if this.cache_state["3"]["state"] == "M":
                i = 3
                block=this.cache.read_data(this.cache_state[str(i)]["dir"])
                this.bus.write_memory_data(this.cache_state[str(i)]["dir"], block["value"], this.number)
                this.misses = ("P"+str(this.number), "write", direction_memory, block["value"])

        return i

    def invalidate_instr(this, direction_memory):
        block=0
        if direction_memory%4==0:
            if this.cache_state["0"]["dir"] == direction_memory:
                block=0
        elif direction_memory%4==1:
            if this.cache_state["1"]["dir"] == direction_memory:
                block=1
        elif direction_memory%4==2:
            if this.cache_state["2"]["dir"] == direction_memory:
                block=2
        elif direction_memory%4==3:
            if this.cache_state["3"]["dir"] == direction_memory:
                block=3

        if not isinstance(block, str):
            if this.cache_state[str(block)]["state"]=="M":
                block_readed=this.cache.read_data(this.cache_state[str(block)]["dir"])
                this.bus.write_memory_data(this.cache_state[str(block)]["dir"], block_readed["value"], this.number)
                this.misses = ("P"+str(this.number), "write", direction_memory, block_readed["value"])
            this.cache.change_state(direction_memory, "I", block)
            return True
        else:
            return False
        