# Python Beginner Toolkit - Main File

print("Welcome to the Python Beginner Toolkit!\n")

# Hello World
print("1. Hello World Example:")
print("Hello World\n")

# Variables
print("2. Variables Example:")
name = "Mary"
age = 20
print("Name:", name)
print("Age:", age, "\n")

# User Input
print("3. User Input Example:")
user_name = input("Enter your name: ")
print("Hello", user_name, "\n")

# If Statement
print("4. If Statement Example:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult\n")
else:
    print("You are a minor\n")

# Loop
print("5. Loop Example:")
for i in range(5):
    print(i)

print("\nEnd of examples.")
