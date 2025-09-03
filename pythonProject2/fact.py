fact=1
n=int(input('enter a num:'))
for i in range(n,0,-1):
    fact=fact*i
print(fact)
#recursion
def factorial(n):
    if n==1:
        return 1
        return n*factorial(n-1)
print(factorial(5))
def cal_fac(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
cal_fac(5)
