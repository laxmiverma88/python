# string indexing 

# postive indexing

my_name = "Laxmi"
print(my_name[0])          # first character of str
print(my_name[1])          # second character of str
print(my_name[2])          # third character of str
print(my_name[3])          #fourth character of str
print(my_name[4])          # fifth character of str

name2 = "Hello World"
print(name2[4])

name2 = "Hello World"
print(name2[5])     # sapce in string 

# negative indexing
print(name2[-1])    # last character of str 

# string slicing

my_name = "LAXMI"
# INDEX    01234
#postive
print(my_name[0:3])
print(my_name[0:3:1])
print(my_name[3:5:1])

print(my_name[-1:])# negative
print(my_name[4:])#postive
print(my_name[-2:])
print(my_name[-3])#(: & without: ([-2: & -3]))


print(my_name[0::2])      # every second char output LXM
print(my_name[::])         # All char
print(my_name[::-1])        # reverse the string


# string slicing- example 
name = "laxmi"
#01234
-4-3-2-1
name[0:1] = name[:1]
name[0:2] = name[:2]
name[0:3] = name[:3]
name[0:4] = name[:4]
name[0:5] = name[:5]

name[-1:] = name[-1:]


# string method
word = "Hello laxmi"

#1.len()
print(len(word))

#2. upper()
print(word.upper())     #upper HELLO LAXMI

#3. lower()
print(word.lower())     #lower hello laxmi

#4.COUNT()
print(word.count("a"))   #count the number of "a" in the string     

#5. find()
print(word.find('e'))

#6split()
print(word.split(','))

#7. replace()
print(word.replace("laxmi", "keshav"))

#8. title()
print(word.title())

#strip
word2 = " Hello World "
print(len(word2))
print(word.strip())

#10. join()
zwords = ("Madhav", "is", "Great")
print(" ". join(zwords))
print(" ".join(zwords))


