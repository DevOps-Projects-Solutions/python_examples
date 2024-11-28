def write_to_file(filename, content):

      """

     This function writes content to a file.

      if the file does not exist, it will be created.

      """

      # Open the file in write mode ('w')​

      with open(filename, 'w') as file:

            file.write(content)

      print(f"Data written to {filename}")

def read_from_file(filename):

      """

      This function reads content from a file and returns it.

      If the file does not exist, it will print an error message.

       """

      # Open the file in read mode ('r')​

      try:

          with open(filename, 'r') as file:

                    content = file.read()

          return content

      except FileNotFoundError:

          return "File not found."
      
def append_to_file(filename, content):

        """

        This function appends content to an existing file.

        """

       # Open the file in append mode ('a')​
        with open(filename, 'a') as file:

              file.write(content)

        print(f"Data appended to {filename}")

def main():

     filename = "user_data.txt" 

     # Step 1: Write initial data to the file​

     user_data = "John Doe, 25\n"

     write_to_file(filename, user_data)

     # Step 2: Read and display the file content​

     print("\nReading from the file:")

     print(read_from_file(filename))

     # Step 3: Append new user data to the file​

     new_user_data = "Jane Smith, 30\n"

     append_to_file(filename, new_user_data)

    # Step 4: Read and display the updated file content​

     print("\nReading updated file content:")

     print(read_from_file(filename))


if __name__ == "__main__":

       main()