# Pizza Order Cost Calculator

# Get pizza size
size = input("Enter pizza size (small/large): ").lower()

# Get number of toppings
toppings = int(input("How many extra toppings?: "))

# Get delivery distance
miles = int(input("Delivery distance in miles?: "))

# Determine base pizza price
if size == "small":
    base_price = 8
elif size == "large":
    base_price = 12
else:
    print("Invalid pizza size.")
    exit()

# Calculate topping cost
topping_cost = toppings * 1

# Calculate delivery cost
if miles <= 5:
    delivery_cost = 2
else:
    delivery_cost = 2 + (miles - 5)

# Calculate total
total_cost = base_price + topping_cost + delivery_cost

# Display result
print(f"\nOrder Summary:")
print(f"Pizza size: {size}")
print(f"Toppings cost: ${topping_cost}")
print(f"Delivery cost: ${delivery_cost}")
print(f"Total cost: ${total_cost}")