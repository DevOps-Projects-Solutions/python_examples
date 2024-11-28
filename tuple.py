example_tuple = (1, 2, 3, 2, 2, 4)

nested_tuple = (1, (2, 3), [4, 5, 6]) 


print("\nAccessing Elements:")

print(f"First element of multi_tuple: {example_tuple[0]}")

print(f"Last element of multi_tuple: {example_tuple[-1]}")

print(f"Second element of nested tuple: {nested_tuple[1]}")
print(f"Accessing element inside nested tuple: {nested_tuple[1][1]}") 

print("\nTuple Methods:")

print(f"Count of '2': {example_tuple.count(2)}")

print(f"Index of '3': {example_tuple.index(3)}")

# Unpacking tuples​

coordinates = (15, 25)

x, y = coordinates

print("\nUnpacking Tuple:")

print(f"x: {x}, y: {y}")

# Tuple immutability​

immutable_tuple = (5, 10, 15)

try:

        immutable_tuple[0] = 100 # commenting this line will  not raise an error​

        print("\nImmutability:")

        print("Tuples are immutable, and this line would raise an error.")

except TypeError as e:

        print(e)

# Tuple with a list inside​

print("\nModifying List Inside a Tuple:")

print(f"Before modification: {nested_tuple}")

nested_tuple[2][0] = 99 # The list inside the tuple is mutable​

print(f"After modification: {nested_tuple}")