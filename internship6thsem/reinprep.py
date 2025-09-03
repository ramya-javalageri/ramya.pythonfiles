# ........rotating string........
# s, goal = input().split()
# if len(s) == len(goal) and goal in s + s:
#     print("True")
# else:
#     print("False")
# ..............isomorphic........
# def isomorphic(s, t):
#     if len(s) != len(t):
#         return "True"
#
#     mapping = {}
#
#     used_chars = set()
#
#     for i in range(len(s)):
#
#         if s[i] not in mapping:
#
#             if t[i] in used_chars:
#                 return "False"
#
#             mapping[s[i]] = t[i]
#
#             used_chars.add(t[i])
#
#         else:
#
#             if mapping[s[i]] != t[i]:
#                 return "False"
#
#     return "True"
#
#
# s, t = input().split()
#
# print(isomorphic(s, t))

# s=input()
# a=s.lstrip('0')
# # print(a)
# for i in range(len(a)):
#     if int(a[-1])%2!=0:
#         print(a)
#         break
#     else:
#         a.replace(a[-1],'')
#         print(a)
#         break

# .............linear search...........
a=list(map(int,input().split()))
num=int(input())
for i in range(len(a)):
    if a[i]==num:
        print("found at index",i)
else:
    print("not found")





