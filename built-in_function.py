# 1. Input and Output​

name = input("Enter your name: ") # input() to take user input​

print(f"Hello, {name}!") # print() to display a message​


# 2. Type Checking​

age = int(input("Enter your age: ")) # Convert input to integer using int()​

print(f"Type of 'age' is: {type(age)}") # type() to check data type​

# 3. Working with Lists​

numbers = [5, 10, 15, 20, 25]
# len() to get the length of the list​

print(f"Number of elements in the list: {len(numbers)}")


# sum() to calculate the total sum​

print(f"Sum of numbers: {sum(numbers)}")
# max() and min() to find the largest and smallest elements​

print(f"Maximum value: {max(numbers)}")

print(f"Minimum value: {min(numbers)}")


# 4. Sorting and Rounding​

unsorted_list = [42, 12, 33, 7, 19]

# sorted() to get a sorted version of the list​

sorted_list = sorted(unsorted_list)

print(f"Sorted List: {sorted_list}")

# round() to round off numbers​

pi = 3.14159

print(f"Rounded value of pi: {round(pi, 2)}")

# 5. Checking Conditions​

is_adult = age >= 18

print(f"Are you an adult? {bool(is_adult)}") # bool() to convert to a Boolean

