# Author: Rodolfo 
# Date: October 28th 
# This script splits full names by space between them and displays it in parts


names = ["John Doe", "Grace Flores", "JB Oinonen"]

for name in names:
    # Find the position of the first space
    separator = name.find(" ")

    print("Full Name: {}".format(name))

    # separator to get first and last name, extracting strings
    first_name = name[:separator]
    last_name = name[separator + 1:]

    # Result
    print("First Name: {}".format(first_name))
    print("Last Name: {}".format(last_name))
    print(" ")