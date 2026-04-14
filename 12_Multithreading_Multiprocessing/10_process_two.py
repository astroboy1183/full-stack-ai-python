from multiprocessing import Process
from multiprocessing import Queue
import time

start_times={}
end_times={}
# def cpu_heavy():
#     print("Crunching some numbers...")

#     total = 0
#     for i in range(10**8):
#         total += i
#     print("DONE")

def cpu_heavy(process_name, q):
    print(f"{process_name} started")
    start_time = time.process_time()
    
    q.put({
        "event":"START",
        "process_name":process_name,
        "cpu_start_time":start_time
    })

    total = 0
    for i in range(10**8):
        total += i
    print("DONE")

    end_time = time.process_time()
    
    q.put({
        "event":"FINISH",
        "process_name":process_name,
        "cpu_end_time":end_time
    })

    print(f"{process_name} finished")

# #without using processes explicitly
# start_time = time.time()
# cpu_heavy()
# print(f"Time Taken:{time.time() - start_time:.2f} seconds.")

# start_time = time.time()

# #code for two processes
# p1 = Process(target=cpu_heavy)
# p2= Process(target=cpu_heavy)

# p1.start()
# p2.start()
# p1.join()
# p2.join()

# print(f"Time taken: {time.time() - start_time:.2f} seconds")

# #multiple processes using for loop

# start_time = time.time()
# processes = [Process(target=cpu_heavy) for _ in range(8)]
# [p.start() for p in processes]
# [p.join() for p in processes]

# print(f"Time taken: {time.time() - start_time:.2f} seconds")

#multiple processes using for loop along with tracking each process start and finish. 
q=Queue()

processes = [Process(target=cpu_heavy,args=(f"process-{i}",q)) for i in range(8)]
[p.start() for p in processes]

for _ in range(2*len(processes)):

    message = q.get()
    event = message["event"]
    process_name = message["process_name"]
    # cpu_start_time = message["cpu_start_time"]
    # cpu_end_time = message["cpu_end_time"]

    if event == "START":
        start_times[process_name] = message["cpu_start_time"]
    elif event == "FINISH":
        end_times[process_name] = message["cpu_end_time"]

[p.join() for p in processes]

print(start_times)
print(end_times)

for process_name in start_times:
    start_time = start_times[process_name]
    end_time = end_times[process_name]
    print(f"{process_name} took {end_time - start_time:.2f} seconds")