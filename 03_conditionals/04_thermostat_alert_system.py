'''
Task:

You're building a smart thermostat alert system:

If the device_status is "active"
And temperature > 35 → Warn: "High temperature alert!"
Else: "Temperature normal"
If device is off → "Device is offline"

'''

device_status = input("Enter device status (active/off): ").lower()  # convert input to lowercase for case-insensitive comparison
input_temperature = float(input("Enter current temperature: "))
units = input("Enter temperature units (C/F): ").upper()  # convert input to uppercase for case-insensitive comparison       
print(f"Device status: {device_status}")
print(f"Current temperature: {temperature}°{units}")

temperature = input_temperature
if units == "F":
    temperature = (input_temperature - 32) * 5.0/9.0  # convert Fahrenheit to Celsius

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature normal")

elif device_status == "off":
    print("Device is offline")

else:
    print("Unknown device status")