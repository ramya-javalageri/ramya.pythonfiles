# ...........oops.....
# Examples............
# class Cloths:
#     a=10 #attribute
#     b=20
#     def __init__(self,a): # constructor (when object i created funtion called is automatically)
#         print("Welcome",self.a,self.b,a)# self.a will access global value inside the class
#     def display(self):
#         print("hello")
# b=Cloths(4)# object
# print(b.a)


# class Dog:
#     greetings="welcome"
#     def bard(self,name):
#         print(f"{name} is barking")
# a=Dog()
# print(a.greetings)
# print(a.bard("Buddy"))
# print(a.greetings)
#......................Calculator............
# class Calculator:
#     def __init__(self):
#         print("Performing arithematic operations")
#     def add(self,a,b):
#         print("add=",a+b)
#     def sub(self,a,b):
#         if a-b>=0:
#             print("sub=",a-b)
#         else:
#             print("sub=",b-a)
#     def mul(self,a,b):
#         print("mul=",a*b)
#     def div(self,a,b):
#         try:
#             print("div=", a // b)
#         except:
#             if b==0:
#                 print("Error",ZeroDivisionError)
#
#         # print("div=",a//b)
# obj=Calculator()
# a=int(input("Enter a value1:"))
# b=int(input("Enter a value2:"))
# obj.add(a,b)
# obj.sub(a,b)
# obj.mul(a,b)
# obj.div(a,b)


# class num:
#     def __init__(self,n):
#         self.n1=n
#     def display(self):
#         print(self.n1)
# o=num(4)
# o.display()

# class a:
#     def __init__(self):
#         print("hello")
#     def __del__(self):
#         print("Deleted")
#     def __str__(self):
#         print("Onee")
#         return "I am object"
# obj=a()
#
# print(obj)
# del obj# for getting object use __str__(self) and return value

# .................Inheritance

# class Parent:
#     def display1(self):
#         print("I am parent")
# class Child(Parent):
#     def display2(self):
#         print("I am child")
# # o1=Parent()
# o1=Parent()
# o1.display2()
# o1.display1()

# class A:
#     def one(self):
#         print("I am one")
# class B(A):
#     def two(self):
#         print("I am two")
# class C(A):
#     def three(self):
#         print("I am three")
# class D(B,C):
#     def four(self):
#         print("I am Four")
# obj=D()
# obj.one()
# obj.two()
# obj.three()

# ....................Encapsulation...........
# class A:
#     __a=10
#     _b=20
#     def display(self):
#         print(self.a,self.b)
# class B(A):
#     c=30
#     def display2(self):
#         print(self.c)
# class C(A):
#     def display3(self):
#         print("Hello C")
# obj=C()
# obj.display2()
# print(obj.display())


# class d:
#     __a=10
#     _b=20
#     def fun(self):
#         print(self.__a,self._b)
# obj=d()
# print(obj.__a)
# print((obj._b))
# obj.fun()

# ...............Polymorphism.........

# method overloading.........
# class poly:
#     def __init__(self):
#         print("Polymor")
#     def add(self,*num):
#         if (len(num)==1):
#             return num[0]
#         elif (len(num)==2):
#             return num[0]+num[1]
#         elif (len(num)==3):
#             return num[0]+num[1]+num[2]
#         else:
#             return "invalid"
# p=poly()
# print(p.add(2))
# print(p.add(2,3))
# print(p.add(2,3,4))
# print(p.add(2,3,4,5))

# ...............Abstraction..........
# from abc import ABC,abstractmethod
# class car(ABC):
#     @abstractmethod
#     def milage(self):
#         pass
# class tesla(car):
#     def milage(self):
#         print("30")
# class renault(car):
#     def milage(self):
#         print("27")
# t=tesla()
# t.milage()
# r=renault()
# r.milage()
# x=car()
# x.milage()


# .........overriding......
# class poly:
#     def __init__(self):
#         print("p1")
#     def add(self):
#         print('1a')
# class poly1(poly):
#     def __init__(self):
#         print("p2")
#     def add(self):
#         print("2a")
# o=poly()
# o=poly1()
# o.add()

#.............static method
# class car:
#     @classmethod
#     def display(self):
#         print('hello')
#     @staticmethod
#     def show():
#         print("show hi")
# t=car()
# t.display()
# t.show()