# Define variables
name = "Alice"
age = 25
city = "New York"

# Using print() with f-string
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# Formatting numbers using f-string
price = 49.99
print(f"The price of the item is ${price:.2f}.")

# Aligning text using f-string
print(f"{'Name':<10}{'Age':<5}{'City':<15}")
print(f"{name:<10}{age:<5}{city:<15}")

# Using expressions inside f-string
x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}.")
