# Find the maximum number of consecutive 1 in a binary array
arr = [1,0,0,1,1,1,0,1,1,1,1]
max_count = 0
current_count = 0
for num in arr:
    if num == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
print(max_count)
print()

#count substring in a string 
str = "abababbbab"
substring = "b"
count = str.count(substring)
print(count)
print()

print("------------While Loop------------------")
i = 1
while i<=5:
    print(i)
    i += 1

print("-------------DEF function---------------")
def hello():
    print("Hello world")
hello()
hello()
print()

def arithmatic():
    a = int(input("ENter a number :"))
    b = int(input("ENter another num :"))
    sum = a+b
    diff = a-b
    mul = a*b
    div = a/b 
    return sum , diff , mul , div 
print(arithmatic())
#or
result = arithmatic()
print(result)
print()

#How many types of arguments we pass in function ?
#1 : Positional argument
#2 : Keyword argument
#3 : Default argument
#4 : Variable length argument

def arithmatic(a,b):
    sum = a+b
    diff = a-b
    mul = a*b
    div = a/b 
    return sum , diff , mul , div 
print(arithmatic(4,4))
print()

def credential(username , password):
    if username == password :
        print("login successful")
    else:
        print("login unsuccessful")
credential(username="admin" , password="admin")
print()

def city(c="pune"):    #default city appears when no argument passed
    print(c)
city("Nagpur")
city("Raipur")
city()
print()

def city(*name):
    print(name)
city("Nagpur","delhi","pune","raipur")

#modularity approach in function 
import sys 
def add():
    a = int(input("Enter a number A: "))
    b= int(input("Enter a number B: "))
    print(a+b)
    
def sub():
    a = int(input("Enter a number A: "))
    b= int(input("Enter a number B: "))
    print(a-b)
    
def mul():
    a = int(input("Enter a number A: "))
    b= int(input("Enter a number B: "))
    print(a*b)
    
def div():
    a = int(input("Enter a number A: "))
    b= int(input("Enter a number B: "))
    print(a/b)
    
while True:
    print("1. Addition  ")
    print("2. Subtraction  ")
    print("3. Multiplication  ")
    print("4. Division  ")
    print("5. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add()
    elif choice==2:
        sub()
    elif choice ==3:
        mul()
    elif choice == 4:
        div()
    else:
        sys.exit()
print()      

print("-------------DSA START--------------------")
def findinggreatnumber(sampleArray):
    biggestnumber = sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index]>biggestnumber :
            biggestnumber = sampleArray[index]
    print(biggestnumber)
    
sampleArray = [5,3,8,0,9]
findinggreatnumber(sampleArray)   #time complexity : O(1) + O(1) + O(1) + O(1) + O(N) = O(N)
print()




