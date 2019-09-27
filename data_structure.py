#!/usr/bin/env python
# coding: utf-8

# # ARRAY

# In[33]:


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
    
    


# In[ ]:





# In[34]:


a.append(30)
print(a)


# In[10]:


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


# In[ ]:


#create array having same value in existing array
from array import *
arr=array('i',[2,3,4,5])
print(arr)
newarr=array(arr.typecode,(i for i in arr))
for val in newarr:
             print(val)
print(newarr)


# In[35]:


#traversing of an array
from array import *
size=int(input("enter size of array"))
arr=array('i',[])
for i in range(size):
    num=int(input("enter element"))
    a[i]=num
for i in range(size):
    print(a[i])
    


# # LINKED LIST

# In[50]:


class node:
    def __init__(self,data=None):
        self.data=data
        self.link=None
        

class linkedlist:
    def __init__(self):
        self.start=node()
        self.start=None
        
         
    #insertion at the end
    
    def insert(self,data):
        n=node(data)
        n.data=data
        n.link=None
        if self.start==None:
            self.start=n
        else:
            ptr=node()
            ptr=self.start
            while ptr.link!=None:
                ptr=ptr.link
            ptr.link=n
     
    #insertion at the begining
    
    def insert_beg(self,data):
        n=node(data)
        n.data=data
        n.next=None
        if self.start==None:
            self.start=n
        else:
            n.link=self.start
            self.start=n
    
    #insert element at given position
    
    def insert_bet(self,data):
        n=node(data)
        n.data=data
        n.link=None
        if self.start==None:
            self.start=n
        else:
            ele=int(input("enter the element after which data is to be inserted"))
            loc=node()
            loc=self.start
            while loc.data!=ele:
                loc=loc.link
            n.link=loc.link
            loc.link=n
    
    #deletion at the begning
    
    def delete_beg(self):
        if self.start==None:
            print("underflow")
        else:
            self.start=self.start.link
            
         
            
    #deletion at the end
    
    def delete(self):
        ptr=node()
        ptr=self.start;
        loc=node()
        
        while ptr.link!=None:
            loc=ptr
            ptr=ptr.link
        loc.link=None
            
    def show(self):
        n=node()
        n=self.start
        while n!=None:
            print(n.data)
            n=n.link
list=linkedlist()
list.insert(20)
list.insert(30)
list.insert(40)
list.insert_beg(10)
list.insert_bet(50)
list.show()
list.delete()
list.delete_beg()
print("list of element after deletion")
list.show()

        
        


# In[17]:


#reverse of linked list
class node:
    def __init__(self,val):
        self.data=val
        self.link=None
        
class linked_list:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        n=node(data);
        if self.head==None:
            self.head=n
        else:
            n.link=self.head
            self.head=n
            
    def traverse(self):
        n=self.head
        print("element of linked list")
        while n!=None:
            print(n.data,end=" ")
            n=n.link
            
    def reverse_list(self):
        
        prev=None
        temp=self.head
      
        while temp!=None:
            next_node=temp.link
            temp.link=prev
            prev=temp
            temp=next_node
            
        self.head=prev
        print("\nreverse of linked list")
        n=self.head
        while n!=None:
            print(n.data,end=" ")
            n=n.link
        
            
link=linked_list()
link.insert(30)
link.insert(20)
link.insert(10)
link.traverse()
link.reverse_list()

        
            
            
        
    


# In[3]:


#find the loop in linked list
class node:
    def __init__(self,val):
        self.data=val
        self.link=None
        
class linked_list:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        n=node(data);
        if self.head==None:
            self.head=n
        else:
            n.link=self.head
            self.head=n
            count=self.count_node()
            if count>5:
                temp=self.head
                while temp.link!=None:
                    prev=temp
                    temp=temp.link
                temp.link=prev
            
            
    def check_loop(self):
        slow=self.head
        fast=self.head
        while slow and fast and fast.link:
            slow=slow.link
            fast=fast.link.link
            if slow==fast:
                print("there exist a loop")
                return True
    def traverse(self):
        
        n=self.head
        if not self.check_loop():   
            print("element of linked list")
            while n!=None:
                print(n.data,end=" ")
                n=n.link
            
    def count_node(self):
        n=self.head
        count=0
        
        while n!=None:
            count+=1
            n=n.link
        return count
        
            
    
        
        
            
link=linked_list()
link.insert(60)
link.insert(50)
link.insert(40)
link.insert(30)
link.insert(20)
link.insert(10)


link.traverse()


         


# In[24]:


#find the miiddle element of linked list without using count
#middle can be count/2 node using count
class node:
    def __init__(self,val):
        self.data=val
        self.link=None
        
class linked_list:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        n=node(data);
        if self.head==None:
            self.head=n
        else:
            n.link=self.head
            self.head=n
            

    def traverse(self):

        n=self.head

        print("element of linked list")
        while n!=None:
            print(n.data,end=" ")
            n=n.link

    def middle_node(self):
        slow=self.head
        fast=self.head
        while fast and fast.link:
            fast=fast.link.link
            slow=slow.link
        mid=slow.data
        return slow
    
    def delete_mid(self,n):
        temp=self.head
        while temp.link!=n:
            temp=temp.link
        temp.link=n.link
            
            
    
