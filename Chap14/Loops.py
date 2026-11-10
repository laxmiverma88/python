# Loops in python - while & for loop 
#while loop

count = 0             #Postive

while count <5:
    print(count)
    count = count +1


# sol2 - print number from 1 to 5 using while loop
count = 1

while count <6:
      print(count)
      count = count + 1


count = 5                #negative
while count >0:
    print(count)
    # count = count + 1
    count -= 1
else:
    print("while loop ended")

while True:
    print("again and again !!")


#Check Conditions to avoid infinite loop
#for loop

#for loop

language = 'python'              #Sequence

for X in language:
    print(X)


# range(stop)
for i in range(5):
    print(i)

#range(start,step)
for i in range(5,10):
    print(i)

#range(start,stop,step)
for i in range(1,10,2):
    print(i)
else:
    print("for loop ended")



#Loop Control - Pass statement
#1. pass statement

for i in range(5):
    #mann nhi hai
    pass

count = 5
while count > 0:
    if count == 3:
        pass
    else:
        print(count)
        count -= 1
        

#Loop Control - break statement
# break statement

for i in range(10):
    if i == 5:
        break
    print(i)


#Loop Control - Continue Statement
for i in range(5):
    if i == 3:
        continue
    print(i)

while True:
    user_input = input("Enter 'exit' to STOP: ")
    if user_input == 'exit':
        print("congarta! you gusses it right!")
        break
    print("Sorry, you enterd: ", user_input)
    










