import copy
import threading
import tkinter as tk

from tkinter import *
from processor import processor
from time import sleep

window = ""
memory = []
processors = []
misses = []
cache1 = {}
cache2 = {}
cache3 = {}
cache4 = {}

next_list = []
current_list = []
entry = ""
list_data = []
list_cache = []
threads = []
run = True
continuous = False
cicles = 0
step = False
multiple_steps = False

change_instruction=False
entry_state = "" 
entry_value = "" 
entry_dir = ""
entry_proc = ""

def begin():
    global window, next_list, current_list, entry, list_data, list_cache, entry_state, entry_value, entry_dir, entry_proc

    window = tk.Tk()
    width = 1200
    height = 400
    window.title("Coherencia de caché en sistemas multiprocesador")
    window.geometry(str(width) + "x" + str(height))
    
    mem_label = tk.Label(window, text="Memory")
    mem_label.place(x=185, y=180)

    list_dir = tk.Listbox(window, width=3, height=8)
    list_data = tk.Listbox(window, width=7, height=8)
    for i in range(len(memory)):
        list_dir.insert(i, i)

    list_dir.place(x=185, y=200)
    list_data.place(x=201, y=200)

    curr_ins_label_1 = tk.Label(window, text="Current instruction")
    curr_ins_label_2 = tk.Label(window, text="Current instruction")
    curr_ins_label_3 = tk.Label(window, text="Current instruction")
    curr_ins_label_4 = tk.Label(window, text="Current instruction")

    curr_ins_label_1.place(x=60, y=62)
    curr_ins_label_2.place(x=320, y=62)
    curr_ins_label_3.place(x=580, y=62)
    curr_ins_label_4.place(x=840, y=62)

    cache_name_1 = tk.Label(window, text="Cache")
    cache_name_2 = tk.Label(window, text="Cache")
    cache_name_3 = tk.Label(window, text="Cache")
    cache_name_4 = tk.Label(window, text="Cache")

    cache_name_1.place(x=60, y=84)
    cache_name_2.place(x=320, y=84)
    cache_name_3.place(x=580, y=84)
    cache_name_4.place(x=840, y=84)

    curr_ins_label_1 = tk.Label(window, text="Next instruction")
    curr_ins_label_2 = tk.Label(window, text="Next instruction")
    curr_ins_label_3 = tk.Label(window, text="Next instruction")
    curr_ins_label_4 = tk.Label(window, text="Next instruction")

    curr_ins_label_1.place(x=60, y=40)
    curr_ins_label_2.place(x=320, y=40)
    curr_ins_label_3.place(x=580, y=40)
    curr_ins_label_4.place(x=840, y=40)

    current_ins_1 = tk.Listbox(window, width=16, height=1)
    current_ins_2 = tk.Listbox(window, width=16, height=1)
    current_ins_3 = tk.Listbox(window, width=16, height=1)
    current_ins_4 = tk.Listbox(window, width=16, height=1)

    current_ins_1.place(x=185, y=62)
    current_ins_2.place(x=445, y=62)
    current_ins_3.place(x=705, y=62)
    current_ins_4.place(x=965, y=62)

    next_ins_1 = tk.Listbox(window, width=16, height=1)
    next_ins_2 = tk.Listbox(window, width=16, height=1)
    next_ins_3 = tk.Listbox(window, width=16, height=1)
    next_ins_4 = tk.Listbox(window, width=16, height=1)

    next_ins_1.place(x=185, y=40)
    next_ins_2.place(x=445, y=40)
    next_ins_3.place(x=705, y=40)
    next_ins_4.place(x=965, y=40)

    processor_0_label = tk.Label(window, text="Processor 0")
    processor_0_label.place(x=185, y=20)
    processor_1_label = tk.Label(window, text="Processor 1")
    processor_1_label.place(x=445, y=20)
    processor_2_label = tk.Label(window, text="Processor 2")
    processor_2_label.place(x=705, y=20)
    processor_3_label = tk.Label(window, text="Processor 3")
    processor_3_label.place(x=965, y=20)

    list_cache_1 = tk.Listbox(window, width=13, height=4)
    list_cache_2 = tk.Listbox(window, width=13, height=4)
    list_cache_3 = tk.Listbox(window, width=13, height=4)
    list_cache_4 = tk.Listbox(window, width=13, height=4)
    list_cache = [list_cache_1, list_cache_2, list_cache_3, list_cache_4]
    list_cache_1.place(x=205, y=84)
    list_cache_2.place(x=465, y=84)
    list_cache_3.place(x=725, y=84)
    list_cache_4.place(x=985, y=84)

    current_list = [current_ins_1, current_ins_2, current_ins_3, current_ins_4]
    next_list = [next_ins_1, next_ins_2, next_ins_3, next_ins_4]

    list_bloq_1 = tk.Listbox(window, width=3, height=4)
    for i in range(4):
        list_bloq_1.insert(i, "B" + str(i))
    list_bloq_1.place(x=185, y=84)

    list_bloq_2 = tk.Listbox(window, width=3, height=4)
    for i in range(4):
        list_bloq_2.insert(i, "B" + str(i))
    list_bloq_2.place(x=445, y=84)

    list_bloq_3 = tk.Listbox(window, width=3, height=4)
    for i in range(4):
        list_bloq_3.insert(i, "B" + str(i))
    list_bloq_3.place(x=965, y=84)

    list_bloq_4 = tk.Listbox(window, width=3, height=4)
    for i in range(4):
        list_bloq_4.insert(i, "B" + str(i))
    list_bloq_4.place(x=705, y=84)

    modes_label = tk.Label(window, text="Modes")
    modes_label.place(x=445, y=180)

    button_step = tk.Button(window, text="Step by step", command=step_func)
    button_continuous = tk.Button(window, text="Continuous", command=continuous_func)
    button_pause = tk.Button(window, text=" Pause  ", command=pause_func)

    button_step.place(x=445, y=200)
    button_continuous.place(x=445, y=230)
    button_pause.place(x=445, y=260)

    change_instr_label = tk.Label(window, text="Change instruction")
    change_instr_label.place(x=840, y=180)

    state_label = tk.Label(window, text="State")
    state_label.place(x=840, y=200)
    dir_label = tk.Label(window, text="Direction")
    dir_label.place(x=840, y=222)
    value_label = tk.Label(window, text="Value")
    value_label.place(x=840, y=244)
    processor_label = tk.Label(window, text="Processor")
    processor_label.place(x=840, y=266)

    entry_state = tk.Entry(window, width=20)
    entry_state.place(x=965, y=200)
    entry_dir = tk.Entry(window, width=20)
    entry_dir.place(x=965, y=222)
    entry_value = tk.Entry(window, width=20)
    entry_value.place(x=965, y=244)
    entry_proc = tk.Entry(window, width=20)
    entry_proc.place(x=965, y=266)

    button_change = tk.Button(window, text=" Change  ", command=change_instr_func)
    button_change.place(x=965, y=286)

