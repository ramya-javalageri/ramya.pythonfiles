# #QUADRATIC EQUATIONS
# import cmath,math
# a=1
# b=5
# c=6
# d=((b**2)-(4*a*c))
# sol1=((-b-cmath.sqrt(d))/(2*a))
# sol2=((-b+cmath.sqrt(d))/(2*a))
# print('two solutions are:',sol1,sol2)
#
# #RANDOM
# import random
# print(random.randint(10,20))
# lis=['ramya','lavanya','poojitha','bhanu']
# print(random.choice(lis))
#
# prime number
# a=int(input('Enter a num:'))
# if a==1:
#     print('1 is not a pm')
# elif a>1:
#     for i in range(2,a):
#         if a%i==0:
#             print('not pm')
#         else:
#             print('pm')
#         break
# else:
#     print('enter positive num')
#
# for num in range(1,11):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                break
#         else:
#             print(num)
#
# LCM
# def lcm(a,b):
#     if a>b:
#         g=a
#         print(a,'is greater')
#     else:
#         g=b
#         print(b,'is greater')
#     while(True):
#
#         if (g%a==0) and (g%b==0):
#             res=g
#             break
#         g+=1
#     return res
# print('The lcm is',lcm(54,24))
#
# #factors
# def factors(x):
#     print('the factors of',x,'are:')
#     for i in range(1,x+1):
#         if x%i==0:
#             print(i)
#
# print(factors(10))
# tables
# n=int(input('Enter a num:'))
# for i in range(1,11):
#     print(n,'*',i,'=',n*i)
#
# #calender
# import calendar
# yy=int(input('Enter a year:'))
# mm=int(input('enter a month:'))
# print(calendar.month(yy,mm))
#
# class student:
#     clg_name='BITM'
#     def __init__(self,name,usn,branch):
#         self.name=name
#         self.usn=usn
#         self.branch=branch
#     def display(self,name,usn,branch):
#         print('STUDENT:','\n',self.name,'\n',self.usn,'\n',self.branch,'\n',self.clg_name)
# s= student('ramya','3br22ec131','ECE')
# s.display('ramya','3br22ec131','ECE')
#
# class food:
#     def __init__(self,*snacks):
#         self.snacks1='pizza'
#         self.snacks2 = 'samosa'
#         self.snacks3 = 'cake'
#     def display(self):
#         print('snacks:',self.snacks1,self.snacks2,self.snacks3)
# items=food('pizza','samosa','cake')
# items.display()
#
# import math
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def perimeter(self):
#         print('perimeter=',2*(math.pi)*self.radius)
#     def area(self):
#         print('area=',(math.pi)*(self.radius**2))
# c=circle(5)
# c.perimeter()
# c.area()

from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def c_age(self):

        today=date.today()
        age=today.year-self.dob.year
        if today<(date(today.year,self.dob.month,self.dob.day)):
            age-=1
        return age
    def display(self):
        print('name=',self.name,'\ncountry=',self.country,'\ndate of birth=',self.dob,'\nage=',self.c_age())
person1=person('ramya','INDIA',date(2004,12,10))
person2=person('roja','INDIA',date(2008,6,10))
person3=person('bhanu','INDIA',date(2004,7,12))
person4=person('Lavanya','INDIA',date(2004,11,18))
person5=person('Poojitha','INDIA',date(2004,4,30))
person1.c_age()
person2.c_age()
person3.c_age()
person4.c_age()
person5.c_age()
person5.display()
#
# a={1,2,4}
# a=frozenset(a)
# print(type(a))
#
#
#
#
