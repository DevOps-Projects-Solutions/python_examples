# Initial string​
text = " Hello, Python World! Python is fun."
# Using various string methods​

print(f"Original: '{text}'")

print(f"Length: {len(text)}")    # Length of the string​

print(f"Lowercase: {text.lower()}")                                               # Convert to lowercase​

print(f"Uppercase: {text.upper()}")                                              # Convert to uppercase​

print(f"Capitalized: {text.capitalize()}")                                     # Capitalize the first character​

print(f"Title Case: {text.title()}")                                                    # Title case​

print(f"Stripped: '{text.strip()}'")                                                   # Remove leading/trailing whitespace​

print(f"Replaced: {text.replace('Python', 'Coding')}")        # Replace "Python" with "Coding"

print(f"Split: {text.split()}") # Split into words​

print(f"Joined: {'-'.join(['Python', 'is', 'awesome'])}") # Join words with a delimiter​

print(f"Starts with ' Hello': {text.startswith(' Hello')}") # Check prefix​

print(f"Ends with 'fun. ': {text.endswith('fun. ')}") # Check suffix​

print(f"Find 'Python': {text.find('Python')}") # Find first occurrence of "Python"​

print(f"Count 'Python': {text.count('Python')}") # Count occurrences of "Python"​

print(f"Is Alpha: {'Python'.isalpha()}") # Check if all characters are alphabets​

print(f"Is Digit: {'12345'.isdigit()}") # Check if all characters are digits​

print(f"Is Lower: {'python'.islower()}") # Check if all characters are lowercase​

print(f"Is Upper: {'PYTHON'.isupper()}") # Check if all characters are uppercase