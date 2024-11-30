# Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.

def array_builder(leng,start):
    my_array = []
    for i in range(leng):
        my_array.append(start+i)
    
    return my_array

# print(array_builder(5,50))
#______________________________________________________________
# write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" 
# and if is is divisible by both return "FizzBuzz"

    def fizzbuzz(num):
        my_str =""
        if num%3==0:
            my_str += 'Fizz'
        
        if num%5==0:
            my_str += 'Buzz'
        
        return my_str    

# print(fizzbuzz(45))

#______________________________________________________________
# Write a function which has an input of a string from user then it will return the same string reversed.

def str_reverser(my_str):
    reversed_string = ''
    str_len = len(my_str)
    for i in range(str_len):
        reversed_string += my_str[str_len-i-1]
    return reversed_string

# print(str_reverser("Ahmed Nasr"))

#______________________________________________________________
# Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for 
# his email and print all this data (Bonus) check if it is a valid email # or not

def get_user_data():
    name = input("What's your name ? ")
    while not is_valid_name(name.replace(" ","")):
        name = input("What's your name ? ")
    user_name = name
    
    email = input("What's your email ? ")
    while not is_valid_email(email.replace(" ","")):
        email = input("What's your email ? ")
    user_email = email

    print("User name :",user_name," User email :",user_email)

def is_valid_name(name):
    if name == "":
        return False
    for ch in name:
        if not ch.isalpha():
            return False 
    return True

def is_valid_email(email):
    if email == "":
        return False
    count_at = 0
    count_dot = 0
    at_index = 0
    if len(email) < 6 :
        return False
    for i,ch in enumerate(email):
        if i != 0 and ch == "@":
            count_at +=1
            at_index = i
        if (ch == "." and count_at == 1 and i < len(email) - 1 and i > at_index + 1 ):
            count_dot = 1

    return bool(count_at and count_dot)

# get_user_data()

#print(is_valid_name("Ahmed"))
#print(is_valid_email('ahmednasr@gmail.com'))



#__________________________________________________________

    # Write a function that takes a string and prints the
    # longest alphabetical ordered substring occurred For example, if
    # the string is 'abdulrahman' then the output is: Longest substring in
    # alphabetical order is: abdu


def get_long_alpha_order(input_string):
    long_str = ""
    current_ch= '0'
    for ch in input_string:
        if ch.capitalize() > current_ch:
            long_str += ch
            current_ch = ch.capitalize()
        else:
            break
    return long_str

# print(get_long_alpha_order('abCdEfGahiJklMnOPQrstUvWxYz'))
# print(get_long_alpha_order('abdulrahman'))
#_______________________________________________________________
# Write a program which repeatedly reads numbers until the user
# enters “done”.
# Once “done” is entered, print out the total, count, and
# average of the numbers.
# If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.


def statistics_calc():
    num_arr = []
    sum=0
    answer=''
    while answer.lower() != 'done':
        answer = input("Please enter a number : ")
        if answer.isdigit():
            num_arr.append(int(answer))
            sum += int(answer)
        else:
            print("Error!, Please insert a valid value ")

    print(f'''    Total is {sum},
    Count is {len(num_arr)},
    Average is {sum/len(num_arr)}
    ''')

# statistics_calc()


#_________________________________________________

# Word guessing game (hangman)

# A list of words will be hardcoded in your program, out of
# which the interpreter will choose 1 random word.
# -The user first must input their names
# -Ask the user to guess any alphabet. If the random word
# contains that alphabet, it
# -will be shown as the output(with correct placement)
# -Else the program will ask you to guess another alphabet.
# -Give 7 turns maximum to guess the complete word.

import random as r
def replace_dash_with_ch(input_str,choice_str,ch):
    out_str = ""
    for current_ch in choice_str:
        if current_ch in input_str:
            out_str += current_ch
            continue
        if current_ch == ch:
            out_str += current_ch
            continue
        out_str += '-'
    return out_str 

def guessing_game():
    words = ['cat','dog','bird','elephant','apple','banana','orange','horse','monkey']
    r.shuffle(words)
    current_choice = r.choice(words)
    user_answer='-'*len(current_choice)
    available_turns=7
    #print(current_choice)
    #print(user_answer)
    while user_answer != current_choice and available_turns != 0 :
        user_guess=input("Enter one letter guess : ")
        if user_guess in current_choice:
            user_answer = replace_dash_with_ch(user_answer,current_choice,user_guess)
            print(f"Your current answer {user_answer}")
        else:
            available_turns-=1
            print(f"Number of remaining turns is : {available_turns}")

    if user_answer == current_choice:
        print(f"Perfect! the word is {current_choice}")
    else:
        print("Game Over")


guessing_game()