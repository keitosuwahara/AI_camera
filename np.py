import numpy as np
a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(a.ndim)
nd=a.ndim+8
print(np.zeros((nd,nd)))

print(a.mean())#mean(配列の平均をとる)
print(a.mean(axis=1))#1行ごとの平均
print('分散→データのばらつき')
print(a.var())
print("std:標準偏差")
print(a.std())
print("最大値")
print(a.max())
print("行ごとの最大値も可能")
print(a.max(axis=1))
print("最小値")
print(a.min())

ar1=np.array([
    [2,3],
    [1,5],
    [3,1]
])
print("転置")
print(ar1.T)
