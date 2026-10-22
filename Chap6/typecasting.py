#casting in python

a = 1
print(type(a))

b = "1"
print(type(b))

c = int(b)
print(c)
print(type(c))

print(a+int(b))

# all str type can't be casted into numerical type
mynum = 26
mynum2 = str(mynum)
print(type(mynum2))


# float convert to int
f1 = 22.56
f2 = int(f1)
print(type(f1))
print(f2)


# int convert to float
in1 = 26
in2 = float(in1)
print(type(in2))
print(in2)


# implicit type casting
var1 = 10
var2 = 15.5
print(var1+var2)
print(type(var1+var2))

# explicit type casting
int_num = 101
str_num = str(int_num)
print(str_num)
print(type(str_num))

a0 = bool(0)
print(a0)
print(type(a0))

a1 = bool(1)
print(a1)
print(type(a1))


