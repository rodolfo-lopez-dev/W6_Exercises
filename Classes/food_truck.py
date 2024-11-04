# Author: Rodolfo
# Date: November 4
# Script: Enhanced Restaurant Classes with FoodTruck

# Define the Restaurant class
class Restaurant:
    """Represents a restaurant and its food type."""

    def __init__(self, rest_name, food_type):
        # Initialize restaurant name and food type
        self.rest_name = rest_name
        self.food_type = food_type

    # The restaurant's name and food type
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

     # Restaurant being open
    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Creating a new type of restaurant called a FoodTruck
class FoodTruck(Restaurant):
    """Represents a food truck with extra features."""

    def __init__(self, rest_name, food_type):
        # Super ()._init__ to borrow the restaurant name and type from the Restaurant
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'  #  no private bookings
        self.truck_location = ''     # for no specific location

    def accepts_private_bookings(self):
        response = input("Accept private bookings? (Y/N): ").upper()
        self.private_bookings = response
        # Showing the booking status
        if self.private_bookings == 'Y':
            print(f"{self.rest_name} accepts private bookings.")
        else:
            print(f"{self.rest_name} does not accept private bookings.")

    def relocate_truck(self):
        # Update and print the truck's current location
        self.truck_location = input("Enter truck location (address, city): ")
        print(f"Truck is now at {self.truck_location}")

# Create a FoodTruck instance
food_truck = FoodTruck("DD on the Road", "Coffee and Pastries")
food_truck.describe_rest()
food_truck.rest_open()
food_truck.accepts_private_bookings()
food_truck.relocate_truck()





