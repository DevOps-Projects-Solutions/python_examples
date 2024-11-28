# Function to write employee data to a CSV file​

def write_to_csv(filename, data):

      with open(filename, mode='w', newline='') as file:

              writer = csv.DictWriter(file, fieldnames=["Name", "Age", "Department"])

              writer.writeheader() # Write column headers​

              writer.writerows(data) # Write rows of data​

      print(f"Data written to {filename}")

# Function to read employee data from a CSV file​

def read_from_csv(filename):

        with open(filename, mode='r') as file:

                  reader = csv.DictReader(file)

                  data = [row for row in reader]

        print(f"Data read from {filename}:")

        for row in data:

                  print(row)

        return data
# Function to write data to a JSON file​

def write_to_json(filename, data):

      with open(filename, mode='w') as file:

                json.dump(data, file, indent=4)

      print(f"Data written to {filename}")

# Function to read data from a JSON file​

def read_from_json(filename):

         with open(filename, mode='r') as file:

                data = json.load(file)

         print(f"Data read from {filename}:")

         print(json.dumps(data, indent=4))

         return data

import csv

import json

def main():

   csv_filename = "employees.csv"

   json_filename = "employees.json"

   # Step 1: Employee data​

   employees = [
   {"Name": "Alice", "Age": 30, "Department": "HR"},
   {"Name": "Bob", "Age": 25, "Department": "Engineering"}
   ]

  # Step 2: Write employee data to a CSV file​

   write_to_csv(csv_filename, employees)

  # Step 3: Read employee data from the CSV file​

   csv_data = read_from_csv(csv_filename)

  # Step 4: Write the CSV data to a JSON file​

   write_to_json(json_filename, csv_data)

  # Step 5: Read and display the JSON file content​

   read_from_json(json_filename)

if __name__ == "__main__":
  main()