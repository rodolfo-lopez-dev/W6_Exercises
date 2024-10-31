# Author: Rodolfo 
# Date: October 30 
# Script using various imports like random, math and stats

import random
import math
import statistics


# using example variables

# focusing on subsets of int 1-100:


vals_1_100 = range(1, 101)
vals_sample = random.sample(vals_1_100, 75)
print("Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values:", sum(vals_sample))
print("Average of 75 sample values:", round(statistics.mean(vals_sample)))
print("Median of 75 sample values:", statistics.median(vals_sample))
print('\n') 

# 