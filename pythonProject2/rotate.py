name=input('Enter a word:')
n=int(input('Enter 0 or 1:'))
if n==0:
    num=int(input('Enter num of times to be rotated:'))
    for i in range(num):
        name=name[-1] + name[:-1]
    print(name)
    # break
elif n==1:
    num = int(input('Enter num of times to be rotated:'))
    for j in range(num):
        name=name[1:] + name[0]
    print(name)
        # break
else:
    print('Enter 0 or 1')



