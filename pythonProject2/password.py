name=input('Enter a name:')
if name=='Ramya':
    print('Hi,Ramya')
    pas=input('Enter a password:')
    if pas=='123':
        print('Access granted')
    else:
        print('Try again')
else:
    print("Name is not found")
ramya_amt=10000
roja_amt=10000
def ramya():
    print('Hi,Ramya')
    pas=input('enter a pasword:')
    if pas=='123':
        w=print('access granted')
    else:
        print('try again')
    w=input('Enter a work')
    amt=int(input('Enter a amount:'))
    ramya_amt = 10000
    if w=='withdraw':
        if amt<=ramya_amt:
            ramya_amt=ramya_amt-amt
            print(ramya_amt)
        else:
            print('enterned amount is exceeded')
    elif w=='deposit':
        ramya_amt = ramya_amt - amt
        print(ramya_amt)
    else:
        print('enter valid work')

def roja():
    print('Hi,Roja')
    pas = input('enter a pasword:')
    if pas == '567':
        w = print('access granted')
    else:
        print('try again')
    w = input('Enter a work')
    amt = int(input('Enter a amount:'))
    roja_amt = 10000
    if w == 'withdraw':
        if amt <= roja_amt:
            ramya_amt = roja_amt - amt
            print(roja_amt)
        else:
            print('enterned amount is exceeded')
    elif w == 'deposit':
        roja_amt= roja_amt - amt
        print(roja_amt)
    else:
        print('enter valid work')

def imf():
    n=input('Enter a name:')
    switch_data={'Ramya':ramya,'Roja':roja}
    res=switch_data.get(n,0)
    res()
imf()

