#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
一直递归画分左右，画分足够小，然后再左右均为有顺序列表，然后判断元素大小合并
'''


# 升序排列
def sorted(arr):
    if arr is None:
        return []
    n = len(arr)
    if n == 0:
        return []
    if n == 1:
        return arr
    mid = n // 2
    left = sorted(arr[:mid])
    right = sorted(arr[mid:])
    result = []
    i = 0
    j = 0
    left_n = len(left)
    right_n = len(right)
    while i < left_n and j < right_n:
        left_v = left[i]
        right_v = right[j]
        if left_v == right_v:
            result.append(left_v)
            result.append(right_v)
            i += 1
            j += 1
        elif left_v > right_v:
            result.append(right_v)
            j += 1
        else:
            result.append(left_v)
            i += 1
    while i < left_n:
        result.append(left[i])
        i += 1
    while j < right_n:
        result.append(right[j])
        j += 1
    return result


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 32, 56, 77]
    print(sorted(arr))
