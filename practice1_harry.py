# # ............speech program............
# import pyttsx3
# engine=pyttsx3.init()
# engine.say(" I am ramya")
# engine.runAndWait()

# # .............strings..............
# n=input()
# print(n+" Good afternoon")


# # ..............letter.....
# name=input()
# Date=input()
# print('Dear '+name+'\nYou are selected!\n' +Date)

# # .......detect space.......
# name=input()
# n=name.find("  ")
# print(n)

# # ...........replace......
# name=input()
# n=name.replace("  "," ")
# print(n)

# # ...........using escape.......
# print('\"','Dear harry,this python course is nice.Thanks!','\"')

# # ...................list and tuples............
# # ...........store..............
# fruits=[]
# for i in range(int(input())):
#     fruits.append(input())
# print(fruits)
# f=[]
# n=int(input("enter len:"))
# for i in range(n):
#     l=input("enter a fruit:")
#     f.append(l)
# print(f)


# # ...............sort.....
# m=[]
# n=int(input("enter len:"))
# for i in range(n):
#     l=input("enter the marks:")
#     m.append(l)
# print(m)
# m.sort()
# print(m)

# # ...............4th question.........
# m=[]
# n=int(input("enter len:"))
# for i in range(n):
#     l=int(input("enter the marks:"))
#     m.append(l)
# print(sum(m))

# # .................count.......
# n=(1,2,3,0,3,0,1,0,0)
# print(n.count(0))
# f=list(input().split())
# print(f)


# # .....................Dictnory and sets............
# # .......1
# t={'one':1,'two':2,'three':3}
# l=t.get(input())
# print(l)


# # ............2......
# s=set(input().split())
# print(s)

# s=set()
# for i in range(int(input())):
#     s.add(input())
# print(s)

# # .......................
# dic={}
# # for i in range(int(input()))
# for i in range(int(input("enter a len:"))):
#     k=input("enter a name:")
#     v=input("enter a lang:")
#     dic.update({k:v})
# print(dic)

# # .....................if statements......

# # .........1.........
# lis=[5,4,3,1]
# #print(max(lis))
# if lis[0]>lis[1] and lis[0]>lis[2] and lis[0]>lis[3]:
#     g=lis[0]
# elif lis[1]>lis[0] and lis[1]>lis[2] and lis[1]>lis[3]:
#     g=lis[1]
# elif lis[2] > lis[0] and lis[2] > lis[1] and lis[2] > lis[3]:
#     g = lis[2]
# else:
#     g=lis[3]
# print(g)

# # ..............2..
# s1=int(input("Enter s1:"))
# s2=int(input("Enter s2:"))
# s3=int(input("Enter s3:"))
# s1_p=int((s1/100)*100)
# s2_p=int((s2/100)*100)
# s3_p=int((s3/100)*100)
# t_p=int(((s1+s2+s3)/300)*100)
# if (t_p>44) and (s1_p>=33) and (s2_p>=33) and (s3_p>=33):
#     print("Pass")
# else:
#     print("fail")

# # .............3..........
# input_msg=input("Enter a message:")
# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"
# # msg_s=str(msg)
# if p1.lower() or p2.lower() or p3.lower() or p4.lower() in input_msg.lower():
#     print("Spam message")
# else:
#     print("Not a spam")
# if msg=="Make a lot of money":
#     print(msg," is spam")
# elif msg=="buy now":
#     print(msg," is spam")
# elif msg=="subscribe this":
#     print(msg," is spam")
# elif msg=="click this":
#     print(msg," is spam")
# else:
#     print(msg," is not "spam")

# # ............4.............
# w=input("Enter a word:")
# if len(w)==10:
#     print(w," have 10 characters")
# else:
#     print(w," does not have 10 characters")

# # ...........5.............
# l=['ramya','lav','bhanu','poojitha']
# l1=str(l)
# n=input("enter a name:")
# if n.lower() in l1.lower():
#     print(n," is present in given list")
# else:
#     print(n, " is not present in given list")

