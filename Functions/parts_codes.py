# Author: Rodolfo 
# Date: October 29
# Script to part codes 


# extracting by using : for supplier code
def get_supplier_code(part_codes):
  return part_codes.split(":")[0]

# extracting product number via the separators
def get_product_numb(part_codes):
  return part_codes.split(":")[1].split("-")[0]

# extracts the size from the code
def get_size(part_codes):
  return part_codes.split(":")[1].split("-")[1]

part_codes = ["ACME:123-L", "DI:12345-M", "ACE:1-12"]


# looping
for code in part_codes:
  supplier = get_supplier_code(code)  
  product = get_product_numb(code)
  size = get_size(code)
  # result
  print(f"{supplier} {product} {size}")
