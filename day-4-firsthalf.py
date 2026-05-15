salary = int(input('enter tyour salary:'))
rating = int(input('enter your performance appraisal rating:'))
increment =0
if rating >=1 and rating<=3:
    increment = salary*10/100
elif rating>=3.1 and rating<=4:
    increment = salary*30/100
elif rating>=4.1 and rating<=5:
    increment = salary*40/100
else:
    print('invalid rating')
print('incremented salary:',increment+salary)
print()

#basic salary = 20000
#so we have to calculate the HRA of basic salary  = 20% TA = 30% DA = 45%
#calculate gross salary 
salary = 20000
da = (20000 * 45)/100
print("DA :" , da)
ta = (20000 * 30)/100
print("TA : ",ta)
hra = (20000 * 20)/100
print("HRA : " , hra)
gross = salary +hra + da + ta
print("Gross Salary : ",gross)
print()

print("----------BINARY SEARCH-------------")
def binary(array,target):
    low = 0
    high = len(array)-1
    while low <= high :
        mid = (low + high)//2
        if array[mid] == target :
            return mid
        elif array[mid] < target :
            low = mid +1 
        else :
            high = mid - 1
    return -1
array = [2,4,3,5,6,7,8,9,12,3,4,11,1,4,15,17,35,64,75,72]
target = 64
result = binary(array,target)
if result == -1 :
    print("Element not found!")
else : 
    print("Element found at : ",result)
print()

print("---------BUBBLE SORT------------")
def bubble(array):
    for i in range(len(array)-1) :
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print("Sorted array : ", array)
array = [64,34,55,22,75,90,12,4,66]
print("Given array : ",array)
bubble(array)
print()

#A company is transmiting data to another server . 
#To secure the data during transmission they plan to obtain a security key that will be sent along with the data . 
#The security key is defined as the count of repeating digit in the data . 
#Write an algorithm to find the security key for the data
newlist = [5,7,8,3,7,8,9,2,3]
mylist = []

for i in range(len(newlist)) : 
    count = 0
    key = newlist[i]
    j = i+1
    while j < len(newlist):
        if key == newlist[j]:
            mylist.append(key)
        j = j+1
print(len(mylist))

#or
def security_key(data):
    data = str(data)
    count = 0
    for i in range(len(data)):
        repeated = False
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                repeated = True
        already_counted = False
        for k in range(i):
            if data[i] == data[k]:
                already_counted = True
        if repeated and not already_counted:
            count += 1
    return count
data = 578378923
print(security_key(data))
print()