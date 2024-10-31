# Author: Rodolfo 
# Date: October 31
# Script 5 parameters, name address, city and zip 

# mailing label 

def display_mailing_label(name, address, city, state, zip_code):
    print(f"{name}\n{address}\n{city}, {state} {zip_code}\n")

# test mailing
display_mailing_label("David", "101 Apple St", "Chicago", "IL", "60629")
display_mailing_label("Slime Herrera","111 Banana St", "Chicago", "IL", "60629")

# second function to add numbers
def add_numbers(*numbers):
    total = sum(numbers)
    print("Sum:", total)


# test numbers
add_numbers(7)
add_numbers(7, 4)
add_numbers(1, 2, 3)


# the next function will display receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}" )
    print(f"Amount Paid: ${amount_paid:.2f}\n") 

    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f"Change Due: ${change_due:.2f}\n")
    else:
        balance_remaining =total_due - amount_paid
        print(f"Remaining Balance: ${balance_remaining:.2f}\n")


# test receipt
display_receipt(20, 20)
display_receipt(20, 25)
display_receipt(20, 10)