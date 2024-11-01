# Author: Rodolfo 
# Date: November 1
# Script working with "The Name Game" and using trunc function 

# we'll start by creating trunc_name variable

def trunc_name(name):
    name = name.lower()
    
    # If a vowel is in the start, leave it unchanged
    if name[0] in 'aeiou':
        return name
    
    # We'll need to modify a string to remove any starting consonants
    for i in range(len(name)):
        if name[i] in 'aeiou':
            return name[i:]
    return name 

# using original and truncate versions of the name
def name_game(name):
    trunc = trunc_name(name)
    
    # Using yield to allow the function to return each line of the song
    yield f"{name}, {name}, bo-b{trunc}"
    yield f"Banana-fana fo-f{trunc}"
    yield f"Fee-fi-mo-m{trunc}"
    yield f"{name}!"

# Prompt user for a name
user_name = input("Enter a name for The Name Game song: ")

# Result 
for line in name_game(user_name):
    print(line)

# the outputs for my name, and the following examples worked 