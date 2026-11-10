#string in python

name = "Laxmi"      #creating a string
print(name)

print(type(name))     # checking data type

print("Hellow world")
print ("It's easy")

print(''' "this" is my first program ''' )  
print(" \"kw_double code\" ")
print ("kw_single code")
print ('kw_double code')    

#formatted string 
#1. old style formatting - % operator

name1 = "Laxmi"
age = 26 
print("My name is %s and I'm %d" % (name , age))
# %s, %d are placeholders for the string and int


# 2. NEW STYLE FORMATTING - .format() method 
# str.format() method

name1 = "Laxmi"
age = 26 
print("My name is {} and I'am {} year old ".format(name1, age)) 



# you can reference variables by indx or keyword
print("My name is {0} and I'm {1}year old ".format (name , age))  
print("My name is {1} and I'm {0}year old ".format (name , age))  


# print("My name is {1} and I'm {0}year old ".format (name = "hello", age = 26 ))  

#3. formatted string - f- string
# f- strings(formatted string literals)

name = "Laxmi"
age = 26
print(f"My name is {name} and I'm {age} year old ")

print (f"My age afyer 5 years will be {age + 5}")


# Escape characters in string

print("I want to go 'hyderabad'")
print(" \"Laxmi\" want to go \"hyderabad\"")
print (" \' i want to go \'hyderabad\' ")


# Python String methods
a = "Hello"
b = "python"

print(a+b)# concatenate
print (a*2) # multiple copies
print(len(a), len(b)) # length of string

