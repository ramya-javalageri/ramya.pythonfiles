n = int(input('Enter the number:'))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
# n = int(input('Enter the number:'))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print()
# n = int(input('Enter the number:'))
for i in range(n):
    for j in range(0,i+1):
        print('*',end=' ')
    print()

# n=int(input("Enter a number:"))
num=1
for i in range(n):
    for j in range(0,i+1):
        print(num,end=" ")
        num+=1
    print()
# n=int(input("Enter a number:"))
num=1
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(num,end=" ")
        num+=1
    print()
# n=int(input('Enter a number:'))
for i in range(n):
    for j in range(n,i+1,-1):
        print(' ',end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
    print()
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(' ',end=' ')
    for k in range(i-1,0,-1):
        print('*',end=' ')
    print()
# n=int(input('Enter a number:'))
for i in range(n):
    for j in range(n,i+1,-1):
        print(' ',end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
    for l in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(' ',end=' ')
    for k in range(i-1,0,-1):
        print('*',end=' ')
    for l in range(i-2,0,-1):
        print('*',end=' ')
    print()


for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
name=input("Enter a name:")
for i in range(len(name)):
    for j in range(0,i+1):
        print(name[j],end='')
    print()
for i in range(len(name)-1,0,-1):
    for j in range(0,i):
        print(name[j],end='')
    print()

num=1
for i in range(n):
    for j in range(0,i+1):
        print(num,end=' ')
    num+=1
    print()
