# l = []
# n =int(input('Enter the num of elements:'))
# for i in range(n):
#     l.append(input('enter the elements'))
# print('list=',l)
# print('Reveresed list=',l[::-1])
# if l==l[::-1]:
#     print('palindrome')
# else:
#     print('not')

class a:
    def reverse(self,n):
        s=str(n)
        return int(s[::-1])
class b(a):
    def palindrome(self,n):
            if self.reverse(n)==n:
                print('palindrome')
            else:
                print('not palindrome')
b().palindrome(121)