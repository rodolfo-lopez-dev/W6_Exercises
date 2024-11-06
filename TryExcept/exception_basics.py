# Author: Rodolfo 
# Date: November 5 
# Script adds code blocks to raise specific exceptions using try-except 

# ValueError 

try:
    goals = int("hat-trick")  # Try to turn the string "hat-trick" into an integer
except ValueError:
    print("ValueError: 'hat-trick' cannot be converted to a number.")
else:
    print(f"Goals scored: {goals}")
finally:
    print("Try something else...") 


# NameError
try:
    print(player_position)  # player_position' is undefined
except NameError:
    print("NameError: The player's position hasn't been defined.")
else:
    print(player_position)
finally:
    print("Try something else...")

# TypeError
try:
    team_name = "Real Madrid"
    total_goals = team_name + 3  # Trying to combine a string with an integer
except TypeError:
    print("TypeError: You cannot mix a team name with a goal count.")
else:
    print(f"{team_name} scored {total_goals} goals.")
finally:
    print("Try something else...")


# SyntaxError
try:
    eval("if win_count > 5 print('Winning season!')")  # We will miss a colon in 'if' statement
except SyntaxError:
    print("SyntaxError: Missing colon in the if statement.")
finally:
    print("Try something else...") 

