# Arguments in Functions

# 1. Required arguments (single/multiple arguments)

# from __unknown__ import add2number
def greetings(name ):
    print("Hello ", name, "!")

greetings("laxmi")

#greetings("Madhav"). # Madhav is argument
#greetings().         #required an argument to run code

def intro(course_name, instructor_name):
    print("welcome to ", course_name, "by", instructor_name)

intro("python", "Laxmi")


# 2. default Arguments 

def greetings(name = "delhi"):
    print("hello ", name)

    
greetings()


# 3. Keyword Arguments -  (named argument)

def divide(a,b):
    return a/b

result1 = divide(100,20)  # positional argument  
print(result1)

result2 = divide(b= 100, a = 20)  # keyword arguments
print(result2)


# Arbitrary Arguments (*args) in function

def add2number(a,b,c):
    return a+b+c 

result = add2number(10,11,12)
print(result)  

def add_number(*args):
    return sum(args)

op = add_number(1,2,3,4,5)
print(op)

def greetings(*args):
    print("hello",*args)

greetings() 

def greeting2(*name):
    for name in name:
        print(f"hello {name}")

greeting2("Laxmi", 'rishab','laxmi','madhav','nandini')


# Arbitrary Keyword Arguments (**kwargs)

def mydata(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

mydata(name = "laxmi", age = 21, course = "python")
