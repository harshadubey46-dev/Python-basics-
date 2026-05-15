#python collection datatypes 
print("-------LIST------------------------------------------------------------------------------------------")
mylist = ["Harsha","Geetu","Sumanth","Samantha","Harshal",8,9,10]

print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[2:6:2])

mylist[3]="Aradhya"
print(mylist)

if "ankush" in mylist:
    print("Ankush is present in the list")  
else:
    print("Ankush is not present in the list")
    
mylist.append("Ankush")
mylist.append("Jay")
print(mylist)

mylist.insert(3,"Aradhya")
print(mylist)

mylist.remove("Harshal")
print(mylist)

newlist = mylist.copy()
print(newlist)

print("")

mylist = [["Harsha","Dubey"],['85','90'],['442001','yyy']]
print("Example of nested list : ")
print(mylist)
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[1][1])
print(mylist[2][0])
print(mylist[2][1])

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,"Harsha", "Geetu", "Sumanth", "Samantha", "Harshal"]
del list2[2]
#del list2
print(list2)
list2.clear()
print(list2)

#typecasting 
name = "Harsha" 
print(name)
myname=list(name)
print(myname)

mylist = name.split()
print(mylist)
print(name)

#sorting list
list1 = [5,7,33,6,11,3,9,1,4,2]
list1.sort(reverse=True) #sorts the list in descending order and default is ascending order
print(list1)

#Aliasing  
xlist = [33,55,11,77,22,44,66,88]
newlist = xlist #newlist is an alias of xlist
print(id(newlist)) #id() function returns the memory address of the object
print(id(xlist)) 

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
for i in list3:
    print(i)
    
#i/p = [0,1,4,0,2,5]
# o/p = [1,4,2,5,0,0] moving all the zeroes to the end of the list
alist = [0,1,4,0,2,5]
for i in alist:
    if i != 0:
        print(i," ")
    if i == 0:
        continue
for i in alist:
    if i == 0:
        print(i," ") 

#OR
for i in alist:
    if i==0:
        alist.remove(i)
        alist.append(i)
print(alist)

#second largest number in a list of numbers.
mylist = [3,5,9,6,0,2]
list.sort(mylist)
for i in mylist:
    print(i)
print("The second largest number is : ",mylist[-2])

a = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
a[::2] = [10, 20, 30, 40, 50]
print(a)

a= [1, 2, 3, 4, 5 ]
print(a[3:0:-1])  

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0,3): #only focused on your rows
    print(arr[i].pop())

fruitlist = ["apple","banana","grapes","orange"]
fruitlist1 = fruitlist
fruitlist2 = fruitlist[:]
fruitlist1[0] = "mango"
fruitlist2[1] = "kiwi"

sum = 0
for i in (fruitlist ,fruitlist1 ,fruitlist2):
    if i[0] =="mango":
        sum = sum + 1
    if i[1] == "kiwi":
        sum = sum + 20   
print(sum)

A=[1,2,3]
B=[2,3,4]
c=[3,4,5]

for i in A:
    if i in B and i in c:
        print(i)
        
#add the last digit of all elements of array and print the total sum of those last digits

mylist = []
total = 0
n = int(input("Enter the number of elements in the list : "))
for i in range(n):
    val = int(input("Enter the number : "))
    mylist.append(val)
print(mylist)
for i in range(n-1):
    total += abs(mylist[i] - mylist[i+1])   
print("Total : " ,total)
