a=int(input('enter a number:'))
b=int(input('enter a number:'))
c=int(input('enter a number:'))
lis=[a,b,c]
lis.sort(reverse=True)
print(lis)
print("largest=",lis[0])
print("sec_lar=",lis[1])
print("third_lar=",lis[2])
#if condition
if a>b and a>c:
    print('a 1')
    if b>c:
        print("b 2\nc 3")
    else:
        print('c 2\nb 2')
elif b>a and b>c:
    print('b 1')
    if a>c:
        print('a 2\nc 3')
    else:
        print('c 2\na 3')
else:
    print('c 1')
    if a>b:
        print('a 2\nb 3')
    else:
        print('b 2\na 3')
