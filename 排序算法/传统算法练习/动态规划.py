#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#f菲波那挈
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

# 最长路径问题
def max_distine(arr):
    '''
    arr[i][j]就表示第i行第j列，从arr[i][j]只能到arr[i+1][j]和arr[i+1][j+1]
    f(i,j)=arr[i][j]+max(f(i+1,j),f(i+1,j+1)
    '''
    n=len(arr)-1
    def f(i,j):
        if i==n:
            return arr[i][j]
        else:
            print(f'计算：{i}-{j}')
            left=f(i+1,j)
            right=f(i+1,j+1)
            return arr[i][j]+max(left,right)
    return f(0,0)

def max_distine2(arr):
    '''
    arr[i][j]就表示第i行第j列，从arr[i][j]只能到arr[i+1][j]和arr[i+1][j+1]
    f(i,j)=arr[i][j]+max(f(i+1,j),f(i+1,j+1)
    '''
    n=len(arr)-1
    max_dis=[[ -1 for j in range(n+1)]for i in range(n+1)]
    def f(i,j):
        if max_dis[i][j]!=-1:
            return max_dis[i][j]
        if i==n:
            return arr[i][j]
        else:
            print(f'计算：{i}-{j}')
            left=f(i+1,j)
            right=f(i+1,j+1)
            dist= arr[i][j]+max(left,right)
            max_dis[i][j]=dist
            return  dist
    return f(0,0)
if __name__ == '__main__':
    # g(20)
    D=[
        [7],
        [3,8],
        [8,1,0],
        [2,7,4,4],
        [4,5,2,6,5]
    ]
    print(max_distine(D))
    print(max_distine2(D))
    print('haha')
