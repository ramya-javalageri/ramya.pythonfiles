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








