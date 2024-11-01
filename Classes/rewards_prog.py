# Author: Rodolfo 
# Date: November 1 
# Script 
class RewardsProgram:
    """" class to be a rewards program customers of a restaurante """
    # We'd be initializing instance for customer name, phone, and email.
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name  
        self.phone = phone          
        self.email = email          

    #  method for profile details
    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    #  thank you message 
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    # adding a customer details
    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

# Global list to store customer details.
cust_list = []

# Create three sample 
cust1 = RewardsProgram("Jose Herrera", "555-1234", "JJose@example.com")
cust2 = RewardsProgram("David Herrera", "555-5678", "Bigdave@example.com")
cust3 = RewardsProgram("Isma Herrera", "555-8765", "Isma@example.com")

# A thank you message to add to the list
cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()

cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()

cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()

# Result
print("\nCustomer List:")
print(cust_list)
