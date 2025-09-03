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
attempts
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
