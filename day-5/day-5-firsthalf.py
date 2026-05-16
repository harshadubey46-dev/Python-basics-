print("----------Que-----------")
#The garments company Apparel wishes to open outlets at various locations.
#The company shortlisted several plots in these locations and wishes to select only plots that are square-shaped.
#Write an algorithm to help Apparel find the number of plots that it can select for its outlets.
#Input
#The first line of the input consists of an integer numfMots, representing the number of plots shorilisted by 
#the company for outlets (N).
#The second line consists of space-separated integers - areal, areal,,areaN representing the area of theN plots 
#selected for outlets.
#INPUT - 8
#        79 77 54 81 48 34 25 16
#OUTPUT - 3
import math
# Input
numOfPlots = int(input("Enter number of plots : "))
areas = list(map(int, input("Enter area of plots : ").split()))
count = 0
# Check for perfect square plots
for area in areas:
    root = int(math.sqrt(area))
    if root * root == area:
        count += 1
# Output
print(count)

#OR 
def isSquare(n):
    root = int(n ** 0.5)
    if root * root == n:
        return True
    else:
        return False
numOfPlots = int(input("Enter the selected plots number : "))
areas = list(map(int, input("Enter the area of plots : ").split()))
count = 0
for area in areas:
    if isSquare(area):
        count += 1
print(count)
print()

#practice questions :
def fun(value , values):
    var = 1
    values[0] = 44
t = 3
v = [1,2,3]
fun(t,v)
print(t,v[0])  # output - 3 44
print()

def f(i,values = []):
    values.append(i)
    print(values)
f(1)
f(2)
f(3) 

print("--------QUEUE IMPLEMENTATION----------")
print()

import sys
#create class
class Queue :
    #define queue size
    def __init__(self,size):
        self.myqueue = [] #create queue
        self.queuesize = size
    # Check queue empty
    def isEmpty(self):
        if len(self.myqueue) == 0:
            return True
        else:
            return False 
    #check queue is full
    def isFull(self):
        if len(self.myqueue) == size:
            return True
        else :
            return False
    #insert elements
    def enqueue(self,value):
        if self.isFull():
            print("Queue is full . Elements can't be added!")
        else:
            self.myqueue.append(value)
    #display queue
    def display(self):
        print(self.myqueue)
    #delete an element
    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            removed = self.myqueue.pop(0)
            print(removed, "deleted from queue")
    #view front and rear of queue
    def peek(self):
        if self.isEmpty():
            print("Queue is empty.")
        else :
            print("The rear is : " , self.myqueue[-1])
            print("The front is : " , self.myqueue[0])
    #delete the queue
    def deletequeue(self):
        self.myqueue.clear()
        print("Queue successfully deleted !")

size = int(input("Enter the size of the queue : "))
obj = Queue(size) #create object outside of the class
print("Stack created!")

while True :
    print("1. ENQUEUE OPERATION")
    print("2. DISPLAY QUEUE")
    print("3. DELETE OPERATION")
    print("4. PEEK OPERATION")
    print("5. DELETE QUEUE")
    print("6. EXIT")
    ch = int(input("Enter a choice : "))
    if ch == 1 :
        value = int(input("Enter the value to insert in queue : "))
        obj.enqueue(value)
    elif ch == 2 :
        obj.display()
    elif ch == 3 :
        obj.delete()
    elif ch == 4 :
        obj.peek()
    elif ch == 5 :
        obj.deletequeue()
    elif ch == 6 :
        sys.exit()
    else :
        print("Choose a valid option : ")
print()

print("------Que------")
fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else :
        fruit[index] = 1
addone('Apple')
addone('banana')
addone('apple')
print(len(fruit)) #answer 3
print()

#Write a program to accept student name and marks from the keyboard and create a dictionary . Also display 
#student marks by taking student name.
# Create empty dictionary
students = {}
n = int(input("Enter number of students: "))
# Accept student name and marks
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    students[name] = marks
# Display dictionary
print("\nStudent Dictionary:")
print(students)
# Search marks using student name
search_name = input("\nEnter student name to find marks: ")
if search_name in students:
    print(search_name, "marks are:", students[search_name])
else:
    print("Student not found")
print()

#OR
n = int(input ("Enter the number of students: ")) #2
d = {}
for i in range(n):
    name = input("Enter Student Name: ")
    marks = input ("Enter Student Marks: ") 
    d[name ]=marks # add key: value
while True:
    name = input ("Enter Student Name to get Marks: ") 
    marks = d.get(name, - 1) 
    if marks== -1:
        print ("Student Not Found")
    else:
        print ("The Marks of", name, "are",marks)
    option=input ("Do you want to find another student marks [Yes/No]")
    if option== "No":
        break
print("Thanks for using our application") 
    