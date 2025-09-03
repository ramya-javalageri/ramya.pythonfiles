#......................................stack using list.....................
# stack=[]
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)
# print(stack.pop())
# print(stack.pop())
# # print(stack.pop())
# print(stack)
# print(stack[-1])
# print(len(stack)==0)

# .................stack using class and object........
# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,item):
#         return self.items.append(item)
#     def pop(self):
#         if len(self.items)==0:
#             return "Stack is empty"
#         else:
#             return self.items.pop()
#     def is_empty(self):
#         return len(self.items)==0
#     def size(self):
#         return len(self.items)
#     def peek(self):
#         if self.items:
#             return self.items[-1]
#         else:
#             return "Stack is empty"
#     def __str__(self):
#         return str(self.items)
# s=Stack()
# s.push(1)
# print(s)
# s.push(2)
# print(s)
# s.push(3)
# print(s)
# print(s.is_empty())
# print(s.peek())
# print(s.size())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s)


# .....................
class Stack:
    def _init_(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return ("Stack is empty")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def _str_(self):
        return str(self.items)
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack)
# # Pop elements from the stack
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())
# print(stack)
# print(stack.is_empty())
# try:
#     stack.pop()
# except IndexError as e:
#print(e)

# ................................queue........
# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         else:
#             return "Queue is empty"
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size(self):
#         return len(self.items)
#
#     def print_queue(self):
#         print(self.items)
#
#     def peek(self):
#         return self.items[0]
#
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.print_queue()
# print(q.peek())
# print(q.dequeue())
# q.print_queue()
# print("size of queue is",q.size())

# .................................valid or invalid parenthasis........................
# class Stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,item):
#         return self.items.append(item)
#     def pop(self):
#         if len(self.items)==0:
#             return "Stack is empty"
#         else:
#             return self.items.pop()
#     def peek(self):
#         if self.items:
#             return self.items[-1]
#         else:
#             return "Stack is empty"
#     def display(self):
#         if self.items==[]:
#             return "Valid parenthasis"
#         else:
#             return "Invalid parenthesis"
# ip="({[][]})"
# stack=Stack()
# for i in ip:
#     if i=='(' or i=='[' or i=='{':
#         stack.push(i)
#     else:
#         if i=='}' and stack.peek()=='{' or i==']' and stack.peek()=='[' or i==')' and stack.peek()=='(':
#             stack.pop()
#         else:
#             stack.push(i)
# print(stack.display())


# ...............................................single linked list........................
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class Linkedlist:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
#     def insert_at_end(self,value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1
#
#
#     def print_list(self):
#         temp=self.head
#         while temp is not None:
#             print("{",f"{temp.value}:{temp.next}", end="},")
#             temp=temp.next
#         print()
#
#     def update(self,prevalue,newvalue):
#         temp=self.head
#         while temp is not None:
#             if temp.value==prevalue:
#                 temp.value=newvalue
#                 return "updated"
#                 break
#             temp=temp.next
#         return "not present"
#     # def pop_at_end(self):
#
#     def insert_at_beg(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#         self.length+=1
#     def pop_at_beg(self):
#         if self.length==0:
#             return None
#         temp=self.head
#         self.head=self.head.next
#         temp.next= None
#         self.length-=1
#         if self.length==0:
#             self.tail=None
#         return temp
#
#     def pop_at_end(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         pre = self.head
#         while (temp.next):  # 1 2 3
#             pre = temp
#             temp = temp.next
#         self.tail = pre
#         self.tail.next = None
#         self.length -= 1
#         if self.length == 0:
#             self.head = None
#             self.tail = None
#         return temp
#
#     def insert_at_position(self,index,value):
#         if index<0 or index>=self.length:
#             return False
#         if index==0:
#             return self.insert_at_beg(value)
#         newNode=Node(value)
#         temp=self.get(index-1)
#         newNode.next=temp.next
#         temp.next=newNode
#         self.length+=1
#         return True
#
#     def pop_at_position(self,index):
#         if index < 0 or index >= self.length:
#             return False
#         if index == 0:
#             return self.pop_at_beg()
#         if index==self.length-1:
#             return self.pop_at_end()
#         pre=self.get(index-1)
#         temp=pre.next
#         pre.next=temp.next
#         temp.next=None
#         self.length-=1
#         return temp
#
#     def get(self,index):
#         if index<0 or index>=self.length:
#             return None
#         temp=self.head
#         for _ in range(index):
#             temp=temp.next
#         return temp
#
# sll=Linkedlist(300)
# sll.insert_at_end(500)
# sll.insert_at_beg(200)
# sll.insert_at_beg(100)
# sll.print_list()
# sll.insert_at_position(3,400)
# print(sll.update(200,2000))
# print(sll.update(100,1000))
# sll.print_list()
# sll.pop_at_beg()
# sll.pop_at_end()
# sll.print_list()
# print(sll.get(1))
# sll.pop_at_position(1)
# sll.pop_at_position(0)
# sll.print_list()
# print(f"Head value:{sll.head.value}")
# print(f"tail value:{sll.tail.value}")
# print(f"Head next:{sll.head.next}")
# print(f"Tail next:{sll.tail.next}")
# print(f"Length:{sll.length}")


