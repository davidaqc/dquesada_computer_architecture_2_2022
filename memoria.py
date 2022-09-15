
class Memoria:

    # Inicializar memoria
    def __init__(this):
        this.memoria = ["0x0000", "0x0000", "0x0000", "0x0000",
                       "0x0000", "0x0000", "0x0000", "0x0000"]

    # Leer dato de la memoria
    def leer_dato(this, direccion_de_memoria):
        for i in range(len(this.memoria)):
            if i == direccion_de_memoria:
                return this.memoria[i]

    # Escribir dato en memoria
    def escribir_dato(this, direccion_de_memoria, dato):
        for i in range(len(this.memoria)):
            if i == direccion_de_memoria:
                this.memoria[i] = dato
                return this.memoria[i]
                