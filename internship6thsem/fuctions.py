# def sum(n1,n2,n3):
#     # print(n1,n2,n3)
#     return n1+n2+n3
# res=sum(int(input()),int(input()),int(input()))
# print(res)

# ................recursion..........
# num=0
# def a():
#     global num
#     print('h')
#     if num==5:
#         return 'hi'
#     num+=1
#     # print(a())
#     return a()
# print(a())
# .................factorial using recursion............................
# def fact(n):
#     if n==1 :
#         return 1
#     return n*fact(n-1)
# print(fact(int(input('Enter a number:'))))
# ...........................................
# def a(n):
#     print(n)
#     if n<=1:
#         return 1
#
#     return a(n-1)
# a(5)
#
# ....................................
# def a(n):
#     global p
#     print(p-(n-1))
#     if n==1:
#         return 5
#     return a(n-1)
# p=int(input())
# a(p)

# .................................
# a=[1,2,3,4]
# def add(n1):
#     if len(n1)==0:
#         return 0
#     return n1[0]+add(n1[1:])
# print(add(a))

# a=[1,2,[3,4],[5,6]]
# def add(n):
#     s=0
#     for i in n:
#         if type(i)==list:
#             s+=add(i)
#         else:
#             s+=i
#     return s
# print(add(a))

# def add(n):
#     if len(n)==0:
#         return 0
#     elif n is list:
#         return n[0]+add(n[1:])
#     return n[0]+add(n[1:])
# print(add(a))

# li=[1,2,3,4,5]
# def sumli(n,i):
#     if i==len(n):
#         return 0
#
#     return n[i]+sumli(n,i+1)
# print(sumli(li,0))

# li=[1,2,[3,4],[5,6]]
# def sumli(n,i):
#     if i ==len(n):
#         return 0
#     elif type(n[i]) is list:
#         return sum(n[i])+sumli(n,i+1)
#     else:
#         return n[i]+sumli(n,i+1)
# print(sumli(li,0))

# def sumli(n,sp):
#     print(sp)
#     if n==sp:
#         return n
#     return sumli(n,sp+1)
# print(sumli(5,1))

# ..............reverse string.......
def rev(w):
    if len(w)==0:
        return ''
    return w[-1]+rev(w[:-1])
s=input('enter a word:')
print(rev(s))

# ...................sum of integers............
def num(n):
    if n==0:
        return 0
    l=n%10
    n//=10
    return l+num(n)
n=int(input("enter a number:"))
print(num(n))

# ..........................power................
def power(n,p):
    if p==0:
        return 1
    p-=1
    return n*power(n,p)
n=int(input('enter the number:'))
p=int(input('Enter the power'))
print(power(n,p))