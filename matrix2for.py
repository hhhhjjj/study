import time as tm
import numpy as np
dim = 100000#数据长度(包含的元素个数)
x1 = np.ones(dim)
x2 = np.ones(dim)
yFor = np.ones(dim)
tStart = tm.clock()#开始计时
#for循环解算x1*x2(对应元素相乘)
for i in range(dim):
    yFor[i] = x1[i]*x2[i]
tEnd=tm.clock()#停止计时
tFor = tEnd-tStart#计算用时
tStart = tm.clock()#开始计时
#矩阵计算x1*x2(对应元素相乘)，这个直接就是整体相乘了
yMatrix = x1*x2
tEnd = tm.clock()#停止计时
tMatrix = tEnd-tStart#计算用时
print('for循环用时tFor=',tFor)
print('矩阵运算用时tMatrix=',tMatrix)
print('运算用时tFor-tMatrix=',tFor-tMatrix)
print('运算结果的差(所有元素累积和)yFor-yMatrix=',np.sum(yFor-yMatrix))
# 在数据量少的情况下for循环还快一些，数据量大的情况下还小一些
# 用tf.tile也可以代替for循环，不过我也没看明白怎么用
