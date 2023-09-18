import numpy as np
'''
v=np.array
print(v)

v0=np.zeros( shape: 2,int)
print(v0)

v5=np.array([[8,9,42,5],[5,67,21,90]])
print(v5.shape)

v6=v5.reshape(4,2)
print(v6)

print(v6[2:])

v7=np.arange(60)
print(v7)

v8=np.arange(14,60)
print(v8)

v9=np.arange(20,100,5)
print(v9)

#linespace

v10=np.linspace(1,20,9)
print(v10)

#logspace
v11=np.array([[20,21,9,30,30],[5,6,78,3,20]])
v12=np.array([[1,12,5,6,7],[10,2,8,4,13]])

np.sum(v11)
np.max(v11)
np.min(v11)
np.std(v11)
np.sqrt(v11)
np.average(v11)
np.mean(v11)
np.median(v11)

print(np.average(v11))
print(np.mean(v11))
print(np.median(v11))
print(np.sum(v11))
print(np.max(v11))
print(np.min(v11))
print(np.std(v11))
print(np.sqrt(v11))
v12=v11.max(axis=0)
print(v12)
'''
v11=np.array([[20,21,9,30,30],[5,6,78,3,20]])
v12=np.array([[1,12,5,6,7],[10,2,8,4,13]])
v13=np.vstack((v11,v12))
v14=np.hstack((v11,v12))
print(v13)

for i in np.nditer(v14):
    if i > 5:
        print(i)




