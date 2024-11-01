# Author: Rodolfo 
# Date: October 31 
# Script referring to lambda functions

# creating a function for lambda 
doubler = lambda n: n * 2
tripler = lambda n: n * 3

# now we'll print the following values 
print("doubler:")
print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

# now in triple 
print("Tripler:")
print(tripler(8))
print(tripler(-4))
print(tripler("banana"))

# creating multiplers 
def multiplier(factor):
    return lambda n: n * factor

# using variables provided in example 5
# quad=4,quin=5,sextu=6,sep=7....

quad = multiplier(4)
quin = multiplier(5)
sextu = multiplier(6)
sept = multiplier(7)
oct = multiplier(8)
non = multiplier(9)
dec = multiplier(10)

# Testing each multiplier with a sample number (-4) thought of 
# also using x = -4 and setting all values to x ex. 
# print print("Quadrupler (x):", quad (x))
print("Additional Multipliers:")
print("Quadrupler (-4):", quad(-4))  
print("Quintupler (-4):", quin(-4))  
print("Sextupler (-4):", sextu(-4))    
print("Septupler (-4):", sept(-4))    
print("Octupler (-4):", oct(-4))      
print("Nonupler (-4):", non(-4))      
print("Decupler (-4):", dec(-4)) 