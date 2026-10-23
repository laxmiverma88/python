# Assignment - 2
# Write a program to input student name & marks of 3 student name and marks of 3 subject . print name & percentage in output.

student_name = input("Enter Student name : ")
hindi_marks = input("Enter hindi marks : ")
english_marks = input("Enter english marks : ")
science_marks = input("Enter science marks : ")

# calculate percentage

percentage = (int(hindi_marks)+ int(english_marks)+ int(science_marks)/300)*100
# print("name :", student_name )
# print("percentage :", percentage)

print (f"The result of {student_name} is {int(percentage)} % well done")

# write a python program that called multiple types of data (eg., name, age, height, and student status)
# from user input, store then in a dictionary and then print out the collected data  ?

user_data = {}
user_data['name'] = input("Enter your name ")
user_data['age'] = input("Enter your age")
user_data['height'] = input("Enter your height")
user_data['student status'] = input("Are you student")

print(user_data)