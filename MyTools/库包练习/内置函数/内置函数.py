#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class model:
    a=1
    b=2
    c=3

# 是否包含某些属性
print(model.__dict__) #展示对象包含哪些属性

print(hasattr(model,'a'))#判断对象是否包含某些属性
print(hasattr(model,'d'))

aa=1
print(isinstance(aa,int )) #判断是否属于这个类型

print(hash(aa)) #获取对象哈希值
print(hash('strr'))