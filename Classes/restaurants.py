# Author: Rodolfo 
# Date: November 1 
# Script def restaurants classes


# Here we intialize instance between name and food type 
class Restaurant:
    """"Class to demonstrate a restaurant of my choice and their food types"""
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

# using two methods 
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    def rest_open(self):
        print(f"{self.rest_name} is open.")


# three restaurants instances 
rest1 = Restaurant("Dunkin", "Coffee and Pastries")
rest2 = Restaurant("McNaldos", "Fast Food")
rest3 = Restaurant("Sbubby", "Sandwiches")

# call describe_rest and rest open

rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()