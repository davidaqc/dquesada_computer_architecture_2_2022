from copy import copy

class cache():

    def __init__(this):
        this.cache_memory={
            "0": 
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                }
            ,
            "1": 
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                },
            "2": 
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                },
            "3": 
                {
                    "state": "I",
                    "value": "0x0000",
                    "dir": None
                }
        }

    # Leer dato de cache
    def read_data(this, direction_memory):

        block=""

        # correspondencia set one way (directa)
        if direction_memory%4==0:
            block=this.cache_memory["0"]
        elif direction_memory%4==1:
            block=this.cache_memory["1"]
        elif direction_memory%4==2:
            block=this.cache_memory["2"]
        elif direction_memory%4==3:
            block=this.cache_memory["3"]
            
        return block

    # Escribir dato en cache
    def write_data(this, value, replacement_direction, direction_memory, state=None):
        block=""

        block=this.cache_memory[str(replacement_direction)]

        block["value"]=copy(value)
        block["dir"]=direction_memory

        if state!=None:
            block["state"]=state
        return value

    # Cambiar estado en la cache
    def change_state(this, state, replacement_direction):
        this.cache_memory[str(replacement_direction)]["state"]=state
        return state
