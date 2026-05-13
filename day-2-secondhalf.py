print("----------Tuple-------------")
#tuple is immutable , jab fixed data ke saath kaam karna ho tab tuple use karte hai
#tuple me duplicate value allowed hoti hai
tup1 = (1, 2, 3, 4, 5)
print(tup1)
print()

mytuple = ("apple", "banana", "cherry" , 5, 78 , 5.6 , True , 50)
print(mytuple)
print(type(mytuple))
print()

# mytuple[2]="Sunio"
# print(mytuple)

init_tuple = ()
print(init_tuple.__len__()) #O/p = 0    
print(len(init_tuple)) #O/p = 0
print()

init_tuple1 = (1, 2, 3, 4, 5)
init_tuple2 = (1, 2, 3, 4, 5)
print(init_tuple1 == init_tuple2) #O/p = True
print(init_tuple1 is init_tuple2) #O/p = True
print()

init_tuple1 = (1, 2, 3, 4, 5)
init_tuple2 = (10, 9, 7, 8, 6)
print(init_tuple1 == init_tuple2) #O/p = False
print(init_tuple1 + init_tuple2) #O/p = (1, 2, 3, 4, 5, 10, 9, 7, 8, 6)
print()

# i = [1,2,3]
# init_tuple = ('python',)* (i.__len__() - 1)
# print(init_tuple) #O/p = ('python', 'python')
# print()

init_tupleg=('python',)*3
print(type(init_tupleg)) # class tuple
print()

init_tuplex=('python')*3
print(type(init_tuplex)) # class str 
print()

# mytuple=(1,)*3
# mytuple[0]=2
# print(mytuple)   # error
# print()

# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8]))

print("----------Dictionary Datatype-----------")
#dict represented by { key:value } pair 

mydict = {
    101:"Harsha" ,
    102: "Geetu" ,
    "103 " : "Mohini" , 
    "104" : "Triveni" , 
    101 : "Aradhya" ,
    104 : "Aradhya"
}
print(mydict)

a = mydict[102]
print(a)

mydict[102] = "Peter"
print(mydict)

for x in mydict :
    print(x)  #by default it executes key reads key
    
print()

for x in mydict.values():
    print(x)    

print()

for x , y in mydict.items():
    print(x , y)

print()

mydict["mobile_no"] = 94043585750
print(mydict)

dict1 = {
    101 : "prashant" ,
    "dept" : "MCA" , 
    "id" : 102
}
dict1.pop(101)
print(dict1)

# a = ((1,2):1 , (2,3):2 , (4,5):3)   #tuple as key
# print(a[4,5]) #error

# print()

# a={'a':1 , 'b' : 2 , 'c' : 3}
# print(a['a','b'])   #keyerror

print()

arr = {}
arr[1] = 1 
arr['1'] = 2
arr[1] += 1
print(arr)
sum = 0
for k in arr :
    sum +=arr[k]
print(sum)
print()

dict2 = {}
dict2[1] = 1
dict2['1'] = 2
dict2[1.0] = 4 #it assumes 1.0 as 1 and replaces 1 by 4
print(dict2)
sum = 0
for k in dict2:
    sum += dict2[k]
print(sum)

print()
dict3 = {}
dict3[(1,2,4)] = 8
dict3[(4,2,1)] = 10
dict3[(1,2)] = 12
sum = 0
for k in dict3:
    sum += dict3[k]
print(sum)
print(dict3)
print()
 
box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
#print(len(crates['box'])) this gives keyerror
print(len(crates['box']))
print()

dictx ={ 'c' : 97 , 'a':96 , 'b':98}
for _ in sorted(dictx):
    print(dictx[_])    #alphabetically sorted that is sort by order of keys.
    
print()

rec = {"Name":"Python" , "Age":"20"}
r = rec.copy()
print(id(r) == id(rec))
print(id(r))
print(id(rec))
print()

rec = {"Name":"Python" , "Age":"20" , "Addr":"NJ" , "Country":"USA"}
id1 = id(rec)
print(id1)
del rec
rec = {"Name":"Python" , "Age":"20" , "Addr":"NJ" , "Country":"USA"}
id2 = id(rec)
print(id2)
print(id1 == id2)
print()

mydict = {"A":30 , "B":40 , "C":50 , "D":10}
max_key = None
max_value = None
for key, value in mydict.items():
    if max_value is None or value > max_value:
        max_key = key
        max_value = value

print("Maximum key:value pair :" , max_key, max_value)  # C 50
print()

mydict = {"A":30 , "B":40 , "C":50 , "D":10}
min_key = None
min_value = None
for key, value in mydict.items():
    if min_value is None or value < min_value:
        min_key = key
        min_value = value
print("Minimum Key:Value pair : " , min_key, min_value)  # D 10
print()

mydict = {"A":30 , "B":40 , "C":50 , "D":10}
print(len(mydict))
print()

data = [1, 2, 2, 4, 6, 3, 8, 3]
freq = {}
for i in data:
    freq[i] = freq.get(i , 0) + 1
print(freq)
# {1: 1, 2: 2, 4: 1, 6: 1, 3: 2, 8: 1}


print("-------------// operator--------------")
num = int(input("Enter a number to reverse : "))
a = num // 10  #12
c = a // 10 #1
b = num % 10 #3
d = a % 10 #2
rev = (b*100)+(d*10)+(c*1)
print("reversed : " , rev)

n = int(input("Enter a number : "))
a=n%10 #123456%10 = 6
b = n //10 # 12345
c=b%10 #5
d=b//10 #1234
e=d%10 #4
f=d//10 #123
g=f%10 #3
h=f//10 #12
i=h%10 #2
j=h//10 #1

rev= (a*100000)+(c*10000)+(e*1000)+(g*100)+(i*10)+(j*1)
print("reversed : " , rev)
print()

Amount = int(input("Enter an amount to withdraw : ")) #533
print("100 notes : " , Amount//100 ) #5
print("50 notes : " , (Amount%100)//50) #0
print("20 notes : " , ((Amount%100)%50)//20) #1
print("10 notes : " , (((Amount%100)%50)%20)//10) #1
print("5 notes : " , ((((Amount%100)%50)%20)%10)//5) #0
print("2 notes : " , (((((Amount%100)%50)%20)%10)%5)//2) #1
print("1 notes : " , ((((((Amount%100)%50)%20)%10)%5)%2)//1) #1


