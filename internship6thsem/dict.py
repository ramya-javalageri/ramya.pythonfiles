# # ............dict................:
# dic={'1':1,'2':2,'3':3}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.get('1'))
# print(dic.get('2',1))
# # print(dic.get(4,'bb'))
# dic.update({'3':1})
# # print(dic.pop(1))
# dic['2']=1
# print(dic['2'])
# print(dic)
# # print(dic.popitem())
# for i in dic.items(): #
#     print(i)
# for i,j in dic.items():
#     print(f'key is {i}-value is {j}')
# for i in dic:
#     print(i)# for getting keys
#     print(dic[i]) # for getting values
#     print(dic.get(i))# for getting values
# # dic['3']=dic.get('3')+1
# print(dic)
# for i in dic:
#     dic[i]=dic.get(i)+1
# print(dic)
#
# dic={}
# for i in range(10):
#     dic[i]=dic.get(i,0)+1
# print(dic)
# for i in range(10):
#     dic[i]=dic.get(i,0)+i+1
# print(dic)

#...........................................................
# n=int(input())
# o_n=str(n)
# l=[]
# for i in o_n:
#     if i not in l:
#         l.append(i)
# print(l)
# dic={}
# while(n>0):
#     a=n%10
#     dic[a]=dic.get(a,0)+1
#     n//=10
# print(dic)
# for i in l:
#     print(f"{i}-{dic.get(int(i))}")

