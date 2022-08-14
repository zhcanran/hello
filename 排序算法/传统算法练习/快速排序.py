#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def sorted(arr, start, end):
    if arr is None:
        return
    n = end - start
    if n < 2:
        return
    pivot = arr[start]  # 基准
    i = start + 1  # 第一个比基准大的索引
    j = start + 1  # 遍历所有元素的索引

    while j < end:
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    sorted(arr, start, i - 1)
    sorted(arr, i, end)


if __name__ == '__main__':
    _arr = [1, 3, 5, 7, 9, 2, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 32, 56, 77]
    sorted(_arr, 0, len(_arr))
    print(_arr)
