#..........Assertion error......
# ip=int(input())
# # print(ip)
# def check(value):
#     assert(value!=0),"wrong input"#print when it becomes false
#     print(5/value)
# check(ip)

# ,,,,,,raise error
try:
    ip=int(input())
    def check(val):
        if(val==0):
            raise ValueError("Wrong input")
        print(5/val)
    check(ip)
except ZeroDivisionError:
    print("error")