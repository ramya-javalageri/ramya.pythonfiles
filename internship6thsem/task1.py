#  ............max value.........
# lis=[]
# n=int(input("Enter the length of list:"))
# for i in range(n):
#     lis.append(int(input()))
# print(lis)
# n=lis[0]
# for i in range(len(lis)):
#     if lis[i]>n:
#         n=lis[i]
# print(n)

# .............2
# lis=[]
# n=int(input("Enter the length of list:"))
# for i in range(n):
#     lis.append(int(input()))
# print(lis)
# for i in range(1,n):
#     print(lis[i-1]+lis[i])

#......3.reverse
# word=input("Enter a word:")
# print(word[::-1])

# ...............factorial
# fact=1
# for i in range(1,int(input())+1):
#     fact*=i
# print(fact)


# .......4.fibonacci series......

# a=0
# b=1
# for i in range(int(input())):
#     print(a)
#     c=a+b
#     a=b
#     b=c


#........palindrome..........
# w='abcdcba'
# w=input()
# if w==w[::-1]:
#     print(w,'is a palindrome')
# else:
#     print(w,'is not a palindrome')

# .......7..anagram.........
# w1=input()
# w2=input()
# if len(w1)==len(w2):
#     l1=list(w1)
#     l2=list(w2)
#     s1=l1.sort()
#     s2=l2.sort()
#     if s1==s2:
#         print('anagram')
#     else:
#         print('not')
# else:
#     print('length not equal')

# ...........8....pattern....
# n=int(input('Enter a value:'))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print('* '*n)
#     # else:
#     #     print('* ','  '*(n-3),'*')
#     for j in range(1,n+1):
#         if j!=1 or j!=n:
#             print("* ",' '*(n-3),'*')


# ...........9.
# n=int(input("enter a num:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(n+1-i,end='')
#     print()
# .............10........
# n=int(input("enter a num:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# n=int(input())
# c=0
# for i in range(n):
#     if i<=1:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         c+=1
# print(c)

# n=int(input())
# order_n=str(n)
# l=[]
# for i in str(n):
#     if i not in l:
#         l.append(i)
# l.sort()
# print(l)
# dic={}
# while n>0:
#     l=n%10
#     n //= 10
#     # print(l)
#     if l in dic:
#         dic[l]+=1
#     else:
#         dic[l]=1
#
# dict((sorted(dic.items())))
# print(dic)
# for i,j in dic.items():
#     print(f'{i}-{j}')

    # print(n)
#     dic.update({l:0})
# print(dic)
# for i in l:
#     print(f'{int(i)}-{dic.get(int(i))}')
# ...............................................
# def find_factors(n):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     return factors
#
# n = int(input("Enter a number: "))
# print(find_factors(n))


# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*n)
#     else:
#         print('* ',end="")
#         print('  '*(n-2),end="")
#         print('*')

# n=int(input())

# for i in range(1,2*n):
#     for j in range(1,2*n):
#         if i==j or i+j==2*n:
#             print('*',end=" ")
#         else:
#             print(' ',end=' ')
#     print()
#
# for i in range(0,n):
#     for j in range(0,n):
#         if (i==0 or i==n-1 or j==0 or j==n-1 or j==i or i==n-1-j):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print('')


# .........................
# l=list([3,4,1,6,7,8])
# l=list(map(int,input("Enter the elements:").split()))
# k=int(input("Enter the number :"))
# lis=[]
# for j in range(1,k+1):
#     a=max(l)
#     lis.append(a)
#     l.remove(a)
# print(sum(lis))



# ..........01/03/25...............
# .....................lower and upper..........
# s="hELLO aLL 22"
# print(s.swapcase())
# r=''
# for i in s:
#     if (i.isupper()):
#         r=i.lower()
#     else:
#         r=i.upper()
#     print(r,end='')

# .......palindrome...................
# s=input().lower()
# g=s[::-1]
# print(s==g)

# ..............anagram.........
# ip1=input()
# ip2=input()
# if len(ip1)==len(ip2):
#     for i in ip1:
#         if ip1.count(i)!=ip2.count(i):
#             print('false')
#             break
#     else:
#         print('True')
# else:
#     print('False')
#
# ip="hello words this is java"
# li=list(map(str,ip.split()))
# ip_r=''
# for i in li:
#     ip_r+=i[::-1]
#     ip_r+=' '
# print(ip_r,end='')
# print()

# ....................................
# ip=list('abcdefgh')
# for i in range(0,len(ip),2):
#     # if i%2==0 and i+1<len(ip):
#     ip[i],ip[i+1]=ip[i+1],ip[i]
# print(''.join(ip))
# print()
# ..............................
# ip=input()
# if ip.isdigit():
#     print(ip.lstrip('0'))

    # ..........................................
# li = [2, -3, 4, -1, 2, 1, -5, 4]
# max_sum = float('-inf')
# sum = 0
# for i in li:
#     sum += i
#     max_sum = max(max_sum, sum)
#     if sum < 0:
#         sum = 0
# print(max_sum)

#................................
# n=int(input())
# s=0
# for i in range(1,n+1):
#     s+=i
# print(s)

# # ...............
# n=int(input())
# p=1
# while n!=0:
#     l=n%10
#     n//=10
#     # print(l)
#     p*=l
# print(p)

s=input("Enter string:")
for i in s:
    if i==i.lower():
        print('lower')
        break
else:
    print('not lower')
for i in s:
    if i==i.upper():
        print('upper')
        break
for i in s:
    if i.isdigit():
        print('digit')
        break
c=0
for i in s:
    if i.isalpha():
        c+=1
        if c==len(s):
            print("letters")
# if s.isalpha() & s.isdigit():
#     print('num&letters')
