# conditional statements


# 1. if statement 

a = 26
b = 108
#if condition:
# if statement works only when the condition is true
if b > a :
    print("b is greater than a")


age = 25
if age > 19:
    print("you are an adult")


age = int(input("Enter your age:"))
if age > 19:
    print("you are an adult")


# 2. if - else statement 
age = int(input("Enter your age: "))
if age >19:
    print ("you are an adult")
else:
    print("you are not an adult")
    
temp = 30
if temp < 25:
    print("it's a cool day")
else:
    print("It's a hot day")


# 3.'if-elif-else ' conditional statement 
# multiple conditons 

mark = int(input("Enter your marks - 100: "))

if mark >= 90:
    print("Grade :A+")
elif mark >= 80:
    print ("Grade: A")
elif mark >= 70:
    print ("Grade: B")
else:
    print("Grade: C")


# 4. Nested 'if - else' conditional statement 
#if-else inside if-else statement
# multiple condition depend on each other



#Q : positive, negative & zero. postive - even/odd negative number, 0- zero

number = int(input("Enter a number: "))

if number > 0:
    if number %2 == 0:
        print("This is a even number")
    else:
        print("This ia a odd number") 
else:
    if number == 0:
        print("This is zero")
    else:
        print("This is a negative number")


# 5. Conditional expressions (Ternary Operators) 

age = 26
status = "Major" if age >=18 else "Minor"
print(status)