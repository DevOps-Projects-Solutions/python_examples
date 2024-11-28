set1 = {1, 2, 3, 4, 5} # Set with integer elements​

print("Sets:")
print(set1)

# Adding elements to a set​

set1.add(6) # Adds 6 to set1​

print(f"After adding 6: {set1}")
# Removing elements from a set​

set1.remove(6) # Removes 6 from set1​

print(f"After removing 6: {set1}")

# Discarding an element (doesn't raise error if element is not found)​

set1.discard(5)

print(f"After discarding 5: {set1}")

# Set union​

setA = {1, 2, 3}

setB = {3, 4, 5}

union_set = setA | setB # Or: setA.union(setB)​

print(f"Union: {union_set}") # {1, 2, 3, 4, 5}​


# Set intersection​

intersection_set = setA & setB # Or: setA.intersection(setB)​

print(f"Intersection: {intersection_set}") # {3}​

# Set difference​

difference_set = setA - setB # Or: setA.difference(setB)​

print(f"Difference: {difference_set}") # {1, 2}​

# Set Methods​

example_set = {1, 2, 3, 4, 5}


# Clearing all elements from the set​

example_set.clear()
print(f"After clear: {example_set}") # set()​


# Copying a set​

example_set = {1, 2, 3}

new_set = example_set.copy()

print(f"New set after copy: {new_set}") # {1, 2, 3}​

# Checking if an element exists in a set​

print(3 in example_set) # True​

print(6 in example_set) # False