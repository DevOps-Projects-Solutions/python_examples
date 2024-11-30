
# # 1) Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.
# input_string = input("Enter your string : ")
# count = 0
# for c in input_string:
#     if c.capitalize() in ['A','E','I','O','U']:
#         count +=1

# print("Number of voewls is : " , count)

#________________________
#2) Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.
# user_arr = []
# for i in range(5):
#   num = input("Enter your number :")
#   while not num.isdigit():
#      num = input("please enter a valide number :")
#   num = int(num)
#   user_arr.append( num )

# for i in range(len(user_arr)):
#    for j in range( i + 1 , len(user_arr)):
#        if user_arr[i] > user_arr[j]:
#            user_arr[i],user_arr[j] = user_arr[j],user_arr[i]

# print(user_arr) 
# print(user_arr[::-1])

#_____________________________
#3) Write a program that prints the number of times the string 'py' occurs in anystring.
# input_string = input("Enter your string : ")
# print(input_string.count('py'))
# count = 0
# i=0
# while i < len(input_string):
#     if input_string[i] == 'p' and input_string[i+1] == 'y' :
#           count +=1
#           i+=2
#     i += 1
# print(count)

#__________________________________
#4) Write a program that remove all vowels from the input word and generate a brief version of it.
# input_string = input("Enter your string : ")
# brief_version=""
# for ch in input_string:
#     if ch.capitalize() not in ['A','E','I','O','U']:
#         brief_version+=ch

# print(brief_version)

#_______________________________
#5) Write a program that prints the locations of "i" character in any string you added.
#input_string = input("Enter your string : ")
#for i,ch in enumerate(input_string):
  ##  if ch == 'i':
     #   print(i)

#__________________________________
#6) Write a program that generate a multiplication table from 1 to the number passed.
# num = input("Enter your number :")
# while not num.isdigit():
#   num = input("please enter a valide number :")
# num = int(num)
# list_of_lists = []
# for i in range(1,num+1):
#     minor_list=[]
#     for j in range(1,i+1):
#         minor_list.append(i*j)
#     list_of_lists.append(minor_list)

# print(list_of_lists)

#_____________________
#7)     
# num = int(input("Enter your number :"))
# l= len(range(1,num+1))
# for i in range(1,num+1):
#     print(" "*(l-i) ,'*'*i)