# ................................................................
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class Ll:
#     def __init__(self, value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1
#
#     def insert_at_end(self, value):
#         new_node=Node(value)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=new_node
#         self.length+=1
#
#     def sum(self):
#         temp=self.head
#         s=0
#         while temp is not None:
#             s+=temp.value
#             temp=temp.next
#         return s
#
#     def max_v(self):
#         temp=self.head
#         m=temp.value
#         while temp is not None:
#             if temp.value>m:
#                 m=temp.value
#             temp=temp.next
#         return m
#
#     def min_v(self):
#         temp=self.head
#         m=temp.value
#         while temp is not None:
#             if temp.value<m:
#                 m=temp.value
#             temp=temp.next
    #     return m
    # def print_list(self):
    #     temp=self.head
    #     while temp is not None:
    #         print("{",f"{temp.value}:{temp.next}", end="},")
    #         temp=temp.next
    #     print()

#     def mid_val(self):
#         if self.length==0:
#             return None
#         temp=self.head
#         mid=self.length//2
#         for _ in range(mid):
#             temp=temp.next
#         return temp.value
#
# sll=Ll(100)
# # sll.insert_at_end(110)
# sll.insert_at_end(120)
# sll.insert_at_end(130)
# sll.insert_at_end(140)
# sll.insert_at_end(150)
# sll.insert_at_end(160)
# print(sll.length)
# print(f'mid value is:{sll.mid_val()}')
# sll.print_list()
# print(f'sum={sll.sum()}')
# print(f'max value:{sll.max_v()}')
# print(f'min value:{sll.min_v()}')


# ................................double linked list...........
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
#         self.pre=None
#
# class Doublelinkedlist:
#     def __init__(self,value):
#         newnode=Node(value)
#         self.head=newnode
#         self.tail=newnode
#         self.length=1
#
#     def insert_at_beg(self,value):
#         newnode=Node(value)
#         if self.length==0:
#             self.head=newnode
#             self.tail=newnode
#         else:
#             newnode.next=self.head
#             self.head.pre=newnode
#             self.head=newnode
#         self.length+=1
#         return True
#     def insert_at_end(self,value):
#         newnode = Node(value)
#         if self.head is None:
#             self.head=newnode
#             self.tail=newnode
#         else:
#             self.tail.next=newnode
#             newnode.pre=self.tail
#             self.tail=newnode
#         self.length+=1
#         return True
#     def insert_at_position(self,index,value):
#         if index<0 or index>self.length:
#             return False
#         if index==0:
#             return self.insert_at_beg()
#         if index==self.length:
#             return self.insert_at_end()
#         newnode=Node(value)
#         before=self.get(index-1)
#         after=before.next
#         newnode.pre=before
#         newnode.next=after
#         before.next=newnode
#         after.pre=newnode
#         self.length+=1
#         return True
#
#     def get(self,index):
#         if index<0 or index>=self.length:
#             return None
#         temp=self.head
#         if index<self.length/2:
#             for _ in range(index):
#                 temp=temp.next
#         else:
#             temp=self.tail
#             for _ in range(self.length-1,index,-1):
#                 temp=temp.pre
#         return temp
#     def print_li(self):
#         temp=self.head
#         while temp is not None:
#             print("{",f"{temp.pre}:{temp.value}:{temp.next}",end='}')
#             temp=temp.next
#         print()
#
# dll=Doublelinkedlist(4)
# dll.insert_at_beg(2)
# dll.insert_at_beg(1)
# dll.insert_at_end(5)
# dll.insert_at_end(6)
# dll.insert_at_beg(0)
# dll.insert_at_position(3,3)
# print(dll.get(2))
# dll.print_li()

# .................................double.............
# class Node:
#     def _init_(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class DoublyLinkedList:
#     def _init_(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def print_list(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node
#         self.length += 1
#         return True
#
#     def pop(self):
#         if self.length == 0:
#             return None
#         temp = self.tail
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             temp.prev = None
#         self.length -= 1
#         return temp
#
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.length += 1
#         return True
#
#     def pop_first(self):
#         if self.length == 0:
#             return None
#         temp = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.prev = None
#             temp.next = None
#         self.length -= 1
#         return temp
#
#     def get(self, index):
#         if index < 0 or index >= self.length:
#             return None
#         temp = self.head
#         if index < self.length / 2:
#             for _ in range(index):
#                 temp = temp.next
#         else:
#             temp = self.tail
#             for _ in range(self.length - 1, index, -1):
#                 temp = temp.prev
#         return temp
#
#     def set_value(self, index, value):
#         temp = self.get(index)
#         if temp:
#             temp.value = value
#             return True
#         return False
#
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False
#         if index == 0:
#             return self.prepend(value)
#         if index == self.length:
#             return self.append(value)
#
#         new_node = Node(value)
#         before = self.get(index - 1)
#         after = before.next
#
#         new_node.prev = before
#         new_node.next = after
#         before.next = new_node
#         after.prev = new_node
#
#         self.length += 1
#         return True
#
#
# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(3)
#
# print('DLL before insert():')
# my_doubly_linked_list.print_list()
#
# my_doubly_linked_list.insert(1, 2)
#
# print('\nDLL after insert(2) in middle:')
# my_doubly_linked_list.print_list()
#
# my_doubly_linked_list.insert(0, 0)
#
# print('\nDLL after insert(0) at beginning:')
# my_doubly_linked_list.print_list()
#
# my_doubly_linked_list.insert(4, 4)
#
# print('\nDLL after insert(4) at end:')
# my_doubly_linked_list.print_list()

# ...............................circular.............
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        if not self.head:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                return False

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")


csll = CircularSinglyLinkedList()
csll.insert(10)
csll.insert(20)
csll.insert(30)
csll.display()
print("Search 20:", csll.search(20))
csll.display()
