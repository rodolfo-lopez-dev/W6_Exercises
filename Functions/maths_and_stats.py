# Author: Rodolfo 
# Date: October 30 
# Script using various imports like random, math and stats

import random
import math
import statistics


# def all example variables


vals_1_100 = range(1, 101)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3,10)
pi = math.pi

# subset of int 1-100

print("Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values:", sum(vals_sample))
print("Average of 75 sample values:", round(statistics.mean(vals_sample)))
print("Median of 75 sample values:", statistics.median(vals_sample))
print('\n') 

# superset of 200, int 1-100
print("Experimenting with a superset of 200 value of 1-100 integers:")
print("Average of 200 values:", round(statistics.mean(vals_choices)))
print("Median of 200 values:", round(statistics.median(vals_choices)))
print("Mode of 200 values:", round(statistics.mode(vals_choices)))
print("Standard deviation of 200 values:", round(statistics.stdev(vals_choices)))
print("Variance of 200 values:", round(statistics.variance(vals_choices)))
print('\n')


# modeling a random circle 

print("Modeling a random circle:")
print("Radius:", radius)
print("Ceiling of the area:", math.ceil(pi * radius ** 2))
print("Floor of the area:", math.floor(pi * radius ** 2))
print('\n')
