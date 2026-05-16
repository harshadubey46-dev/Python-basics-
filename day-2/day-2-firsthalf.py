print("----------------String Slicing---------------")
name = "Prashant jha"
print(name[0]) 
print(name[1])
print(name[-1])
#print(name[15])
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])
print(name[1:8:2])
print(name[::-1]) #reverse the String 

print(" ")

s="Python is a high level programming language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

print(" ")

name="Prashant"
sal = 50000
age = 28
print("{} sal is {} and age is {}".format(name,sal,age))
print("{0} sal is {1} and age is {2}".format(name,sal,age))
print("{x} sal is {y} and age is {z}".format(x=name,y=sal,z=age))
A=1
print(f"{A} is a good boy .")

print(" ")

#remove duplicates
name="Harsha"
newname=""
for i in name : 
    if i not in newname:
        newname = newname+i
        print(newname)
    
#reverse a name 
name="Harsha"
newname=""
for i in name :
    newname = i+newname
    print(newname)

name="geetu"
newname=""
for i in range(len(name)-1,-1,-1):
    newname = newname + name[i]
    print(newname)

print(" ")

#palindrome    
name = input("Enter a name : ")
if name == name[::-1]:
    print("Palindrome")
else:    
    print("Not Palindrome")
#or print(name)
#or print(name[::-1])
#or if name == name[::-1]:
#print("Palindrome")    

print(" ")
    
#consonants and vowels
name = input("Enter a name : ")
for i in name :
    if i == "i" or i == "a" or i == "e" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        print(i, " is a vowel")
    else:
        print(i, " is a consonant")
#or vowels = ["a","e","i","o","u","A","E","I","O","U"]
#name = input("Enter a name : ")
#cons=0
#vowels=0
#for i in name :
#    if i in vowels:
#        vowels += 1
#    else:
#        cons += 1  
#print("Number of vowels:", vow)
#print("Number of consonants:", cons)     

print(" ")

#check if two strings are anagram 
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
if sorted_str1 == sorted_str2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    
#count words in a string
name = "HarshaDubey"
count = 0
for i in name :
    count += 1
print(count)
  
#reverse words in a string
name = input("Enter a name : ")
newname = ""
for i in name :
    newname = i + newname
print(newname)

print("")

#BODMAS rule
a=50
b=30
c=20
d=10
print((a-b)*(c/d))
print((a+b)*(c/d))
print(a+(b*c)/d)

#determining special characters and special symbols in a string
name = input("Enter a name : ")
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
             "w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L",
             "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
count = 0
for i in name :
    if i not in alphabets and i not in digits:
        count += 1  
print("Total symbols : ", count)

#OR 

name = input("Enter a name : ")
count = 0
for i in name :
    if not i.isalnum():
        count += 1
print("Total symbols : ", count)

print("")

#title case a sentence 
name = input("Enter a sentence to title case  : ")
newname = ""
for i in range(len(name)):
    if i == 0 or name[i-1] == " ":
        newname = newname + name[i].upper()
    else:
        newname = newname + name[i].lower()
print(newname)

print(" ")
print("Prashantjha5678".isalnum())
print("Prashantjha".isalpha())
print("Prashantjha5678".isdecimal())
print("Prashantjha5678".isdigit())
print("Prashant".isidentifier())
print("Prashantjha".islower())
print(''.islower())
print("PRASHANT".isupper())
print("My Name Is Prashant".istitle())
print(''.istitle())
print(''.isspace())
print('Hello'.startswith('J'))
print('Hello'.endswith('o'))
print("Prashant".find('r'))
print("Prashant".index('r'))
print("Prashant".count('a'))

print(" ")

print("-----------Nested Loops-----------------")
# nested loop to print 
# 1  2  3
# 2
# 3
for i in range(1,4):    
    for j in range(1,4):
        print(i, end="   ")
    print()
        
n = int(input("Enter a number of rows : "))
for i in range(1,n-1):
    for j in range(1,n-1):
        print(chr(64+i), end="   ")
    print()
    
n = int(input("Enter a number of rows : "))
for i in range(1,n-1):
    for j in range(1,i+1):
        print("*", end="   ")
    print()
    
print(" ")
n = int(input("Enter a number of rows : "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*", end="   ")
    print()
    
n = int(input("Enter a number of rows : "))
for i in range(1,n+1):
    print(" "*(n-i)*3, end="")
    for j in range(1,i+1):          
        print("*", end="   ")
    for j in range(1,n+2-i):
        print("*", end="   ")
    print()
    
n = int(input("Enter a number of rows : "))
for i in range(1,n+1):
    print(" "*(n-i)*3, end="")
    for j in range(1,i+1):          
        print("*", end="   ")  
    print()
    
print(" ")

import time
n = int(input("Enter a number of rows : "))
for i in range(1,n+1):
    print(" "*(n-i), end=" ")
    for j in range(1,i+1):
        time.sleep(0.6)          
        print("*", end=" ")  
    print()
    
print(" ")
#multiply the numbers of the array but do not include the number in the index
arr = [1,2,3,4]
result = []
for i in range(len(arr)):
    product = 1
    for j in range(len(arr)):
        if i != j:
            product *= arr[j]
    result.append(product)
print(result)