# # ................6.............
# s1=int(input("Enter s1:"))
# s2=int(input("Enter s2:"))
# s3=int(input("Enter s3:"))
# t_p=int(((s1+s2+s3)/300)*100)
# print(t_p)
# if t_p<=100 and t_p>90:
#     print("Ex")
# elif t_p<=90 and t_p>80:
#     print("A")
# elif t_p<=80 and t_p>70:
#     print("B")
# elif t_p<=70 and t_p>60:
#     print("C")
# elif t_p<=60 and t_p>50:
#     print("D")
# else:
#     print("Fail")

# # .........7.....
# post=input("Enter a msg:")
# n=input()
# if n.lower() in post.lower():
#     print("post is talking about", n.lower())
# else:
#     print("not talking about ",n.lower())

# # .................conditional satements................

# # .......1.............
# n=int(input("Enter a number:"))
# for i in range(1,10):
#     print(i*n)

# # .......2.........
# l=['ramya','lav','bhanu','poojitha','rfgvyg']
# for i in l:
#     if i.startswith('r'):
#         print(i,"welcome")

# # .........3...........
# n=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1

# # .........4...........
# n=int(input("Enter a number:"))
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         print("not a prime number")
#         break
# else:
#     print(n, "is prime number")

# # ..........5.........
# n=int(input("Enter a number:"))
# s=0
# i=1
# while i<n+1:
#     s+=i
#     i+=1
# print(s)

# # ..........6.........
# fact=1
# for i in range(1,int(input("Enter a number:"))+1):
#     fact*=i
# print(fact)

# # ..........8..........
# n=int(input("Enter  a number:"))
# for i in range(1,n+1):
#     print("*"*i)

# # ................7..............
# n=int(input())
# for i in range(n):
#     for j in range(n,i+1,-1):
#         print(' ',end='')
#     for k in range(0,i+1):
#         print('*',end='')
#     for l in range(1,i+1):
#         print('*',end='')
#     print()

# # .............9........
# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print('* '*n)
#         # print()
#     else:
#         print('* ','  '*(n-3),'*')

# # ...........10..
# n=int(input())
# for i in range(10,0,-1):
#     print(i*n)

# dic={}
# for i in range(2):
#     # k=input("enter key")
#     # v=input("enter value")
#     k,v=map(str,input().split())
#     dic.update({k:v})
# print(dic)

# # ..................fuctions and recursion
# # ............1........
# def greatest():
#     a=int(input())
#     b=int(input())
#     c=int(input())
#     if a>=b and a>=c:
#         print(a,"is greater")
#     elif b>=a and b>=c:
#         print(b,"is greater")
#     else:
#         print(c,"is greater")
# greatest()
# def greater():
#     l=list(map(int,input().split()))
#     return max(l)
# print(greater())

# # .............2.......
# def convert(c):
#     f=(c*(9/5)+32)
#     return f
# print(convert(int(input("Enter celcius value:"))))
# # .............4.............
# def summy(n):
#     if n==1:
#         return 1
#     return n+summy(n-1)
# print(summy(int(input("enter a num:"))))

# # .......5.........
# def pattern(n):
#     for i in range(n,0,-1):
#         print('*'*i,end=" ")
#         print()
# pattern(int(input()))

# # ........6.......
# def convert(i):
#     return 2.54*i
# print(convert(int(input("enter inch:"))))

# # ........7.......
# def word(n):

#     l.remove(n)
#     print(l)
# l=list(map(str,input().split()))
# word(input("Enter a word").lower())

# # .......8.....
# def mul(n):
#     for i in range(1,11):
#         print(f'{n}*{i}={n*i}')
# mul(int(input("Enter:")))

# # ..........
# def strip_w(l,w):
#     n=[]
#     for i in l:
#         if not(i==w):
#             n.append(i.rstrip(w))
#     return n
# l=['harryar','ramya','lav','ar']
# print(strip_w(l,'ar'))

# # ......................Files..........................
# # ..............1............
# f=open("poems.txt","w")
# f.write("Twinkle twinkle little star")
# with open("poems.txt",'r') as f:
#     # print(f.read())
#     if "twinkle" in f.read():
#         print("present")
#     else:
#         print("not present ")

