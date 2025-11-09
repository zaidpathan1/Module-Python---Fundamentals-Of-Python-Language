# Practical 1: Python Code Structure

def greet_user():
    """Simple function to demonstrate structure"""
    print("Welcome to the Python Variables Demo!")

# Practical 2: Creating Variables

name = "Zaid"             
age = 20                 
height = 5.9             
is_student = True         

print("\n--- Created Variables ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Practical 3: Taking User Input

user_name = input("\nEnter your name: ")
user_age = input("Enter your age: ")

print("Hello,", user_name, "! You are", user_age, "years old.")

# Practical 4: Checking Data Types Dynamically

print("\n--- Data Types of Variables ---")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
print("Type of user_name:", type(user_name))
print("Type of user_age:", type(user_age))


greet_user()