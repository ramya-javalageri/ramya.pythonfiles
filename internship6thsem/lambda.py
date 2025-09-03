#...................
# def user_n(name):
#     return "hello "+name
#
# a=lambda n1:'hello'+n1
# print(user_n(input("Enter a name:")))
# print(a((input("Enter a number:"))))
# ...........a......
# a=lambda *n:print(n)
# a('abc','jj','jhsu')
# a=lambda *n:print(list(reversed(n)))
# a(4,5,1,3,8)

# a=lambda n1,n2,n3=0:print(n1,n2,n3)
# a(1,2)
# n=lambda a,b,c:max(a,b,c)
# print(n(1,2,6))

# .............mapping......
# l=[[1,2,3],[3,5,6],[8,7,1]]
# def double(n):
#     m=1
#     for i in n:
#         m=m*i
#     return m
# res=map(double,l)
# print(list(res))

# def sort_l(n):
#     return (sorted(n))
# res=map(sort_l,l)
# print(list(res))


#......filter............
# l=[4,5,6,1,77,2,3]
# def fil(n):
#     return n>5
# r=filter(fil,l)
# print(list(r))

# names=['abhishek','hasinha','arjun','surya','jo','haarith']
# def fil(n):
#     return len(n)<=5
# r=filter(fil,names)
# print(list(r))

# .......reduce.....
from functools import reduce
# add=(1,2,3,4)
# def double_tuple(n1,n2):
#     print(n1,n2)
#     return n1+n2
# re=reduce(double_tuple,add,1)
# print(re)

# w=['apple','banana','orange']
# def l_w(w1,w2):
#     # print(w1,w2)
#     # print(len(w1),len(w2))
#     if len(w1)>len(w2):
#         return w1
#     elif len(w1)==len(w2):
#         return w1,w2
#     else:
#         return w2
# r=reduce(l_w,w,'abcdbhgh')
# print(r)
