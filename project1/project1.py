# Write a python program to build a simple calculator

# sol . 
# pyhton program to create a simple calculator

# 3 step to build calculator program 
# 1. functions for operations
# 2. user input
# 3. print result 


# STEP 1
# 1. addition (1) : sum of multiple numbers
def add(num1, num2):
    return num1 + num2

# 2. subtraction (2): difference of two or more numbers
def sub(num1 , num2):
    return num1 - num2

# 3. multiplication (3): product of multiple numbers
def multiply(num1 , num2):
    return num1 * num2

# 4. division (4) : division of two numbers 
def divide(num1 , num2):
    return num1 / num2

# 5. average (5) : average of multiple numbers
def average(num1 , num2):
    return (num1 + num2) / 2

def average(num1 , num2, num3):
    return (num1 + num2 + num3) /3
    

# STEP2
# 2. user input
print("please select a operation: \n " \
    "1.addition \n "\
    "2. subtraction  \n "\
    "3. multiplicati \n "\
    "4.division \n " \
    "5. Average \n " )
    
select = int(input("select a opration from 1,2,3,4,5,: "))

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

# STEP3
# 3. Print result

if select == 1:
    print("The sum is : ", add(number1, number2))
elif select == 2:
    print("The difference is : ", sub(number1, number2))
elif select == 3:
    print("The product is : ", multiply(number1, number2))
elif select == 4:
    print("The division is : ", divide(number1, number2))
elif select == 5:
    print("The average is : ", average(number1, number2))
else:
    print("Invalid input")
