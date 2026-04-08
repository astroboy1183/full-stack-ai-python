import sys

ideal_temp = 95.5
current_temp = 95.49999999999999

print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"difference: {ideal_temp - current_temp}")
print(sys.float_info)

a = 0.1 + 0.2
b = 0.3
print(abs(a - b) < sys.float_info.epsilon)  # Handles floating-point imprecision