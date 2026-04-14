import threading
import time

def take_orders():
    for i in range(1, 8):
        print(f"Taking order for #{i}")
        time.sleep(3)

def brew_chai():
    for i in range(1, 8):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

# create threads

t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=brew_chai)

#start threads
t1.start()
t2.start()

t1.join()
t2.join()

#show concurrency using for loop
threads=[]
for i in range(8):
    threads.append(threading.Thread(target=brew_chai))
    threads.append(threading.Thread(target=take_orders))

for t in threads:
    t.start()
    
for t in threads:
    t.join()

print("All orders taken and chai brewed.")