def pause_func():
    global continuous
    if continuous:
        continuous = False

def step_func():
    global step
    step = not step 

def change_instr_func():
    global change_instruction
    change_instruction = True

def continuous_func():
    global continuous
    continuous = True

def update_misses(number):
    global misses
    if processors[number].control.misses != "":
        print("P", number + 1, "miss", processors[number].control.misses)
        misses.append(processors[number].control.misses)
        print("Misses:", misses)
    processors[number].control.misses = ""

def update_memory():
    global list_data
    for i in range(len(memory)):
        list_data.insert(i, memory[i])

def update_cache(number):
    global list_cache
    global cache1, cache2, cache3, cache4
    cache = {}

    if number == 1:
        cache = cache1
    elif number == 2:
        cache = cache2
    elif number == 3:
        cache = cache3
    else:
        cache = cache4
    string = ""
    count = 0
    if True:
        string += cache["3"]["state"] + "\t " + str(cache["3"]["dir"]) + "\t " + cache["3"]["value"]
        list_cache[number - 1].insert(count, string)
        string = ""
        count += 1
    string = ""
    count = 0
    if True:
        string += cache["2"]["state"] + "\t " + str(cache["2"]["dir"]) + "\t " + cache["2"]["value"]
        list_cache[number - 1].insert(count, string)
        string = ""
        count += 1
        string = ""
    count = 0
    if True:
        string += cache["1"]["state"] + "\t " + str(cache["1"]["dir"]) + "\t " + cache["1"]["value"]
        list_cache[number - 1].insert(count, string)
        string = ""
        count += 1
        string = ""
    count = 0
    if True:
        string += cache["0"]["state"] + "\t " + str(cache["0"]["dir"]) + "\t " + cache["0"]["value"]
        list_cache[number - 1].insert(count, string)
        string = ""
        count += 1
    
