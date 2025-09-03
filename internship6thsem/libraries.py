#.......................................library---collection of python code.
# import numpy as np
# arr=np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]])
# print(type(arr))
# print(arr[0][1, -3:])
# print(arr.ndim)
import pandas as pd

#...............for loop to read array......
# import numpy as np
# arr=np.array([1,2,3])
# arr2=np.array([[1,2,3],[4,5,6]])
# for i in arr:
#     print(i)
# for i in arr2:
#     for j in i:
#         print(j,end='')
# ........................................using range function..........
# arr=np.array([1,2,3])
# arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for i in range(len(arr)):
#     if arr[i]==3:
#         arr[i]=10               #.......updating the value........
# print(arr)
# for i in range(len(arr2)):
#     for j in range(len(arr2[i])):
#         if arr1[i][j]==2:
#             arr1[i][j]=10
# print(arr1)
# for i in range(len(arr2)):
#     for j in range(len(arr2[i])):
#         for k in range(len(arr2[i][j])):
#             # print(f'index {i}-{j}-{k}={arr2[i][j][k]}')
#             if arr2[i][j][k]==4:
#                 arr2[i][j][k] =10
# print(arr2)

# for i in range(len(arr1)):
#     for j in range(len(arr1[i])-1,0):
#         print(arr1[i][j],end='')
#     print()
# print(arr1)


import pandas as pd
# pd1=[1,2,3,4]
# pd2=[4,3,1]
# s1=pd.Series(pd1)
# s2=pd.Series(pd2,index=['x','y','z'])
# print(s2)


# import pandas as pd
# mydataset={'cars':['BMW','Volvo','Ford'],'year':[1990,1980,1970]}
# # data=[1,2,3,4,5]
# myvar=pd.DataFrame(mydataset)
# # myvar=pd.Index()
# print(myvar)


# import  pandas as pd
# pdRead=pd.read_csv('C:\Users\RAMYA\Downloads')
# print(pdRead)


# ....................matplotlib.........
import matplotlib.pyplot as plt
# import numpy as np
# xp=np.array([1,2,3,10])
# yp=np.array([1,7,8,10])
# plt.plot(xp,yp)
# plt.plot(xp,yp,'*')
# plt.plot(xp,yp,marker='o')
# plt.title("Sports vs data")
# plt.xlabel("Sports")
# plt.ylabel("Data")
# x=np.array(['a','b','c'])
# y=np.array([1,2,3])
# myexplode=[0.3,0,0]
# myc=['red','blue','green']
# plt.pie(y,labels=x,explode=myexplode,shadow=False,colors=myc)
#
# # plt.plot(yp,'D:r')
# plt.show()
# ...............................................