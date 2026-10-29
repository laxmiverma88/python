# Assignment - 3

# Leap year:
# write a simple program to determine if a giveb year is a leap year using user input.print

# * Leap year occurs once every four years
# * A year is a leap year if it is divisilbe by 4, but not if it is divisilbe by 100 unless it is also divisible by 400



# user input
year = int(input("Enter a year:"))

# check leap year
if (year % 4 == 0 and year % 100 !=0)or(year %400 ==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")




# Q2. Login Authentication using conditional statement. Assume you have a pre defind user name and password.print
# Write a program that prompts the user to enter a username and password and checks whether they match. Provide appropriate message for the following cases:

# * Both username and password are correct . 
# * username is corret but password is incorrect 
# * username is correct.print

predefined_username = "Laxmi"
predefined_password = "Laxmi123"

#prompts the user to enter a username and password
username = input("Enter your username:")
password = input("Enter your password:")

# username and password check and print the result
if username == predefined_username:
    if password == predefined_password:
        print("welcome login was success")
    else:
        print("Incorrect password")
else:
    print("Invalid username")


#Q3. Admission Eligibility: A university has the following eligibility criteria for admission:
# Q1. Marks in Mathematics >=55
# Q2. Marks in Physics >=55
# Q3.  Total marks in all three subject >180 OR total marks in Mathematics and physics >=140

#Write a program that marks in three sunject as input and prints wheather the student is eligible for admission.



    
# user input
print("Enter PCM marks out of 100")
physics_marks = int(input("Enter physics marks : "))
Chemistry_marks = int(input("Enter Chemistry marks : "))
Maths_marks = int(input("Enter Maths marks : "))    

# Eligibility criteria

# pyrefly: ignore[parse-error]
if (Maths_marks >=65 and
   physics_marks >=55 and                                                                                                                               
   Chemistry_marks >=50 and
   (Maths_marks + physics_marks + Chemistry_marks) >180) or \
   (Maths_marks + physics_marks) >=140:
    print("You're eligible")
else:
    print("you are not eligible for admission")

             