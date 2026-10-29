# #functions in python

# #create or define function

def greetings():
    print("welcome to python tutorial by laxmi!")

# # call function (use funstion)
greetings()

# craete a function to add 2 numbers
def add2number(a,b):
    result = a+b
    print("The sun is : ", result)

# # calling this function with arguments
add2number(10, 20)


# # create a funation to add3 numbers

def add3numbers(a,b,c):
    result = a+b+c
    print("The sum of: ", result)

    # call the function with values
add3numbers(1,2,3)
add3numbers(100,200,300) 



#Function with retuen statement
def add2num(a,b):
    return(a+b)
    return(a-b)
    return(a*b)
    return(a/b)

sum2num = add2num(10,1)
print(sum2num)



# function to convert celsius to fahreneit
def celsius_to_fahreneit(celsius):
    fahrenheit = (celsius *9/5) +32
    return fahrenheit

    #call function
    temp_f = celsius_to_fahreneit(25)
    print(temp_f)