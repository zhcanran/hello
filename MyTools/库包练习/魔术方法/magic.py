#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Test:
    # def __new__(cls, *args, **kwargs):
    #     print("I'm,__new__")
    def __init__(self):
        self.n = [1, 2, 3, 4, 5, 6, ]
        print("I'm __init__")

    # def __del__(self):
    #     print("I'm __del__")
    def __call__(self, *args, **kwargs):
        arg = args[0]
        print(f"I'm __call__,{arg}，当对象当作函数执行时会被默认自动调用，即  对象（X）形式")

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

    def __getitem__(self, item):
        '''实例对象可以通过键值来取值。'''

        print(self.n[item])

    def __str__(self):
        return "打印的时候调用，print(对象）形式"

    def __len__(self):
        '''__len__ 方法一般与 len(对象) 方法搭配使用。
        即先在__len__方法中说明需要求类中的哪个属性(假如是属性a)的长度，
        当使用 len(对象A) 方法时会得到对象A的该属性（就是属性a）的长度。'''
        return len(self.n)


test = Test()

test(1)
print(test)

test[2]

l = len(test)
print(l)
iter(test)
for i in range(10):
    print(next(test))
