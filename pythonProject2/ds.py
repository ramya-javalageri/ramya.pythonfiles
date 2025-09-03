# for i in range(10,0,-1):
#     print(i,end=' ')
# print(list(range(10)))
# for i in range(10,0,1):
#     print(i,end=' ')
# for i in {1,2,3,4}:
#     print(i)
# #LINEAR
# l=list(map(int,input('Enter a list values:').split(' ')))
# key=int(input('enter value to be find:'))
# for i in range(len(l)):
#     if l[i]==key:
#         print(f"the value is found at {i} index")
#         break
# if key not in l:
#     print('value not found')
# if i==len(l)-1 and l[i]!=key:
#     print('value not found')
# #BINARY SEARCH
# l=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('enter a value to be find:'))
# beg=0
# end=len(l)-1
# while beg<=end:
#     mid=(beg+end)//2
#     if l[mid]==k:
#         print(f"value is found at index {mid}")
#         break
#     elif l[mid]>k:
#         end=mid-1
#     else:
#         beg=mid+1
# if k not in l:
#     print('value not found')
#
# #
# def b_s(l,k):
#     beg=0
#     end=len(l)-1
#     while beg<=end:
#         mid=(beg+end)//2
#         if l[mid]==k:
#             print(f"value is found at index {mid}")
#             break
#         elif l[mid]>k:
#             end=mid-1
#         else:
#             beg=mid+1
#     if k not in l:
#         print('value not found')
# l=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('enter a value to be find:'))
# b_s(l,k)
#
# from matplotlib import pyplot
# a=[1,2,3,4,5]
# b=[2,5,4,3,6]
# pyplot.bar(a,b,width=0.25)
# pyplot.plot(a,b)
# pyplot.show()
#
# #BUBBLE SORT
# l=[2,6,7,3,8,7,1]
# print('original list:',l)
# n=len(l)
# for i in range(n):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print('sorted list:',l)
#
# #selection sort
# l=[2,7,6,3,8,1]
# print('original list:',l)
# n=len(l)
# for i in range(n):
#     min=i
#     for j in range(i+1,n):
#         if l[min]>l[j]:
#             min=j
#     l[i],l[min]=l[min],l[i]
# print('sorted list:',l)
# #INSERTION SORT
# l=list(map(int,input("enter a values:").split(' ')))
# for i in range(1,len(l)):
#     key=l[i]
#     j=i-1
#     while j>=0 and l[j]>key:
#         l[j+1],l[j]=l[j],l[j+1]
#         j=j-1
#     l[j+1]=key
# print(l)
# # MERGE SORT
def merge(lis):
    if len(lis)>1:
        mid=len(lis)//2
        left=lis[:mid]
        right=lis[mid:]
        merge(left)

        merge(right)
        l,r,k=0,0,0
        while l<len(left) and r<len(right):
            if left[l]>right[r]:
                lis[k]=right[r]
                r=r+1
            else:
                lis[k]=left[l]
                l=l+1
            k=k+1
        while l<len(left):
            lis[k]=left[l]
            l=l+1
            k=k+1

        while r<len(right):
            lis[k]=right[r]
            r=r+1
            k=k+1

