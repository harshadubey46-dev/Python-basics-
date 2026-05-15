#why is python is dynamically typed language ? 
#Usses both compiler and interpreter and is a two state system ,write once read anywhere ; 
#whenever we provide a value we do not assign a datatype it is decided by python interpreter .
age = 22
pi = 3.14
name = "Harsha"
result = True
print(type(age))
print(type(pi))
print(type(name))
print(type(result))

print("----------------DATATYPES-----------------------------------------------------------------------------------------------------------------------")

#why all predefined dATAtypes are IMMUTABLE(non-changeable) in python ?
#because we cannot change the value of a variable once it is assigned ,
#we can only reassign a new value to the variable but we cannot change the value of the variable itself .
math = 50
chem = 50
phy = 50
print(id(math))
print(id(chem))
print(id(phy))

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

print(2+2)
print("2"+"2")
a = input("Enter a number: ")
b = input("Enter another number: ")
print(a+b) #it will concatenate the two strings because input() function returns a string by default
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))    
print(a+b) #it will add the two numbers because we have converted the input to integers using int() function

print("---------------------TYPECASTING------------------------------------------------------------------------------------------------------------------")

#typecasting is the process of converting one data type to another data type .
#we can use the built-in functions like int(), float(), str() to convert the data types .
print(int(3.14))
#print(int(10+5j))
print(int(True)) 
print(int(False)) 
print(int(4))
print(int(4.22))
#print(int("Prashant"))

print(float(3.14))
#print(float(10+5j))
print(float(True)) 
print(float(False)) 
print(float(4))
print(float(4.22))
#print(float("Prashant"))

#complex typecasting is not possible for all data types ,it is only possible for int, float and bool data types .
#complex() function takes two arguments real and imag ,if we provide only one argument it will be considered as 
#real part and imaginary part will be 0 by default .
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex(5))
print(complex(5.6))
#print(complex("Prashant"))
print(complex(5,-3))
print(complex(True,False))

#bool typecasting is the process of converting a value to a boolean value (True or False) based on its truthiness.
print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(""))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(True))
print(bool(False))

print("----------------IF , IF_ELSE , IF_ELIF_ELSE---------------------------------------------------------------------------------------------------------------------")

#simple if statement
x=int(input("Enter a number: "))
if x<0:
    print("x is negative")
if x>0:
    print("x is positive")  
if x==0:
    print("x is zero")    
print("")

a = input("Enter a Day: ")
if a=="Saturday" or a=="Sunday" or a=="saturday" or a=="sunday" or a=="SATURDAY" or a=="SUNDAY" or a=="Sat" or a=="Sun" or a=="sat" or a=="sun" or a=="SAT" or a=="SUN":
    print("It is a weekend")
else:
    print("It is a weekday")

per = 45
if per>=80:
    print("Grade A")
elif per<=70 and per>=50:
    print("Grade B")
elif per<50 and per>=35:
    print("Grade C")
else:
    print("Fail")

#ord function is used to get the ASCII value of a character and chr function is used to get the character from the ASCII value .   
chr=ord(input("Enter a character: "))
if chr>=65 and chr<=90:
    print("It is an uppercase letter.")
elif chr>=97 and chr<=122:
    print("It is a lowercase letter.")
elif chr>=48 and chr<=57:
    print("It is a digit.")
else:
    print("It is a special character.")    

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

#in and not in operators are used to check if a value is present in a sequence (list, tuple, string) or not .
name = "Harsha"
print("H" in name)
print("Q" in name)
print("r" not in name)
print("")

#is and is not operators are used to check if two variables refer to the same object in memory or not (address comparison).
math = 50
chem = 50
print(math is chem)
print(math is not chem)
print("")

#for loop 
for i in range(5): #until 5 (0,1,2,3,4)
    print(i)
print("")    
for i in range(2,10): #from 2 to 9 (2,3,4,5,6,7,8,9)
    print(i)
print("")   
for i in range(1,10,2): #from 1 to 9 with a difference of 2 (1,3,5,7,9)
    print(i)
print("")    
for i in range(5,0,-1): #from 5 to 1 with a difference of -1 (5,4,3,2,1)
    print(i)
print("")

print("2" + "  " + "3" + "  " + "4" + "  " + "5" + "  " + "6" + "  " + "7" + "  " + "8" + "  " + "9" + "  " + "10")
for i in range(1,11):
    print(i*2 , "  " , i*3 , "  " , i*4 , "  " , i*5 , "  " , i*6 , "  " , i*7 , "  " , i*8 , "  " , i*9 , "  " , i*10)

print("-----------------------------------------------------------------------------------------------------------------------------------------")

print("11" + "  " + "12" + "  " + "13" + "  " + "14" + "  " + "15" + "  " + "16" + "  " + "17" + "  " + "18" + "  " + "19" + "  " + "20")
for i in range(1,11):
    print(i*11 , "  " , i*12 , "  " , i*13 , "  " , i*14 , "  " , i*15 , "  " , i*16 , "  " , i*17 , "  " , i*18 , "  " , i*19 , "  " , i*20)
print("")

#write a progrAM to print paper marks and calculate total percentage and check if he/she has passed all the subjects so print pass or fail .
#if percentage is greater than 65 and gender = male so it is elligible for placement or else not elligible .
maths = int(input("Enter marks for maths : "))
chem = int(input("ENter marks for chemistry :"))
phy = int(input("Enter marks for physics : "))
total = maths + chem + phy 
percentage = (total / 150) * 100
 
print("Total marks : " , total)
if total >= 100 and maths >= 30 and chem >= 30 and phy >= 30 : 
    print("Pass")
else:
    print("Fail")
    
print("Percentage : " , percentage)
gender = input("Enter gender (M/F): ")
if percentage >= 65 and gender == "M" :
    print("Elligible for placement")
else :
    print("Not elligible")  
    
print("")  

for i in range(1,5):
    if i == 3:
        break
    print(i)
print("")

for i in range(1,5):
    if i == 3:
        continue
    print(i)
print("")

#zip function is used to combine two or more iterables (list, tuple, string) into a single iterable of tuples.
a = [1,2,3,4,5]     
b = [5,4,3,2,1]
for i,j in zip(a,b):
    print(i , "  " , j)

print("")

#give thebelow ouput :    
#1   5
#2   4
#4   2
#5   1
for i,j in zip(range(1,6), range(5,0,-1)):
    if i == 3:
        continue
    print(i,"  ",j)

