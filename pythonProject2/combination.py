# l=[1,2,3,4]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         print(l[i],l[j])
#
# from math import *
# print(sqrt(100))
from itertools import *
l=[1,2,10,3,4,5,6,7,8,9,0]
print(list(combinations(l,2)))
