#Q1. Limit the decimal places to 2 digits using. format method and print, for the variable pi = 3.14159265359

pi = 3.14159265359

print(round(pi,2))

print("value of pi is {}".format(pi))

print("value of pi is {:.1f}".format(pi))

print("{:.1f}".format(pi))

#sol2 (using f-function formating float numbers)
print(f"{pi:.2f} using f-string")



#Q2.Extract characters from index 2 to 8 with a step of 2:Given my_string = "python Course" , Slice Characters From index 2 to 8, skipping every other char
my_string ="python course"

#string[ start : stop: step]

print(my_string[2:8:2])


#Q3.Slice to get only the middle character(s): for my_string = "Madhv", use slicing to Extract the middle Character(s)

my_string = "Madhav"     #6char-even
my_string = "Madhav"     #7chars-odd

def mid_str(word):
    middle =int(len(word)/2)      #3
    if len(word) % 2 == 0:
        return word[middle-1: middle+1]
    else:
        return word[middle]
print(mid_str(my_string))



#Q4. Remove the first 3 and last 3 characters: Given my_string =" Regression Analysis", remove the first 3 and last 3 characters

my_string = "Regression Analysis"
print(my_string[3:-3])           #ression Analy

#Q5. Get the substring that start 4 characters from the end to the last character: for my_string = "Classification", Slice the string starting the 4th character from the end to the last character
my_string = "classification"
print(my_string[-4:])      #tion


#Q6. How to Reverse s string using python string Method?
word = "python"
print(word[::-1])      #step value -1

#Q7 Write a python function to check if a string is a palindrome using string methods
word = "madam"
def is_palindrome(s):
    if s == s[::-1]:
       print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")

is_palindrome(word)