l=[4,3,8,7,1,2]
print('Original list:',l)
merge(l)
print('Sorted list:',l)
# #SINGLE LINKED LIST
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class linkedlist:
#     def __init__(self):
#         self.head=None
#
#     def insert_at_end(self,data):
#         newNode=node(data)
#         if self.head is None:
#             self.head=newNode
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=newNode
#
#     def insert_at_beg(self,data):
#         newNode=node(data)
#         if self.head is None:
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode
#
#     def insert_at_position(self,data,position):
#         newNode = node(data)
#         if self.head is None:
#             self.head = newNode
#         elif position==1:
#             self.head=newNode
#         else:
#             current=self.head
#             count=0
#             while current:
#                 count+=1
#                 if count==position-1:
#                     newNode.next=current.next
#                     current.next=newNode
#                     break
#                 current=current.next
#             if count<position-1:
#                 self.insert_at_end(data)
#
#     def delete_at_beg(self):
#         if self.head is None:
#             print('no data found')
#         else:
#             self.head=self.head.next
#             self.head.next=None
#
#
#     def delete_at_end(self):
#         if self.head is None:
#             print('no data found')
#         else:
#             current=self.head
#             while current.next.next:
#                 current=current.next
#             current.next=None
#
#     def delete_by_value(self,data):
#         if self.head is None:
#             print('no data found')
#         elif self.head.data==data:
#             self.delete_at_beg()
#         else:
#             current=self.head
#             count=0
#             while current.next:
#                 if current.next.data==data:
#                     count+=1
#                     current.next=current.next.next
#                     break
#             if count==0:
#                 print('no data found')
#
#     def search_by_value(self,key):
#         if self.head is None:
#             print('no data found')
#         else:
#             current=self.head
#             count=0
#             while current:
#                 count += 1
#                 if current.data==key:
#                     #
#                     print('data is found at position',count)
#                     count =-1
#                     break
#                 current=current.next
#             if count!=-1:
#                 print('data not found')
#
#
#
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="-->")
#             current=current.next
#
#
# obj=linkedlist()
# obj.insert_at_end(5)
# obj.insert_at_beg(10)
# obj.insert_at_beg(3)
# obj.insert_at_beg(7)
# obj.display()
# obj.search_by_value(7)
#
#
#
# obj.insert_at_end(6)
# obj.insert_at_position(2,3)
# obj.delete_at_beg()
# obj.insert_at_beg(5)
# obj.delete_at_beg()
#
#
# obj.display()
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.previous=None
# class double_link_list:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def insert_at_end(self,data):
#         newNode=Node(data)
#         self.tail=newNode
#         if self.head is None:
#             self.head=newNode
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=newNode
#             newNode.previous=current
#     def insert_at_beg(self,data):
#         newNode=Node(data)
#         self.tail=newNode
#         if self.head==None:
#             self.head=newNode
#         else:
#             newNode.next=self.head
#             self.head=newNode
#             current=newNode.previous
#
#     def display_f(self):
#         current = self.head
#         while current:
#             print(current.data,end="-->")
#             current=current.next
#     def display_b(self):
#         current=self.tail
#         while current:
#             print(current.data,end='<--')
#             current=current.previous
# obj=double_link_list()
# # obj.insert_at_end(5)
# obj.insert_at_beg(1)
# # obj.insert_at_end(4)
# obj.insert_at_beg(6)
# # obj.insert_at_end(3)
# obj.display_f()
# print()
# obj.display_b()
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.previous=None
# class circular_link_lis:
#     def __init__(self):
#         self.head=None
#     def insert_end(self,data):
#         newnode=node(data)
#         if self.head==None:
#             self.head=newnode
#             newnode.next=self.head
#         else:
#             current=self.head
#             while current.next != self.head:
#                 current=current.next
#             current.next=newnode
#             newnode.next = self.head
#
#
#     def display(self):
#         current=self.head
#         print(self.head.data,end='-->')
#         current=self.head.next
#         while current!=self.head:
#             print(current.data,end='-->')
#             current=current.next
# obj=circular_link_lis()
# obj.insert_end(1)
# obj.insert_end(2)
# obj.insert_end(3)
# obj.display()
# #STACK
# class stack:
#     def __init__(self):
#         self.stack=[]
#         self.size=4
#         self.top=-1
#     def push(self,item):
#         if self.top<self.size-1:
#             self.stack.append(item)
#             self.top=self.top+1
#         else:
#             print('Overflow')
#     def pop(self):
#         if self.isEmpty():
#             print('Underflow')
#         else:
#             self.stack.pop()
#             self.top=self.top-1
#     def isEmpty(self):
#         if self.top==-1:
#             return True
#         else:
#             return  False
#
#     def display(self):
#         for i in range(len(self.stack)-1,-1,-1):
#             print(self.stack[i])
# obj=stack()
# obj.push('ramya')
# obj.push('lavanya')
# obj.push('bhanu')
# obj.push('poojitha')
# obj.push('1')
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
# obj.display()
#
#
# #QUEUE
# class queue:
#     def __init__(self):
#         self.queue=[]
#         self.size=4
#         self.front=-1
#         self.rear=-1
#     def enqueue(self,item):
#         if self.front==-1 and self.rear==-1:
#             self.queue.append(item)
#         elif self.rear<self.size-1:
#             self.queue.append(item)
#             self.rear+=1
#         else:
#             print('Queue is full')
#     def dequeue(self):
#
#         # if self.front ==-1 and self.rear==-1:
#         #     print('queue is empty')
#         # else:
#             self.queue.(self.queue.self.front)
#             self.front+=self.front
#
#     def display(self):
#         for i in self.queue:
#             print(i,end=' ')
# obj=queue()
# obj.enqueue(5)
# obj.enqueue(6)
# obj.enqueue(3)
# obj.enqueue(1)
# obj.dequeue()
# obj.dequeue()
# # obj.dequeue()
# obj.display()
##STACK USING LINKED LIST
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class stack:
#     def __init__(self):
#         self.head=None
#         self.size=4
#         self.top=-1
#     def push(self,data):
#         newnode=node(data)
#         if self.top<self.size-1:
#             self.top+=1
#             if self.head is None:
#                 self.head=newnode
#             else:
#                 newnode.next = self.head
#                 self.head = newnode
#         else:
#             print('stack is full')
#
#     def pop(self):
#         if self.head==None :
#             print('Stack is empty')
#         else:
#             self.head=self.head.next
#             self.top-=1
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end='\n')
#             current=current.next
# obj=stack()
# obj.push(5)
# obj.push(1)
# obj.push(6)
# obj.push(8)
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
#
# obj.pop()
# obj.display()

