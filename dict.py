# Creating a dictionary​

person = {

    "name": "John", # Key: "name", Value: "John"​

      "age": 30, # Key: "age", Value: 30​

      "city": "New York" # Key: "city", Value: "New York"​

}

print("Dictionary:")

print(person)

# Accessing values using keys​

print("\nAccessing Dictionary Values:")

print(f"Name: {person['name']}")

print(f"Age: {person['age']}")
print(f"City: {person['city']}") 

# Adding a new key-value pair​

person["email"] = "john@example.com"

# Modifying an existing key-value pair​

person["age"] = 31

print("\nAfter Adding and Modifying:")

print(person)

# Removing a key-value pair​

del person["city"]

# Using pop() to remove and return a value​

age = person.pop("age")

print("\nAfter Removing Elements:")

print(person)

print(f"Removed Age: {age}")

# Keys method: Returns all keys in a dictionary​

keys = person.keys()

print("\nKeys:", keys)

# Values method: Returns all values in a dictionary​

values = person.values()

print("Values:", values)

# Items method: Returns all key-value pairs in a dictionary​

items = person.items()

print("Items:", items)
# Dictionary for contact information​

contacts = {

"John": {"phone": "123-456-7890", "email": "john@example.com"},

"Alice": {"phone": "987-654-3210", "email": "alice@example.com"},

}
# Accessing information​

print("\nContact Information:")

print(f"John's Phone: {contacts['John']['phone']}")

print(f"Alice's Email: {contacts['Alice']['email']}")
# Adding a new contact​

contacts["Bob"] = {"phone": "555-555-5555", "email": "bob@example.com"}

print(f"\nAfter Adding Bob: {contacts}")

