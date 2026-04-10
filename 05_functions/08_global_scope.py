chai_type="Plain"

def front_desk():
    def kitchen():
        global chai_type # Refers to the global variable
        chai_type = "Irani" # Modifies the global variable

    kitchen()


front_desk()
# chai_type = "Tulsi"
print(f"final global chai: {chai_type}")