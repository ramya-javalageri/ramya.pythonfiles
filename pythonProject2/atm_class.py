# class ATM:
#     def _init_(self):
#         self.user_data=self.load()
#     def load(self):
#         user_data={}
#         with open("atm.txt", "r") as file:
#             for line in file:
#                 username, balance = line.strip().split(',')
#                 user_data[username] = float(balance)
#         print(user_data)
#         return user_data
#     def update_data(self):
#         f=open('test.txt','w')
#         for a,b in self.user_data.items():
#             f.write(str(a)+','+str(b)+'\n')
#
#     def withdraw(self,username,amount):
#         if username in self.user_data:
#             if self.user_data[username]<amount:
#                 print('insufficient funds')
#             else:
#                 self.user_data[username]-=amount
#                 print('The Available Amount is:',self.user_data[username])
#                 self.update_data()
#     def deposit(self,username,amount):
#         self.user_data[username]+=amount
#         print('The Available Amount is:', self.user_data[username])
#         self.update_data()
#     def balance(self,username):
#         print('The Available Amount is:', self.user_data[username])
#
#
# def main():
#     atm=ATM()
#     print('press ')
#     while True:
#         print('1 for balance check \n2 for withdraw \n3 for deposit \n4 to Exit')
#         choice=int(input('Enter your choice: '))
#         if choice==1:
#             username=input('Enter your username: ')
#             atm.balance(username)
#         elif choice==2:
#             username=input('Enter your username: ')
#             amount=int(input('Enter your amount: '))
#             atm.withdraw(username,amount)
#         elif choice==3:
#             username=input('Enter your username: ')
#             amount=int(input('Enter your amount: '))
#             atm.deposit(username,amount)
#         elif choice==4:
#             print('thank you for visiting the ATM!!!!')
#             break
#         else:
#             print('invalid input please try again')
#
# print(main())
class atm:
    # def __init__(self,u_n,u_p,balance):
    #     self.u_n=u_n
    #     self.u_p=u_p
    #     self.balance=balance

    def withdraw(current):
        balance=[1000,1500,1200,1000]
        amt=int(input('Enter a amount:'))
        if amt<=balance[current]:
            balance[current]-=amt
            print(balance[current])
        else:print('insufficient')

    def deposit(current):
        balance = [1000, 1500, 1200, 1000]
        amt=amt=int(input('Enter a amount:'))
        balance[current]+= amt
        print(balance[current])

    def c_balance(current):
        balance = [1000, 1500, 1200, 1000]
        print('Balance is:',balance[current])

    def default(current):
        print("enter crt option")

def main():
    atm()
    u_n=input('Enter a name:')
    u_p=int(input('Enter a password:'))
    name=['ramya','lavanya','poojitha','bhanu']
    pas=[1,2,3,4]
    balance=[1000,1500,1200,1000]

    for i in range(len(name)):
        if u_n==name[i]:
            print('hello')
            if u_p==pas[i]:
                while True:
                    print('1:withdraw\n 2:deposit\n 3:balance')
                    option=int(input('Enter option:'))
                    if option==0:break
                    if option==1:
                        atm().withdraw()
                    elif option==2:
                        atm().deposit()
                    elif option==3:
                        atm().c_balance()
                    # data={1:withdraw,2:deposit,3:c_balance}
                    # res=data.get(option,default)
                    # res(i)

# at=atm()
main()
# atm().deposit()
# atm().withdraw()
# atm.c_balance()

# class atm:
#     # def __init__(self,u_n,u_p,balance):
#     #     self.u_n=u_n
#     #     self.u_p=u_p
#     #     self.balance=balance
#
#     def withdraw(current):
#         balance=[1000,1500,1200,1000]
#         amt=int(input('Enter a amount:'))
#         if amt<=balance[current]:
#             balance[current]-=amt
#             print(balance[current])
#         else:print('insufficient')
#
#     def deposit(current):
#         balance = [1000, 1500, 1200, 1000]
#         amt=amt=int(input('Enter a amount:'))
#         balance[current]+= amt
#         print(balance[current])
#
#     def c_balance(current):
#         balance = [1000, 1500, 1200, 1000]
#         print('Balance is:',balance[current])
#
#     def default(current):
#         print("enter crt option")
#
# def main():
#     atm()
#     u_n=input('Enter a name:')
#     u_p=int(input('Enter a password:'))
#     name=['ramya','lavanya','poojitha','bhanu']
#     pas=[1,2,3,4]
#     balance=[1000,1500,1200,1000]
#
#     for i in range(len(name)):
#         if u_n==name[i]:
#             print('hello')
#             if u_p==pas[i]:
#                 while True:
#                     print('1:withdraw\n 2:deposit\n 3:balance')
#                     option=int(input('Enter option:'))
#                     if option==0:break
#                     if option==1:
#                         atm().withdraw()
#                     elif option==2:
#                         atm().deposit()
#                     elif option==3:
#                         atm().c_balance()
#                     # data={1:withdraw,2:deposit,3:c_balance}
#                     # res=data.get(option,default)
#                     # res(i)
#
# # at=atm()
# main()
# # atm().deposit()
# # atm().withdraw()
# # atm.c_balance()