def execute_proc(number):
    global processors, run, cicles, step, multiple_steps, change_instruction, entry_state, entry_value, entry_dir, entry_proc
    new_instruccion=[]
    local_cicles = 0
    cicle = 0
    local_step = False
    local_steps = False
    while (run):
        if local_step != step:
            local_step = copy.copy(step)
            local_cicles = 1
            cicle = 0
        elif local_steps != multiple_steps:
            local_cicles = copy.copy(cicles)
            local_steps = copy.copy(multiple_steps)
            cicle = 0

        if change_instruction:
            if entry_proc.get() != "":
                if number == int(entry_proc.get()):
                    if entry_state.get() == "calc":
                        new_instruccion=[entry_state.get()]
                    elif entry_state.get() == "read":
                        new_instruccion=[entry_state.get(), int(entry_dir.get())]
                    elif entry_state.get() == "write":
                        new_instruccion=[entry_state.get(), int(entry_dir.get()), entry_value.get()]
                else:
                    new_instruccion=[]
            change_instruction = False
        
        while (continuous or cicle < local_cicles):
            with threading.Lock():
                processors[number].run(new_instruccion)
                '''if processors[number].control.misses != "":
                    misses.append(processors[number].control.misses)'''
                update_misses(number)
                update_memory()
                update_cache(number + 1)
                update_instructions(number + 1)
                if local_cicles > 1 or continuous:
                    sleep(2)
                cicle += 1
                new_instruccion=[]

def update_instructions(number):
    global current_list, next_list
    proc = processors[number - 1]
    curr_str = ""
    next_str = ""
    for i in proc.current_instruction:
        curr_str += str(i) + " "
    for i in proc.next_instruction:
        next_str += str(i) + " "

    current_list[proc.number - 1].insert(0, curr_str)
    next_list[proc.number - 1].insert(0, next_str)

def set_initial_data():
    global processors, memory, cache1, cache2, cache3, cache4, threads

    for i in range(1, 5):
        # Se crean 4 instancias del procesador
        print(i)
        processors.append(processor(i))
        # Se crean e inicializan 4 hilos
        threads.append(threading.Thread(target=execute_proc, args=(i-1,)))
        threads[i - 1].start()

    # Toma los valores iniciales de la memoria (cualquier procesador lo puede iniciar)
    memory = processors[0].control.bus.memory.memory
    # Toma los valores iniciales de cada cache (desaciertos obligatorios)
    cache1 = processors[0].control.cache.cache_memory
    cache2 = processors[1].control.cache.cache_memory
    cache3 = processors[2].control.cache.cache_memory
    cache4 = processors[3].control.cache.cache_memory

def on_finish():
    global threads, run, window
    run = False

    for thread in threads:
        thread.join()
    window.destroy()

def main():
    global window

    set_initial_data()
    begin()

    window.protocol("WM_DELETE_WINDOW", on_finish)
    window.mainloop()

main()
