# Author: Rodolfo 
# Date: November 4
# Script will exploring reading files

f = open("About_me.txt", "r")
print(f.read())
f.close()

# above just presents the original info

f = open("About_me.txt", "r")
print(f.read(50))
print(f.read(50))
f.close()

# print double about me txt and misses the final perfect night out statement 


f = open("About_me.txt", "r")
print(f.readline(10)) # to read 10 characters of the first line
print(f.readline()) # simply reads the next line

# adding simple loop
for i in range (3):
    print(f.readline())
f.close()

# trying readlines
f = open("About_me.txt", "r")
print(f.readlines(1)) # just my name
print(f.readlines(10)) # my place of birth entirely 
print(f.readlines(100)) # and my pets, dream place and peferred
print(f.readlines(-1)) # all remaining 
f.close()

# Store read results in variables 
f = open("About_me.txt", "r")
first_50 = f.read(50)  # First 50 characters
next_lines = [f.readline() for _ in range(4)]  # Next 4 lines
next_100 = f.readlines(100)  # Next 100 characters
f.close()

# Results
print("First 50 characters:", first_50)
print("Next four lines:", next_lines)
print("Next 100 characters as list:", next_100)
