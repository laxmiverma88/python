# operators
#1. Arthmetic Operators

a = 5
b = 3
print(a+b)  #addition operator
print(a-b)  #subtraction operator
print(a*b)  #multiplication operator
print(a/b)  #division operator
print(a%b)  #modulo operator

# 2. comparison Operators - output is boolean value (T/F)

a = 5
b = 3
print(a > b) # greater tha operator
print(a < b) # less tha operator
print(a == b)  # equal to operator
print(a != b) # not equal to operator

# 3. Assignment Operators - 
a = 5 #assignment operators


#4. logical Operators - and , or , not
# rule
# 1. True + True = True
# 2. True + False = False
# 3. False + False = False

a = 10
b = 20
print(a>10 and b<10) #and  operator 
print(a==10 and b==20) # operator
print(a==10 or b,10) # or operator 

# Rule for 'or' operator 
# True + False= true

# 'not' operator
print(not(a==10 and b==20))


# 5. Identity operators - is , is not 
x = [1,2,3]
y = x
z = [1,2,3]

print(x is y) # is operator cheaks memory location
print(x is z)

print(x is not z) #  is not operator

# 6. Membership operators - in , not in 
my_list = ['apple', 'banana', 'cherry']

print('apple' in my_list) # in operator     
print ('apple' in my_list)
print('apple' not in my_list) # not in operator 

# 7. bitwise operator  - and & , or |, xor,^ not ~, etc
a = 5  # 101 in binary
b = 3  # 011 in binary
print (a & b)  # 1 in binary
print (a | b)  # 7 in binary
print (a ^ b)  # 6 in binary
print (~a)    # -6  
