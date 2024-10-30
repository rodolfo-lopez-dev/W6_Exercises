# Rodolfo 
# October 30 
# script to use random module to experiment

import random

# finding a random int from 10 to 20 

rand_int = random.randint(10, 20)
print("Generate a random number:", rand_int)

# finding random float from 0 to 1  but rounding after running the first time it was too long

rand_float = random.random()
print("Give an example of a random formatted: {:.2f}".format(rand_float))

# selecting random thing from a list 

fruits = ["apple", "banana", "cherry", "peach", "plum", "watermelon"]
rand_choice = random.choices(fruits)
print("Give an example of a random", rand_choice)

# multiple choices


rand_choices = random.choices(fruits, k=2)
print("Give an example of a random", rand_choices)

# finding a sample from 1 to 3000 and selecting 3 numbers
random_numbers = random.sample(range(1, 3000), 3)
print("Give me a sample with random numbers from 1 to 3000:", random_numbers)

# back to using fruits exercise, we'll shuffle the list 

random.shuffle(fruits)
print("Give me a shuffle of fruits:", fruits)