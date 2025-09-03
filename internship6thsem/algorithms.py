#........................linear search......
# import numpy as np
# arr=np.array(list(map(int,input('enter num:').split())))
# t=4
# for i in range(len(arr)):
#     if arr[i]==t:
#         print(f'{t} is found in the index:{i}')
#         break
# else:
#     print('Not found')

# ..........................Binary search..............
import numpy as np
arr=np.array(list(map(int,input('enter num:').split())))
arr1=sorted(arr)
t=4
def b_search(arr1,t):
    low=0
    high=len(arr1)-1
    while low<=high:
        mid=(low+high)//2
        if arr1[mid]==t:
            return mid
        elif arr1[mid]>t:
            high=mid-1
        else:
            low=mid+1
    return -1
print(f'{t} is found in the index:{b_search(arr1,t)}')
