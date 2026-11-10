# Nested Loop Syntax

#print number from 1 to 3 for 3 times
#sol1
for num in (1,4):
    print(num)

#sol2
for i in range(3):
    for num in range(1,4):
        print(num)
        print("_____")

#sol3
i = 1
while i < 4:
    for j in range (1,4):
        print(j)
        print("_______")


#Example 2
#print prime numbers between range of 2 to 10 using nested loop:

for num in range (2,10):
    for i in range (2, num):
        if num % i == 0:
            break
        else:
            print(num)

            