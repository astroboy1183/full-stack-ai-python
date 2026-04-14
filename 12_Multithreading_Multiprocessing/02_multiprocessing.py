from multiprocessing import *
import time

def brew_chai(name):
    print(f"{name} chai served.")
    time.sleep(3)
    print(f"End of {name} chai brewing.")

if __name__ == "__main__":
    p1 = Process(target=brew_chai, args=("Masala",))
    p2 = Process(target=brew_chai, args=("Ginger",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("All chai brewed.")

#using loop to run multiple processes. 
    chai_makers = [ Process(target = brew_chai, args = (f"chai no.{i} brewing",)) for i in range(1,8)]
    [p.start() for p in chai_makers]
    [p.join() for p in chai_makers]
    print("All chai brewed.")

 



