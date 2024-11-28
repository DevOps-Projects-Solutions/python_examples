# Initial list​

my_list = [3, 1, 4, 1, 5, 9, 2, 6]

# Using various list methods​

print(f"Original List: {my_list}")
# Adding elements​

my_list.append(7) # Append an element to the end​

print(f"After Append: {my_list}")


my_list.insert(2, 8) # Insert 8 at index 2​

print(f"After Insert: {my_list}")
# Removing elements​

my_list.remove(1) # Remove the first occurrence of 1​

print(f"After Remove: {my_list}")

popped_item = my_list.pop(3) # Remove and return the item at index 3​

print(f"After Pop: {my_list} (Popped Item: {popped_item})")

# Accessing elements​

print(f"First Element: {my_list[0]}") # Access by index​

print(f"Last Element: {my_list[-1]}")

# Sorting​

my_list.sort() # Sort the list in ascending order​

print(f"After Sort: {my_list}")
my_list.reverse() # Reverse the order of the list​

print(f"After Reverse: {my_list}")
# Searching and counting​

print(f"Index of 5: {my_list.index(5)}") # Find the index of the first occurrence of 5​

print(f"Count of 1: {my_list.count(1)}") # Count occurrences of 1​

# Copying and clearing​

copied_list = my_list.copy() # Create a shallow copy of the list​

print(f"Copied List: {copied_list}")

my_list.clear() # Clear all elements from the list​

print(f"After Clear: {my_list}")

# Creating a 2D list (matrix)​

matrix = [

[1, 2, 3],

[4, 5, 6],

[7, 8, 9]

]

# Accessing elements in a 2D list​

print(matrix[0]) # Access the first row: [1, 2, 3]​

print(matrix[1][2]) # Access element in 2nd row, 3rd column: 6​

# Iterating over each element​

for row in matrix:

     for elem in row:

                print(elem, end=" ") # Print each element