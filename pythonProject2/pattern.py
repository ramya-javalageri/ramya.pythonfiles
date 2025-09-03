# RIGHT TRIANGLE PATTERN
# for i in range(5):
#     for j in range(i):
#         print(' *',end='')
#     print('')
# for k in range(5,0,-1):
#     for l in range(k):
#         print(' *',end='')
#     print('')
#
#
# def pattern():
#     n=5
#     for i in range(1,n+1):
#         print('$ '*i)
#     for i in range(n-1,0,-1):
#         print('$ '*i)
# pattern()


# LEFT TRIANGLE PATTERN
# def pattern2():
#     n=5
#     for i in range(1,n+1):
#         print(' '*(n-i),'* '*i)
#     for i in range(1,n+1):
#         print(' '*i,'* '*(n-i))
# pattern2()
#
#DIMOND PATTERN
# def pattern3():
#     n=5
#     for i in range(1,n+1):
#         print(' '*(n-i),'* '*i)
#     for i in range(1,n+1):
#         print(' '*i,'* '*(n-i))
# pattern3()


# RHOMBUS PATTERN
# def pattern():
#     n = int(input('Enter a num:'))
#     for i  in range(1,n+1):
#         print(' '*(n-i),'*'*(i+(i-1)))
#
#     for i in range(n-1,0,-1):
#         print(' '*(n-i),'*' *(i+(i-1)))
# pattern()



#HELLO PATTERN
# def name1():
#     w=input('Enter a word:')
#     for i in range(len(w)):
#         print(w[0:i+1])
#     for i in range(len(w), 0, -1):
#         print(w[0:i - 1])
# name1()
# SQUARE PATTERN
n=int(input('Enter a value:'))
for i in range(1,n+1):
    if i==1 or i==n:
        print('* '*n)
    else:
        print('* ','  '*(n-3),'*')

# def sum(n1,n2,n3):
#     print(n1,n2,n3)
#     return n1+n2+n3
# res=sum(2,3,4)
# print(res)
