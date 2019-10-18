import numpy as np
# student = np.dtype([('name','S20'),('age',np.int8),('score',np.int)])
# print(student)
# a = np.array([('abc',  21,  50),('xyz',  18,  75)],dtype=student)
# a = np.arange(24)
# b = a.reshape(2,4,3)
# c = b.reshape(24,)
# a = np.empty(shape=(3,2),dtype=bool,order='C')
# arr = [(1,2,3),(4,5,6)]
# a = np.asanyarray(arr)
# a = a.reshape(3,2)
# print(a)
# print(a.shape)
# xlist = [x for x in range(2,5)]
# ylist = np.arange(2,5)
# zlist = np.asarray(xlist)
# print(xlist)
# print(ylist)
# print(zlist)

b = np.array([1,2,3,4,5,6])
b = b.reshape(3,2,1)
print(b)