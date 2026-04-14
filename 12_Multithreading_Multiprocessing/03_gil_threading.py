from concurrent.futures import thread
import threading
import time

import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing.")
    count = 0
    for i in range(100_000_000):
        count+=1
        # print(count)
    print(f"{threading.current_thread().name} finished brewing.")

thread1 = threading.Thread(target=brew_chai, name="barista-1")
thread2 = threading.Thread(target=brew_chai, name="barista-2")
thread3 = threading.Thread(target=brew_chai, name="barista-3")
thread4 = threading.Thread(target=brew_chai, name="barista-4")
thread5 = threading.Thread(target=brew_chai, name="barista-5")
thread6 = threading.Thread(target=brew_chai, name="barista-6")
thread7 = threading.Thread(target=brew_chai, name="barista-7")
thread8 = threading.Thread(target=brew_chai, name="barista-8")


start=time.time()    
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()      
thread7.join()
thread8.join()

end=time.time()

print(f"Time taken: {end - start:.2f} seconds")


#using a global counter and checking how every thread is changing the count value using the mutex.
# count=0
# def brew_chai():
#     print(f"{threading.current_thread().name} started brewing.")
#     global count
#     for i in range(10):
#         count+=1
#         print(f"{threading.current_thread().name} count: {count}")
#         print(count)
#     print(f"{threading.current_thread().name} finished brewing.")

# thread1 = threading.Thread(target=brew_chai, name="barista-1")
# thread2 = threading.Thread(target=brew_chai, name="barista-2")


# start=time.time()    
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# end=time.time()

# print(f"Time taken: {end - start:.2f} seconds")

