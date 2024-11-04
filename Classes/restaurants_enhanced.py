# Author: Rodolfo  
# Date: November 1
# Script enhanced restaurant that focuses on number served, customer rating 

class Restaurant:
    """Class to show a restaurant with enhanced attributes of tracking and ratings"""

    # Initializes instance with restaurant name, food type, and default attributes
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name            
        self.food_type = food_type            
        self.number_served = 0                
        self.customer_ratings = []          

    # Method to describe the restaurant
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    
    def rest_open(self):
        print(f"{self.rest_name} is open.")

    # Adds to the total customers served
    def add_num_served(self):
        customers = int(input("How many customers were served today? "))
        self.number_served += customers

    # Prints total customers served
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    # Adds customer rating, calculates, and prints average
    def customer_rating(self):
        rating = int(input("How would you rate your experience today on a scale of 1-5? "))
        if 1 <= rating <= 5:
            self.customer_ratings.append(rating)
            avg_rating = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {avg_rating:.2f}.")
        else:
            print("Rating is not in range between 1 and 5.")

# Test with Restaurant class 
rest1 = Restaurant("Dunkin", "Coffee and Pastries")
rest2 = Restaurant("McNaldos", "Fast Food")
rest3 = Restaurant("Sbubby", "Sandwiches")

# Testing customer count and rating for each restaurant.
for restaurant in [rest1, rest2, rest3]:
    restaurant.describe_rest()
    restaurant.print_num_served() 
    restaurant.add_num_served()    
    restaurant.print_num_served()  
    
    # Results for ratings and calculate avg 
    for _ in range(3):
        restaurant.customer_rating()
