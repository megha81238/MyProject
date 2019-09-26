#insertion of element in array
from array import *
a=array('i',[2,4,6,8,3])
a.insert(2,12)
print(a)

size=int(input("enter size of array"))
arr=array('i',[])
for i in range(size):
    x=int(input("enter next value"))
    arr.append(x)
print(arr)
length=len(arr)+1
pos=int(input("enter position for inserting value"))
val=int(input("enter value for insertion"))

arr.insert(pos,val)
    
print(arr)


#delete element from array
from array import *
arr=array('i',[2,4,6,8,10])
size=5
x=int(input("enter element for deletion"))
for i in range(5):
    if arr[i]==x:
        index=i
    else:
        i+=1
for i in range(index,size-1,1):
    arr[i]=arr[i+1]
size-=1

for i in range(size):
    print(arr[i])
print(arr)
