from random import randint

class Procesador:

    def __init__(this, numero):
        this.numero = numero
        this.instruccion_actual = []
        this.instruccion_siguiente = []
        this.instrucciones = ("calc", "read", "write")

    # Genera las instrucciones con valores y direccines aleatorias
    def generar_instruccion(this):
        instruccion = randint(0,2)
        instruccion = this.instrucciones[instruccion]
        this.instruccion_actual = this.instruccion_siguiente

        if instruccion == "calc":
            this.instruccion_siguiente = [instruccion]
        elif instruccion == "write":
            dato = str(hex(randint(0, 65535)))
            direccion_de_memoria = randint(0,7)
            this.instruccion_siguiente = [instruccion, direccion_de_memoria, dato]
        else:
            direccion_de_memoria = randint(0,7)
            this.instruccion_siguiente = [instruccion, direccion_de_memoria]
        print(this.instruccion_siguiente)

    # Ejecutar la instruccion
    def ejecutar(this):
        this.generar_instruccion()
        if len(this.instruccion_actual) == 0:
            print("Mensaje: No se cargó ninguna instrucción")
        else:
            if this.instruccion_actual[0] == "write":
                print ("Write")
            elif this.instruccion_actual[0] == "read":
                print ("Read")