def serve_chai():
    yield "Masala Chai is ready!"
    yield "Ginger Chai is ready!"
    yield "Elaichi Chai is ready!"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return["Cup 1", "Cup 2", "Cup 3"]

def get_chai_generator():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_list()
print(f"Chai list: {chai}")
chai_gen = get_chai_generator()
print(f"Chai generator: {chai_gen}")
print(f"First cup from generator: {next(chai_gen)}")   
print(f"Second cup from generator: {next(chai_gen)}")
print(f"Third cup from generator: {next(chai_gen)}")



#generate 1-10 using generators
def generate_numbers(n):
    for i in range(1, n+1):
        yield i
number_gen = generate_numbers(10)
print(number_gen)

#why no next is used below? 
# Because we are using a for loop to iterate through the generator, which automatically calls next() on the generator object in each iteration until it is exhausted.
for number in number_gen:
    print(number)