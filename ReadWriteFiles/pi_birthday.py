# Author: Rodolfo 
# Date: November 4 
# Script will be exploring reading files with the entire pi 


# Step 1: had a bit of trouble opening it; however the file path needs to start from w6 to the subfolder and the file
f = open("W6_Exercises/ReadWriteFiles/pi_million_digits.txt", "r")
first_line = f.readline()
print(first_line)  # Confirm the file opens correctly
f.close()

# Step 2: Read all lines into a list and close the file
f = open("W6_Exercises/ReadWriteFiles/pi_million_digits.txt", "r")
pi_lines = f.readlines()
f.close()

# format of the birthday 
user_birthday = input("Enter your birthday in the format MMDDYY: ")

# See if the numbers are there
birthday_found = None
for line in pi_lines:
    if user_birthday in line:
        print("Your birthday is in the first million digits of pi!")
        birthday_found = 1
        break

# in case birthday wasn't found
if birthday_found is None:
    print("Sorry, your birthday was not found in the first million digits of pi.")

# Combine pi digits into a single string
pi_string = ''
for line in pi_lines:
    pi_string += line.strip() 

# To see if the numbers are in the txt and print its position
if user_birthday in pi_string:
    birthday_position = pi_string.index(user_birthday) - 1  # -1 to adjust for zero indexing
    print(f"Your birthday begins at decimal place {birthday_position}")
else:
    print("Your birthday was not found in the first million digits of pi.")