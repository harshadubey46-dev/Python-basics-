print("--------------CLASS and OBJECT------------------")
class name :
    age = 30
    def display(self):
        print("Hello World!")
obj = name()
print(obj.age)
obj.display()
print()
#Classes and Objects
class student :
    def __init__(self):
        self.name="Harsha"
        self.age = 24        
    def display1(self):
        print("Name : " , self.name)
        print("Age : ",self.age)
sobj = student()
sobj.display1()
print(sobj)
print()

#constructor
class message :
    def __init__(self):
        print("Hello this is a class")
    def show(self):
        print("Class program")
mobj = message()
mobj.show()
m1obj = message()
print()

#parameterized Constructor
class studentinfo :
    def __init__(self,name1,age,roll):
        self.name1 = name1
        self.age = age 
        self.roll = roll
    def dis(self):
        print("Name : ",self.name1)
        print("Age : ",self.age)
        print("Roll No. : ",self.roll)
studentobj = studentinfo("Harsha",24,14)
studentobj.dis()
print()

print("-----------STACK IMPLEMENTATION--------------")
#STACK IMPLEMENTATION WITHOUT LIMIT
# import sys
# class Stack:
#     def __init__(self):
#         self.mystack = []
#     def push(self, value):
#         self.mystack.append(value)
#         print("Element pushed to stack.")
#     def pop(self):
#         if len(self.mystack) == 0:
#             print("Stack is empty.")
#         else:
#             removed = self.mystack.pop()
#             print("Popped element is:", removed)
#     def display(self):
#         print("Stack elements are:", self.mystack)
#     def peek(self):
#         if len(self.mystack) == 0:
#             print("Stack is empty.")
#         else:
#             print("Top element is:", self.mystack[-1])
#     def deletestack(self):
#         self.mystack = None 
            
# obj3 = Stack()
# print("Stack has been created")

# while True:
#     print("\n1. PUSH OPERATION")
#     print("2. POP OPERATION")
#     print("3. DISPLAY STACK")
#     print("4. PEEK OPERATION ")
#     print("5. DELETE STACK")
#     print("6.EXIT")
#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#         value = int(input("Enter a value to push into stack: "))
#         obj3.push(value)
#     elif ch == 2:
#         obj3.pop()
#     elif ch == 3:
#         obj3.display()
#     elif ch == 4:
#         obj3.peek()
#     elif ch == 5 :
#         obj3.deletestack()
#     elif ch == 6:
#         sys.exit()
#     else:
#         print("Invalid choice.")

#STACK IMPLEMENTATION WITH LIMIT     
# import sys
# class Stack:
#     def __init__(self, size):
#         self.mystack = []
#         self.stacksize = size
#     # Check if stack is full
#     def isFull(self):
#         if len(self.mystack) == self.stacksize:
#             return True
#         else:
#             return False
#     # Check if stack is empty
#     def isEmpty(self):
#         if len(self.mystack) == 0:
#             return True
#         else:
#             return False
#     # Push operation
#     def push(self, value):
#         if self.isFull():
#             print("Stack is Full!!")
#         else:
#             self.mystack.append(value)
#             print("Element pushed to stack.")
#     # Pop operation
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty.")
#         else:
#             removed = self.mystack.pop()
#             print("Popped element is:", removed)
#     # Display stack
#     def display(self):
#         print("Stack elements are:", self.mystack)
#     # Peek operation
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty.")
#         else:
#             print("Top element is:", self.mystack[-1])
#     # Delete stack
#     def deletestack(self):
#         self.mystack = None
#         print("Stack deleted successfully.")

# # Main Program
# size = int(input("Enter size of the stack: "))
# obj3 = Stack(size)
# print("Stack has been created")

# while True:
#     print("\n1. PUSH OPERATION")
#     print("2. POP OPERATION")
#     print("3. PEEK OPERATION")
#     print("4. IsEmpty")
#     print("5. IsFull")
#     print("6. DELETE STACK")
#     print("7. DISPLAY STACK")
#     print("8. EXIT")
#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#         value = int(input("Enter a value to push into stack: "))
#         obj3.push(value)
#     elif ch == 2:
#         obj3.pop()
#     elif ch == 3:
#         obj3.peek()
#     elif ch == 4:
#         if obj3.isEmpty():
#             print("Stack is Empty.")
#         else:
#             print("Stack is Not Empty.")
#     elif ch == 5:
#         if obj3.isFull():
#             print("Stack is Full.")
#         else:
#             print("Stack is Not Full.")
#     elif ch == 6:
#         obj3.deletestack()
#     elif ch == 7:
#         obj3.display()
#     elif ch == 8:
#         sys.exit()
#     else:
#         print("Invalid choice.")

print()
print("-----Que-----")
#company wishes to encodes its dala. 
#The data Is in the form of a number They wish to encode the data with respect to a specific digit. 
#They wish to count the number of times the specific digit reoccurs in the given data so that they can 
#encode the data accordingly. Write an algorithm to find the count of the specific digit in the given data.
#Input
#The input consists of two space-separated integers- data and digít, representing the data to be encoded and 
#the digit to be counted in the data.
#Output
#Print an integer representing the courbof the specilic digit.

data = int(input("Enter data : "))
digit = int(input("Enter digit : "))
count = 0
while data > 0:
    rem = data % 10
    if rem == digit:
        count += 1
    data = data // 10
print(count)