link=linked_list()
link.insert(30)
link.insert(20)
link.insert(10)
link.insert(50)
link.insert(60)

link.traverse()
print("mid element of linked list:",link.middle_node())
print("after deletion of mid element")
link.delete_mid(link.middle_node())
link.traverse()


# In[29]:


#Delete the elements in an linked list whose sum is equal to zero
class node:
    def __init__(self,val):
        self.data=val
        self.link=None
        
class linked_list:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        n=node(data);
        if self.head==None:
            self.head=n
        else:
            n.link=self.head
            self.head=n
            

    def traverse(self):

        n=self.head

        print("element of linked list")
        while n!=None:
            print(n.data,end=" ")
            n=n.link
            
#function deleting the node whoes resultant of sum is zero 
            
    def delete_node(self):
        start=self.head
        sum=0
        while start:
            end=start.link
            modified=False
            while(end):
                sum=sum+end.data
                if sum==0:
                    start.link=end.link
                    modified=True
                    break
                end=end.link
            if(not modified):
                start=start.link

                
                
            
link=linked_list()
link.insert(-30)
link.insert(-20)
link.insert(50)
link.insert(10)
link.delete_node()

link.traverse()


# In[ ]:





# # STACK

# In[66]:


class stack:
    def __init__(self):
        self.top=-1
        self.arr=[]
 
    def isempty(self):
        return self.top==-1
            
        
    def  push(self,item):
        self.arr.append(item)
        self.top+=1
        
    def pop(self):
        if not self.isempty():
            return self.arr.pop()
            self.top-=1
            
    def show(self):
        print(self.arr)
        
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.show()
print("stack is empty:",s.isempty())
print("popped element:",s.pop())
s.show()
        
        
        
    


# # QUEUE

# In[72]:


class queue:
    def __init__(self):
        self.arr=[]
        self.front=-1
        self.rear=-1
        
    def push(self,val):
        self.arr.append(val)
        if self.rear==-1:
            self.front+=1
        self.rear+=1
        
        
    def pop(self):
        if self.front>self.rear:
            print("queue is empty")
        else:
            self.front+=1
            return self.arr.pop(0)
    
    
    def show(self):
        for i in range(len(self.arr)):
            print(self.arr[i])
q=queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.show()
print("popped element is:",q.pop())
print("popped element is:",q.pop())
print("popped element is:",q.pop())
print("popped element is:",q.pop())
print("popped element is:",q.pop())
q.show()


# # TREE

# In[28]:


class node:
    def __init__(self,val=None):
        self.data=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        
        if self.root==None:
            self.root=node(data)
        else:
            while self.root!=None:
                if data>self.root.data:
                    if self.root.right==None:
                        self.root.right=node(data)
                        break
                    else:
                        self.root=self.root.right
                        
                elif data<self.root.data:
                    if self.root.left==None:
                        self.root.left=node(data)
                        break
                    else:
                        self.root=self.root.left
                        
                else:
                    print("data is already in tree")
                    break
    
    def inorder(self,n):
        
        if n==None:
            return
        else:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)

            
b=BST()
b.insert(30)
b.insert(10)
b.insert(50)

b.inorder(b.root)
                    
            
                    
                    
            
    
        


# # SORTING and SEARCHING

# In[1]:


# implementation of bubble sort
from array import *
arr=array('i',[3,1,5,6,2,9,8,7])
print(arr)
length=len(arr)

for i in range(length-1):
    for j in range(length-1-i):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            
print("after sorting")
print(arr)

             
#time complexity is n^2 


# In[2]:


#implementation of selection sort
from array import *

def selection():
    arr=array('i',[3,1,5,6,2,9,8,7])
    print("before sorting")
    print(arr)
    length=len(arr)
    
    for i in range(length-1):
        x=min(arr)
        temp=arr[i]
        arr[i]=arr[x]
        arr[x]=temp
        
  
        
    
    
    
def min_ele(a):
    minimum=a[0]
    index=0
    for i in range(1,length-1):
        if minimum>a[i]:
            minimum=a[i]
            index=i
            break
    return index
   

selection()
print("after sort")
print(arr)      
            
 #time complexity is n^2 worst ,average and best case  


# In[4]:


#implementation of insertion sort
from array import *

def insertion_sort():
    arr=array('i',[3,1,5,6,2,9,8,7])
    print("before sorting")
    print(arr)
    length=len(arr)
    
    for i in range(1,length-1):
        for j in range(i-1,0,-1):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                
insertion_sort()
print("after sorting")
print(arr)


# In[27]:


#implementation of quick sort
from array import *
arr=array('i',[3,1,7,6,2,9,8,5])
length=len(arr);
print("before sorting")
print(arr)

def quick_sort(a,start,end):
    if start<end:
        p_index=partition(a,start,end)
        quick_sort(a,start,p_index-1)
        quick_sort(a,p_index+1,end)
        
def partition(a,start,end):
    pivot=a[end]
    pindex=start
    for i in range(end):
        if a[i]< pivot and pindex<end:
            temp=a[pindex]
            a[pindex]=a[i]
            a[i]=temp
            pindex+=1
    temp=a[end]
    a[end]=a[pindex]
    a[pindex]=temp
    
    return pindex
    
    
quick_sort(arr,0,length-1)
print("after sorting")
print(arr)  
    
    


# In[ ]:




