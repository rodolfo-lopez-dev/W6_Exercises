
# Author: Rodolfo 
# Date: October 31
# Script includes a function to convert Celsius to Fahrenheit

def conv_c_to_f(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit)

# Testing conv_c_to_f with sample Celsius values
sample_temperatures = [100, 45, 19, 0, -7, -40]

for current_temp_C in sample_temperatures:
    current_temp_F = conv_c_to_f(current_temp_C)
    print(f"{current_temp_C} degrees Celsius is equal to {current_temp_F} degrees Fahrenheit.")