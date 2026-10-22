# data type in python
a = 1
b = 1
#print(a)
print(a+b)
print(type(a))

c = "1"
d = "1"
print (c+d)
print(type(c))

e = "Laxmi"
f = "Verma"
print(type(e)) # checking data type : string


# basic data types in python:
# 1. numeric
a1 = 1
a2 = 1.5
print (type(a2))
a3 = complex (3,5) #1c. complex
print (type(a3))



#2. sequence
b1 = "Laxmi" # 2a. string
print(type(b1))
b2 = [1,4,7,26,108]  # 2b. list
print(type(b2))
b3 = (1,4,7,26,108)  # 2c. tuple
print(type(b3))
b4 = {1,4,7,26,108}  # 2d. set
print(type(b4))

#3. Dictionary
my_dictionary = {'name': 'Laxmi', 'age' : 26, 'city' : 'Delhi'}
print(type(my_dictionary))



#4. sets
my_sets = {1,4,7,26,108, 'Laxmi'}
print(type(my_sets))

#5. Boolean
bool1 = True
bool2 = False


#6. Binary 
# bytes, bytearray, memoryview
byte1 = b"Laxmi"
print(type(byte1))

bytearray1 = bytearray(b"Laxmi")
print(type(bytearray1))