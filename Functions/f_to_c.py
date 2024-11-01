# Author: Rodolfo 
# Date: October 31
# Script converting Fahrenheit to Celsius

def conv_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9 
    return round(celsius)

# Testing conv_f_to_c with sample Fahrenheit values
sample_temps = [212, 90, 72, 32, 0, -40]

for current_temp_F in sample_temps:
    current_temp_C = conv_f_to_c(current_temp_F)
    print(f"{current_temp_F} degrees Fahrenheit is equal to {current_temp_C} degrees Celsius.")
