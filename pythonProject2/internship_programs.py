
##1.FACTORIAL
fact=1
n=int(input('enter a num:'))
for i in range(n,0,-1):
    fact=fact*i
print(fact)



##2.FIBINOCI
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



##3.ARMSTRONG
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
armstrong()

 ##lambda
def arm_lambda():
    num=int(input('Enter a number:'))
    arms=str(num)
    result=list(map(lambda a:int(a)**len(arms),arms))
    final=0
    for i in result:
        final=final+i
    print(final)
arm_lambda()



##4.REVERSE INTEGER
l = []
n =int(input('Enter the num of elements:'))
for i in range(n):
    l.append(int(input('enter the elements')))
print('list=',l)
print('Reveresed list=',l[::-1])



##5.RECUSSION FACTORIAL
def cal_fac(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
cal_fac(5)



##6.RIGHT SIDE TRIANGLE UPWARD
def pattern():
    n=5
    for i in range(1,n+1):
        print(' *'*i)
pattern()



##7.RIGHT SIDE TRIANGLE DOWNWARD
def pattern1():
    n=5
    for i in range(n , 0, -1):
          print(' *'*i)
pattern1()



# ##8.LEFT SIDE TRIANGLE UPWARD
def pattern3():
    n=5
    for i in range(1,n+1):
        print(' '*(n-i),'*'*i)
pattern3()



##9.LEFT SIDE TRIANGLE DOWNWARD
def pattern4():
  n=5
  for i in range(1,n+1):
        print(' '*i,' *'*(n-i))
pattern4()



##10.USER NAME PASSWORD
name=input('Enter a name:')
if name=='ramya':
    print('hi,ramya')
    pas=input('Enter a password:')
    if pas=='123':
        print('Access granted')
    while pas!='123':
        new_pas=input('Enter a new password')
        if new_pas=='123':
            print("Access granted")
            break
else:
    print('name is not found')



##11.USER NAME PASSWORD WITH ATTEMPTS
u_n=input('Enter a name:')
if u_n=='ramya':
    print('hi,ramya')
    for i in range(1,4):
        u_p=input("enter a password")
        if u_p=='123':
            print('welcome')
            break
        else:
            print(f"{i}attempts done/n {3-i} attempts are remaining")
        if i==3:
            print('Account block')
else:
    print('invalid user')



##12.ATM
name=['ramya','lavanya','poojitha','bhanu']
pas=[1,2,3,4]
balance=[1000,1500,1200,1000]


def withdraw(current):
    amt=int(input('Enter a amount:'))
    if amt<=balance[current]:
        balance[current]-=amt
        print(balance[current])
    else:print('insufficient')
def deposit(current):
    amt=amt=int(input('Enter a amount:'))
    balance[current]+= amt
    print(balance[current])
def c_balance(current):
    print('Balance is:',balance[current])
def default(current):
    print("enter crt option")



u_n=input('Enter a name:')
u_p=int(input('Enetr a password:'))
for i in range(len(name)):
    if u_n==name[i]:
        print('hello')
        if u_p==pas[i]:
            while True:
                print('1:withdraw\n 2:deposit\n 3:balance')
                option=int(input('Enter option:'))
                if option==0:break
                data={1:withdraw,2:deposit,3:c_balance}
                res=data.get(option,default)
                res(i)




##13.SQUARE PATTERN
n=int(input('Enter a value:'))
for i in range(1,n+1):
    if i==1 or i==n:
        print('* '*n)
    else:print('* ','  '*(n-3),'*')



##14.UPWARD TRIANGLE
def pattern6():
    n = int(input('Enter a num:'))
    for i  in range(1,n+1):
        print(' '*(n-i),'*'*(i+(i-1)))
pattern6()


##15.DOWNWORD TRIANGLE
def pattern7():
    n = int(input('Enter a num:'))
    for i in range(n,0,-1):
        print(' '*(n-i),'*' *(i+(i-1)))
pattern7()


##16.WORD PATTERN
def name1():
    w=input('Enter a word:')
    for i in range(len(w)):
        print(w[0:i+1])
    for i in range(len(w), 1, -1):
        print(w[0:i - 1])
name1()









