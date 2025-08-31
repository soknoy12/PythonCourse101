shop_name = "Ice Cream"

# tax 10%
TAX_RATE = 1.1
TAX_RATE = 0.1

item_price = 2.5
item_quantity = 3
is_member = False

total = item_price * TAX_RATE * item_quantity

total = (item_price + (item_price * TAX_RATE)) * item_quantity

print("shop name", shop_name)
print("Total", total)

