# Author: Rodolfo
# Date: October 31
# Script includes functions about Social Security, medicare and federal taxes

def get_soc_sec_tax(gross_pay):
    tax = gross_pay * 0.062
    return round(tax, 2)

def get_medicare_tax(gross_pay):
    tax = gross_pay * 0.0145
    return round(tax, 2)

def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        tax_rate = 0.23
    elif withholding_code == 1:
        tax_rate = 0.21
    elif withholding_code == 2:
        tax_rate = 0.195
    elif withholding_code == 3:
        tax_rate = 0.185
    elif withholding_code >= 4:
        tax_rate = 0.18 - 0.005 * (withholding_code - 4)
    else:
        raise ValueError("Invalid withholding code")

    tax = gross_pay * tax_rate
    return round(tax, 2)

# Test with data provided
print("Person 1: Gross Pay $750, Withholding Code 0")
print("Social Security Tax:", get_soc_sec_tax(750))
print("Medicare Tax:", get_medicare_tax(750))
print("Federal Tax:", get_federal_tax(750, 0))

print("\nPerson 2: Gross Pay $1550, Withholding Code 2")
print("Social Security Tax:", get_soc_sec_tax(1550))
print("Medicare Tax:", get_medicare_tax(1550))
print("Federal Tax:", get_federal_tax(1550, 2))

print("\nPerson 3: Gross Pay $1100, Withholding Code 5")
print("Social Security Tax:", get_soc_sec_tax(1100))
print("Medicare Tax:", get_medicare_tax(1100))
print("Federal Tax:", get_federal_tax(1100, 5))