##QUEUE using linked list
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class queue:
#     def __init__(self):
#         self.head=None
#         self.size=4
#         self.front=-1
#         self.rear=-1
#     def enqueue(self,data):
#         newnode=node(data)
#         if self.front==-1 and self.rear==-1:
#             self.head=newnode
#             self.front=self.rear=0
#         elif self.rear<self.size-1:
#             self.rear+=1
#             current=self.head
#             while current.next:
#                 current=current.next
#             current=current.next
#         else:
#             print('Queue is full')
#
#     # def dequeue(self):
#     #     if self.front==-1 and self.rear==-1:
#     #         print('queue is empty')
#     #     elif self.
#
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end='\n')
#             current=self.head.next
# obj=queue()
# obj.enqueue(2)
# obj.enqueue(5)
# obj.enqueue(1)
# obj.enqueue(3)
# obj.enqueue(6)
# obj.display()

# class node:
#     def __init__(self,key):
#         self.key=key
#         self.right=None
#         self.left=None
# class B_search_tree:
#     def __init__(self):
#         self.root=None
#     def insert(self,key):
#         self.root=self.insert_recursive(self.root,key)
#     def insert_recursive(self,root,key):
#         if root is None:
#             return node(key)
#         if key<root.key:
#             root.left=self.insert_recursive(root.left,key)
#         elif  key>root.key:
#             root.right=self.insert_recursive(root.right,key)
#         return  root
#     def inorder(self,root):
#         if self.root:
#             self.inorder(self.root.left)
#             print(self.root.key)
#             self.inorder(self.root.right)
# obj=B_search_tree()
# obj.insert(8)
# # obj.insert_recursive(4)
# obj.insert(9)
# obj.insert(10)
# obj.insert(2)
# # obj.insert()
# # obj.insert()
# obj.inorder(8)




