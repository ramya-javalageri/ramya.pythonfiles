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

#lambda
def arm_lambda():
    num=int(input('Enter a number:'))
    arms=str(num)
    result=list(map(lambda a:int(a)**len(arms),arms))
    final=0
    for i in result:
        final=final+i
    print(final)

def pattern1():
    n=5
    for i in range(1,n+1):
        print('*'*i)
    for i in range(n-1,0,-1):
        print('*'*i)

def pattern2():
    n=5
    for i in range(1,n+1):
        print(' '*(n-i),'*'*i)
    for i in range(1,n+1):
        print(' '*i,'*'*(n-i))

def switch_case():

    while n!=0:
        v=input('Enter yes to continue:')
        if v=='yes':
            switch_data={1:armstrong,2:arm_lambda,3:pattern1,4:pattern2}
            res=switch_data.get(n,default)
        res()
n=int(input('Enter a function name:'))
