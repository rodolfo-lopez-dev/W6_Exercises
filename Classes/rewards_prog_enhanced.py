# Author: Rodolfo
# Date: November 1
# Script: Enhanced Rewards Program for restaurant customers

class RewardsProgram:
    """Represents a rewards program for customers."""

    # initializes cust_name, phone email and the additional info 
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.restaurants = []  # Track unique restaurants visited
        self.points = 0        # Total rewards points

    # Customer profile details
    def profile(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    # Thank-you message method
    def thank_you(self):
        print(f"Thank you, {self.name}, for visiting!")

    # Method to add customer details/append
    def add_to_list(self, cust_list):
        cust_list.append((self.name, self.phone, self.email))

    # tracking visiting and updated the points of rewards
    def visit_restaurant(self):
        rest_name = input("Name of restaurant: ")
        if rest_name not in self.restaurants:
            self.restaurants.append(rest_name)

        total_bill = float(input("Total food bill: "))
        reards_points = int(bill)  # Rounding to whole numbers
        self.points += points
        
        print(f"Points earned: {points}, Total points: {self.points}")
        print(f"Thank you for visiting {rest_name}!")

# Customer list
cust_list = []

cust1 = RewardsProgram("Jose Herrera", "555-1234", "JJose@example.com")
cust2 = RewardsProgram("David Herrera", "555-5678", "Bigdave@example.com")
cust3 = RewardsProgram("Isma Herrera", "555-8765", "Isma@example.com")

# Tests
for customer in [cust1, cust2, cust3]:
    customer.profile()
    customer.thank_you()
    customer.add_to_list(cust_list)
    customer.visit_restaurant()

# Results
print("\nCustomer List:")
print(cust_list)