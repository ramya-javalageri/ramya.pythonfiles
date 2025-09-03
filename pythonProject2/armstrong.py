# n=int(input('Enter a 3 digit num:'))
# sum=0
# temp=n
# while temp>0:
#     sum=sum+((temp%10)**3)
#     temp=temp//10
# if sum==n:
#     print('The num is armstrong')
# else:
#     print('The num is not  armstrong')
#
# # function
def armstrong():
    num=int(input('enter a number:'))
    arms=str(num)
    result = 0
    for i in arms:
        result=result+int(i)**len(arms)
    print(result)
    if result==num:
        print('armstrong')
    else:
        print('not armstrong')
# armstrong()
# # #lambda
# def arm_lambda():
#     num=int(input('Enter a number:'))
#     arms=str(num)
#     result=list(map(lambda a:int(a)**len(arms),arms))
#     final=0
#     for i in result:
#         final=final+i
#     print(final)
# arm_lambda()

# # Input string and rotation amount for right rotation
# s = "abcde"
# n = int(input("Enter number of positions to rotate right: "))
#
# # Ensure the rotation amount is within the string length
# n = n % len(s)
#
# # Rotate string to the right: move last n characters to the beginning
# rotated = s[-(n+1):] + s[:n]
#
# print("Rotated string:", rotated)
n=int(input())
# for i in range(n,0,-1):
#     for j in range(n,i-1,-1):
#         print(' ',end=' ')
#     for k in range(i-1,0,-1):
#         print('*',end=' ')
#     for l in range(i-2,0,-1):
#         print('*',end=' ')
#     print()
for i in range(n):
    for j in range(n,i+1,-1):
        print(' ',end='')
    for k in range(0,i+1):
        print('*',end='')
    for l in range(1,i+1):
        print('*',end='')
    print()