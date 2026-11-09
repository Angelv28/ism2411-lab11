# Reflection
# 1. One way I can use the .get() method rather than bracket notation is when I want to avoid a KeyError if the key does not exist in the dictionary. The .get() method allows me to provide a default value if the key is not found, which can be useful for handling missing data gracefully.
# 2. Well, I never got to use excel that much to know how building a summary with a loop relates to excel, but I can definitely see how python can be useful for large datasets because it allows for automation and efficient data processing. 

# Exercise 1 create one customer dict with at least 4 fields : name, email, tier, ytd_spend 
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": 5000
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 add a phone field and delete email field 
customer["phone"] = "123-456-7890"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3
email = customer.get("email", "no email on file")
print(email)
try:
    print(customer["email"])
except KeyError:
    print("Bracket notation failed, no email on file")

# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(f"{key}: {customer[key]}")

# Exercise 5 lookup table create a tier discount and get()
tier_discount = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
purchase_amount = 200
discount_rate = tier_discount.get(customer["tier"], 0)
discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount
print(f"Tier: {customer['tier']}")
print(f"Discount %: {discount_rate*100}%")
print(f"Final Price: ${final_price:.2f}")

# Exercise 6 build a list with at least 3 different customers
dict1 = {"name": "Bob", "tier": "gold"}
dict2 = {"name": "Charlie", "tier": "bronze"}
dict3 = {"name": "Diana", "tier": "silver"}
customers = [dict1, dict2, dict3]
purchase_amount = 300

for customer in customers:
    name = customer["name"]
    tier = customer["tier"]
    discount_rate = tier_discount.get(tier, 0)
    discount_amount = purchase_amount * discount_rate
    print(f"name: {name}, tier: {tier}, discount: {discount_amount:.2f}")

# Exercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
} 
for item, info in catalog.items():
    current_stock = info["stock"]
    if current_stock < 20:
        print(f"LOW STOCK : {item} only has {current_stock} left in stock")

# Exercise 8
Transactions = [
    {"region": "south", "amount": 300}, 
    {"region": "north", "amount": 150}, 
    {"region": "south", "amount": 200},     
]
region_summary = {}
for transaction in Transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    region_summary[region] = region_summary.get(region, 0) + amount
for region in sorted(region_summary):
    print(f"{region}: {region_summary[region]}")    