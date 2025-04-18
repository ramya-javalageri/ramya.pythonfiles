import random
s={16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
l={1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
new_pos=0
n_p=0
while new_pos<100 and n_p<100:
    print("--------------------------------")
    input("press enter to roll a dice:")
    roll=random.randint(1,6)
    print(f"you rolled a dice:{roll}")
    new_pos+=roll
    if new_pos>100:
        print("u try again")
        new_pos-=roll
        continue
    elif new_pos in s:
        print(f"you landed on snake and your current position:{s[new_pos]}")
        new_pos=s[new_pos]
    elif new_pos in l:
        print(f"you got ladder and your current position :{l[new_pos]}")
        new_pos=l[new_pos]
    else:
        print(f"your current position:{new_pos}")
        # user_current_pos=new_pos
    print("computer turn")
    rollc=random.randint(1,6)
    print(f"computer rolled a dice:{rollc}")
    n_p+=rollc
    if n_p>100:
        print(" c try again")
        n_p-=rollc
        continue
    elif n_p in s:
        print(f"computer landed on snake and its current position:{s[n_p]}")
        n_p=s[n_p]
    elif n_p in l:
        print(f"computer got ladder and its current position :{l[n_p]}")
        n_p=l[n_p]
    else:
        print(f" computer current position:{n_p}")
if new_pos==100:
    print("user win")
elif n_p==100:
    print("computer win")



