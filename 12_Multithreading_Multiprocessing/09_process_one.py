import threading
import time
from tracemalloc import start

start_times={}
end_times={}
def cpu_heavy():
    print("Crunching some numbers...")

    total = 0
    for i in range(10**8):
        total += i
    print("DONE")

'''
This code is used to track the time each thread takes to execute, 
along with the order in which the threads execute.

def cpu_heavy(thread_name):
    # print("Crunching some numbers...")
    start_times[thread_name]=time.thread_time()
    print("thread_name started",thread_name)

    total = 0
    for i in range(10**8):
        total += i
    print("DONE")

    end_times[thread_name] = time.thread_time()
    print(f"{thread_name} finished")

'''


start_time = time.time()

#code for two threads
t1 = threading.Thread(target=cpu_heavy)
t2 = threading.Thread(target=cpu_heavy)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Time taken: {time.time() - start_time:.2f} seconds")

#without using threads explicitly 
start_time = time.time()
cpu_heavy()
print(f"Time Taken:{time.time() - start_time:.2f} seconds.")

#multiple threads
threads = [threading.Thread(target=cpu_heavy) for i in range(8)]
start_time = time.time()
[t.start() for t in threads]
[t.join() for t in threads]

'''
Uncomment this code to track each thread's execution time and order.

#multiple threads
threads = [threading.Thread(target=cpu_heavy,args=(f"thread-{i}",)) for i in range(8)]
start_time = time.time()
[t.start() for t in threads]
[t.join() for t in threads]

# print(start_times)
# print(end_times) 

for thread_name in start_times:
    start_time = start_times[thread_name]
    end_time = end_times[thread_name]
    print(f"{thread_name} took {end_time - start_time:.2f} seconds")
    '''

print(f"Time taken: {time.time() - start_time:.2f} seconds")



      