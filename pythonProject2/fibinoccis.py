n=int(input('enter a number:'))
a=0
b=1
i=0
while i<n:
    c=a+b
    a=b
    b=c
    i+=1
    print(a)