# # .........3..............
# f=open('table.txt','w')
# # n=int(input())
# for j in range(2,21):
#     for i in range(1,11):
#         f.write(f'{j}*{i}={j*i}\n')
#     # print(end=" ")
# f.close()

# # ............4............
# st="donkey".lower()
# with open('donkey.txt','r') as f:
#     c=f.read()
#     print(c)
# nc=c.replace(st,'##')
# with open('donkey.txt','w') as f:
#     f.write(nc)


# # .................5......
# w=['monkey','donkey','dog']
# with open('censor.txt','r') as f:
#     c=f.read()
# for i in w:
#     c=c.replace(i,'*'*len(i))
# with open('censor.txt','w') as f:
#     f.write(c)


# # .............
# st="Hello donkey,how  are you Donkey".lower()
# f=open('c1.txt','w')
# f.write(st)
# f.close()

# # ...........3........
# def genearte_table(n):
#     table=''
#     for i in range(1,11):
#         table+=f'{n}*{i}={n*i}\n'
#     with open(f'table1/table_{n}.txt','w') as f:
#         f.write(table)
# for i in range(2,5):
#     genearte_table(i)

# # ...................8..........
# with open('c1.txt') as f:
#     c=f.read()
# with open('c1_copy.txt','w') as f:
#     f.write(c)

# .........7.....
# with open('log.txt') as f:
#     c=f.readlines()
# ln=1
# for l in c:
#     if ('business' in l):
#         print(f'yes business present in line number-{ln}')
#         break
#     ln+=1
# else:
#     print("not present")

# # ............................oops..........................

# # ...............1.......................
# class Programmer:
#     def __init__(self,n,l,s):
#         self.n=n
#         self.l=l
#         self.s=s

# obj=Programmer('ramya','py','1000000')
# obj2=Programmer('lav','c','2000000')
# print(obj.n,obj.l,obj.s)
# print(obj2.n,obj2.l,obj2.s)

# # ..................................2......
# class Calculator:
#     n=int(input("enter number:"))
#     def __init__(self):
#         print("Performing operations ")
#     def square(self):
#         print(f'Square of {self.n}={self.n*self.n}')
#     def cube(self):
#         print(f'cube of {self.n}={self.n**3}')
#     def square_root(self):
#         print(f'Square root of {self.n}={self.n **0.5}')
# obj=Calculator()
# obj.square()
# obj.cube()
# obj.square_root()

# # ..................................4.......
# class Calculator:
#     n=int(input("enter number:"))
#     def __init__(self):
#         print("Performing operations ")
#     @staticmethod
#     def greet():
#         print("Good morning")
#     def square(self):
#         print(f'Square of {self.n}={self.n*self.n}')
#     def cube(self):
#         print(f'cube of {self.n}={self.n**3}')
#     def square_root(self):
#         print(f'Square root of {self.n}={self.n **0.5}')
# obj=Calculator()
# obj.greet()
# obj.square()
# obj.cube()
# obj.square_root()

# # .................................5.............
# from random import randint
# class Train:
#     def __init__(self,t_no):
#         self.t_no=t_no
#     def book_t(self,f,e):
#         print(f"your ticket is booked from {f} to {e}")
#     def get_update(self):
#         print(f'The train number {self.t_no} is on time')

#     def fare_info(self):
#         print(f'The ticket fare for {self.t_no} is={randint(200,500)}')
# obj=Train(22131)
# obj.book_t('ballary','raichur')
# obj.get_update()
# obj.fare_info()

# # ........................inheritance.......................
# # ......................1............
# class Twodvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f'the vector is {self.i}i + {self.j}j')
# class Threedvector(Twodvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f'the vector is {self.i}i + {self.j}j + {self.k}k')

# a=Twodvector(1,2)
# a.show()
# b=Threedvector(2,3,4)
# b.show()
# # ...........................2.........
# class Animal:
#     pass
# class Pets(Animal):
#     pass
# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print('Dog is barking')
# a=Dog()
# a.bark()

# # .................................3....................
