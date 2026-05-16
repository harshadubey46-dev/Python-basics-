print("------------SEARCHING--------------")
print()
print("LINEAR SEARCH")
def linearsearch(array,target):
    for i in range (0, len(array)):
        if array[i]== target:
            return i
    return -1
        
array =[1,2,3,4,6,7,9]
target = 7
result =linearsearch(array,target)
if result == -1:
    print("target value not ofund:")
else:
    print("element found at index ", result)

print("-------------------Miscellaneous------------------")
#removing spaces from the string
# rstrip - remove spaces from right hand side
# lstrip - remove spaces from left hand side
# strip - remove spaces from both sides 

city = input("Enter your city : ")
scity = city.strip()
if scity == 'Hyderabad' :
    print("Hello Hyderabad , Namaskar !")
elif scity == 'Raipur' :
    print("Au bhaiya Kaha jaat has gau !")
elif scity == 'Mathura' :
    print("Radhe Radhe !")
else :
    print("Invalid")
print()

# row wise max value :
# [[100,198,333,323],
#  [122,232,221,111],
#  [223,565,245,764]]

mylist = [
        [100,198,333,323],
        [122,232,221,111],
        [223,565,245,764]
    ]   
newlist = []
for i in range(3):
    j=0
    max = mylist[i][j]
    for j in range(4):
        c_max = mylist[i][j]
        if max < c_max :
            max = c_max
    newlist.append(max)
print(newlist)

#or 
arr = [
    [100,198,333,323],
    [122,232,221,111],
    [223,565,245,764]
]

for i in arr:
    print(max(i))
    
#input = "prashant*is*a*good*programmer"
#output = "****prashantisagoodprogrammer"

s = "prashant*is*a*good*programmer"
count = 0
word = ""
for i in s:
    if i == "*":
        count += 1
    else:
        word += i
output = "*" * count + word
print(output)

name = "prashant*is*a*good*programmer"
newname=''
val=''
for i in name:
    if i != '*':
        newname += i
    else:
        val += i
print(newname)
print(str(val+newname))

#input = "aaabbbbccceeeee"
#output = a3b4c3e5
s = "aaabbbbccceeeee"
count = {}
result = ""
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for key in count:
    result += key + str(count[key])
print(result)
