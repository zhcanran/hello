#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np

# 创建numpy
l1=[1,2,3,4,5,6]
a=np.array([1,2,3,4])
a1=np.array([[1,2],[3,4]])
a2=np.array(l1)
a3=np.asarray(l1)

a4=a2+a3
print(a2)
print(a3)
print(a4)

#np.prod()函数用来计算所有元素的乘积，对于有多个维度的数组可以指定轴，如axis=1指定计算每一行的乘积。

#一维
b=np.prod(a)
print(b)

#二维
c=np.prod(a1)
print(c)

#二维
c=np.prod(a1,axis=0)#指定维度
print(c)

#创建（2，3）形状，均值为0，标准差为1的，符合正太分布的数据
d=np.random.normal(0,1,(2,3))
print(d)
