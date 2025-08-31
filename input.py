shop_name = input("Please enter your shop name:")

TAX_RATE = 1.1
DISCOUNT = 10.0 # Discount 10%

item_price = float(input("Enter your price:"))
item_quantity = int(input("Enter number of product"))
is_member = input("Are you a memeber?")

total = item_price * TAX_RATE * item_quantity

# is_member.lower() == "yes"
# is_member.upper() == "YES"
is_member.capitalize() == "Yes"

if (is_member.strip().lower() == "yes"):
    total = total - (total * DISCOUNT / 100)
else:
    total = total

print(shop_name)
print(total)
