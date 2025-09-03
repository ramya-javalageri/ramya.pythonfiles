# class A:
#     def __init__(self):
#         self.b=self.B()
#         self.c=self.b.C()
#         self.c.fan()
#         self.c.num()
#     def fan(self):
#         print('fan')
#     class B:
#         def __init__(self):
#             pass
#
#         class C:
#             def __init__(self):
#                 print('c')
#             def fan(self):
#                 print('on the fan')
#             def num(self):
#                 n=int(input('enter a num'))
#                 print(n)
#
# A().fan()
# class A:
#     b=10
#     c='RAMYA'
#     def displasy(self):
#         print(self.b)
#         print(self.c)
# A().display()
# class A:
#     def __init__(self):
#         print('DUSTER')
# class B(A):
#     def projector(self):
#         A().__init__()
#         super().__init__()
#         print('PROJECTOR')
# class C(B):
#     pass
#     def fan(self):
#         print('FAN')
# lavanya=A()
# ramya=B()
# preethi=C()
# ramya.duster()
# preethi.projector()
# preethi.duster()
# class a:
#     pass
#
#
#
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print('init b')
# class c(b):
#     pass
# c()
# class ramya:
#     def fav_food(self):
#         print('masala dosa')
# class lav:
#     def fav_food(self):
#         print('annam pappu')
# class pooji:
#     def fav_food(self):
#         print('plain dosa')
# class bhanu:
#     def fav_food(self):
#         print('annam muddhapappu')
# def fav_food(food):
#     food.fav_food()
# r=ramya()
# l=lav()
# b=bhanu()
# p=pooji()
# fav_food(l)
# class A:
#     def __init__(self,a):
#         self.a=a
#     def __truediv__(ramya,roja):
#         return (ramya.a/roja.a)
# roja=A(10)
# ramya=A(20)
# print(ramya/roja)
# print(10*10)
from abc  import ABC,abstractmethod
class printable(ABC):
    @abstractmethod
    def print_content(self):
        pass
class document(printable):

    def print_content(self):
        print('hello')
doc=document()
doc.print_content()
#
#
#
#
