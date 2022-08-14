#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def g(n):
    data={}
    def f(m):
        if m<=1:
            return 1
        if m in data:
            return data[m]
        else:
            print(f'计算:{m}')
            v=f(m-1)+f(m-2)
            data[m]=v
            return v
    return f(n)


if __name__ == '__main__':
    g(20)