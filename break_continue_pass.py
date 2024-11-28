# Stop the loop when the number reaches 5​
numberone = 1

while numberone < 10:

      if numberone == 5:

             break

      print(numberone)

      numberone += 1


while True:

       command = input("Enter a command: ")

       if command == "exit":

              print("Exiting...")

              break

       print(f"You entered: {command}")

# Skip number 5 and print others​

for number in range(1, 8):

       if number == 5:

                 continue

       print(number)

# Skipping even numbers​

for number in range(1, 6):

    if number % 2 == 0:

          pass # Placeholder, do nothing for even numbers​

    else:

           print(f"Processing number: {number}")