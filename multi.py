# Processes: Independent programs running separately. No 
# shared memory, so no interference. Good for CPU-heavy 
# tasks.

# Threads: Smaller tasks within a process, sharing the same 
# memory. Good for tasks where waiting is involved (like 
# file reading), but limited by the GIL in Python.

# GIL: A lock that ensures only one thread executes Python 
# bytecode at a time, which simplifies memory management but 
# limits true multi-threading.

from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(101):
        i*i
        time.sleep(0.1)

processes = []
num_process = os.cpu_count() 
#good number is the number of cpu u have 

# create process
for i in range (num_process):
    p = Process(target= square_numbers)
    processes.append(p)

#start

for p in processes:
    p.start()

#join
for p in processes:
    p.join()

print("end main")