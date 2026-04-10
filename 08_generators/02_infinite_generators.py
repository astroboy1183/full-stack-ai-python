def infinite_chai():
    count = 0
    while True:
        count += 1
        yield f"Chai cup #{count} is ready!" # Yielding a value instead of returning

obj1 = infinite_chai() # Creating a generator object

#why next is used below unlike the previous example? 
# Because we are explicitly calling next() to get the next value from the generator, rather than using a for loop to iterate through it.

for _ in range(5):
    print(next(obj1)) # Calling next() to get the next value from the generator

