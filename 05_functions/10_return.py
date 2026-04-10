# Return values from functions
 
# single return value
def make_chai():
    return "Masala Chai"
chai = make_chai()
print(f"Chai: {chai}")

#returns None if no return statement is provided
def idle_chaiwala():
    pass

print(idle_chaiwala())

#early return
def chai_status(cups_left):
    if cups_left == 0:
        return "No more chai available."
    return f"Chai is available. Cups left: {cups_left}"

print(chai_status(5))
print(chai_status(0))

#multiple return values
def chai_report():
    return 10,200,30,40
cups, revenue, _ = chai_report()
print(f"Cups sold: {cups}, Revenue: {revenue}")
