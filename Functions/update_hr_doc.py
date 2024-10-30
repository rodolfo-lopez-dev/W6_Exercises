# Author: Rodolfo
# Date: October 29
# This script updates and displays HR records.

# Original HR list
hr_list = [
    ('0123', 'HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahna Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')
]

# Updating specific records in the HR list
def update_records(hr_list):
    updated_list = []

    for record in hr_list:
        emp_id, dept, name, salary = record

        # test's
        if name == "Mark Blick":
            name = "Mark Blick-Hawley"
        if name == "Jim Smith":
            dept = "CS"
            salary = "60000"
        updated_list.append((emp_id, dept, name, salary))

    return updated_list  # Return the list with any updates

#  HR records in a table
def display_hr_list(hr_list):
    # Header
    print("Employee# | DeptCode | Name           | Salary")
    print("-" * 50)

    # Loop through each record in the list
    for record in hr_list:
        emp_id, dept, name, salary = record
        # from "60000" to "60,000"
        formatted_salary = "{:,.0f}".format(float(salary))

        # Print each record in a table row format
        print(f"{emp_id}      | {dept}     | {name:<17} | ${formatted_salary}")

# Update the HR list records based on specified changes
updated_hr_list = update_records(hr_list)

# Display the updated list in a formatted output
display_hr_list(updated_hr_list)