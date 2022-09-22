from math import exp
from random import random
from random import randint

class processor:

    def __init__(this, number):
        this.number=number
        this.current_instruction=[]
        this.next_instruction=[]
        this.instructions=("calc","read","write")

    # Genera las instrucciones con valores y direccines aleatorias
    def generate_instruction(this):
        instruction=this.getPoisson(1.0)
        instruction=this.instructions[instruction]
        this.current_instruction=this.next_instruction

        if instruction=="calc":
            this.next_instruction=[instruction]
        elif instruction=="write":
            data=str(hex(randint(0,65535)))
            direction_memory=randint(0,7)
            this.next_instruction=[instruction, direction_memory, data]
        else:
            direction_memory=randint(0,7)
            this.next_instruction=[instruction, direction_memory]

    # Ejecuta la instruccion
    def run(this, instruction):

        if len(instruction)==0:
            this.generate_instruction()
        else:
            this.current_instruction=this.next_instruction
            this.current_instruction=instruction
        
        if len(this.current_instruction)==0:
            print("Message: No instruction loaded")
        else:
            if this.current_instruction[0]=="write":
                print ("P", this.number, ", Instruccion: ", this.current_instruction)
                this.control.write_data(this.current_instruction[1], this.current_instruction[2])
            elif this.current_instruction[0]=="read":
                print ("P", this.number, ", Instruccion: ", this.current_instruction)
                this.control.read_data(this.current_instruction[1])

    # Genera un número aleatorio de 0 a 2 mediante la distribucion de poisson
    def getPoisson(this, var_lambda):
        L = exp(-var_lambda)
        p = 2.0
        k = 0
        while True:
            k += 1
            p *= random()
            if p < L:
                break
        result = k - 1
        if result>=3:
            result =  this.getPoisson(var_lambda)
        return result
