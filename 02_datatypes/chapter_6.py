chai_type = "Ginger Chai"
customer_type = "Priya"

print(f"""Customer: {customer_type}\nChai: {chai_type}""")

chai_description = "Aromatic and Bold"

print("first word of chai description:", chai_description[0])
print("last word of chai description:", chai_description[-1])
print("substring of chai description:", chai_description[0:9])
print("substring of chai description:", chai_description[0:4])

#step function in string slicing
print("every second character in chai description:", chai_description[::2])

#print from index 5 to the end
print("substring from index 5 to the end:", chai_description[5:])

#use -n to print from the end of the string
print("substring from index -5 to the end:", chai_description[-5:])

print("substring from index -5 to -3:", chai_description[-5:-2])

#copy above text
print("substring from index -7 to -2:", chai_description[-7:-2])
print("substring from index -7 to -1:", chai_description[-7:-1])

#  reverse the string
print("reverse of chai description:", chai_description[::-1])

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")  
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")