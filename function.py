# Function with parameters​

def greet_user(name):

         print(f"Hello, {name}! Welcome to Python!")

# Function that returns a value​

def add_numbers(a, b):

         return a + b

# Calling the function with arguments​

greet_user("Alice")

greet_user("Bob")

# Using the return value​

result = add_numbers(5, 3)

print(f"The sum is: {result}")

# function with multiple return values​

def arithmetic_operations(a, b):

        sum_result = a + b

        diff_result = a - b

        return sum_result, diff_result

# Using the unction​

sum_val, diff_val = arithmetic_operations(10, 5)

print(f"Sum: {sum_val}, Difference: {diff_val}")

