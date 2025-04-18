#..........rps.......
import random
def rps():
    l = ['rock', 'paper', 'ss']
    print(l)
    com_point=0
    user_point=0
    while True:
        n = input("play or quit:").lower()
        if n == 'quit':
            print("Thank you for playing")
            break
        elif n=='play':
            user = input("Enter user choice:").lower()
            if user in l:
                com = random.choice(l)
                print(f'User choice={user}')
                print(f'computer choice={com}')
                if user==com:
                    print("Draw")
                    print(f'user-point= {user_point},\ncomputer-point= {com_point}')
                elif user=='rock' and com=='paper':
                    print("com wins")
                    com_point+=1
                    print(f'user-point= {user_point},\ncomputer-point= {com_point}')
                elif user=='rock' and com=='ss':
                    print("user wins ")
                    user_point+=1
                    print(f'user-point= {user_point},\ncomputer-point= {com_point}')
                elif user=='paper' and com=='rock':
                    print("user wins")
                    user_point += 1
                    print(f'user-point= {user_point},\ncomputer-point= {com_point}')
                elif user=='paper' and com=='ss':
                    print("com wins")
                    com_point += 1
                    print(f'user-point= {user_point},computer-point= {com_point}')
                elif user=='ss' and com=='rock':
                    print("com wins")
                    com_point += 1
                    print(f'user-point={user_point},computer point= {com_point}')
                elif user=='ss' and com=='paper':
                    print("user wins")
                    user_point += 1
                    print(f'user-point= {user_point},\ncomputer-point= {com_point}')
                else:
                    print("Invalid")
            else:
                print("Enter valid choice")
        else:
            print("invalid")

rps()


