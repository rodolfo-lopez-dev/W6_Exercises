# Author: Rodolfo
# Date: November 5
# Script working with "The Name Game" and using trunc function

# using trunc_name variable
def trunc_name(name):
    name = name.lower()

    # Using if a vowel is in the start, it will be unchanged
    if name[0] in 'aeiou':
        return name

    # modifing a string to remove any starting consonants 
    for i in range(len(name)):
        if name[i] in 'aeiou':
            return name[i:]
    return name

# using original and truncate version of the name game 
def name_game(name):
    trunc = trunc_name(name)

    # Using yield to allow the function to return each line of the song 
    yield f"{name}, {name}, bo-b{trunc}"
    yield f"Banana-fana fo-f{trunc}"
    yield f"Fee-fi-mo-m{trunc}"
    yield f"{name}!"

# Using exception for a name
while True:
    try:
        user_name = input("Enter a name for The Name Game song: ").strip()

        # Check if the input is 2 characters or more
        if len(user_name) < 2:
            raise ValueError("The name must be at least 2 letters long.")

        # Ensure the name is alphabetical
        if not user_name.isalpha():
            raise ValueError("The name must contain only letters (no numbers or symbols).")

        break  # Exit loop if above is met 

    except ValueError as e:
        print(f"Invalid input: {e}")
    finally:
        print("Please enter a valid name.")

# Results 
for line in name_game(user_name):
    print(line)