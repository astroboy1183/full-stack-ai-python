# file = open("order.txt","w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close


#behind the scenes exectutes file__enter__() and file__exit__()
with open("order.txt","w") as file:
    file.write("Masala chai - 2 cups")
