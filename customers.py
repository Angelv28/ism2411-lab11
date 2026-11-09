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
#print(customer[email]) 

# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(f"{key}: {customer[key]}")

