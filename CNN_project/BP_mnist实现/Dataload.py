#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import random


class Mnist_Dataload:
    def __init__(self, datasets, batch_size=32, shuffle=False):
        self.datasets = datasets
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.cursor = 0  # 计数器
        self.datasets = datasets
        self.batch_size = batch_size
        self.lendata = len(self.datasets)
        self.index = list(range(self.lendata))
        if shuffle:
            random.shuffle(self.index)

    def __iter__(self):
        return Mnist_DataLoaderIterator(self.datasets, self.batch_size, self.shuffle)


class Mnist_DataLoaderIterator:
    def __init__(self, datasets, batch_size=32, shuffle=False):
        self.cursor = 0  # 计数器
        self.datasets = datasets
        self.batch_size = batch_size
        self.lendata = len(self.datasets)
        self.index = list(range(self.lendata))
        if shuffle:
            random.shuffle(self.index)

    def __next__(self):
        if self.cursor >= self.lendata:
            raise StopIteration()

        batch_data = []
        remain = min(self.batch_size, self.lendata - self.cursor)  # 256, 128

        for i in range(remain):
            index = self.index[self.cursor]  # 按顺序拿到数据的索引值
            data = self.datasets[index]

            # 如果batch没有初始化，则初始化n个list成员
            if len(batch_data) == 0:
                batch_data = [[] for i in range(len(data))]

            # 直接append进去
            for index, item in enumerate(data):
                batch_data[index].append(item)
            self.cursor += 1
        # 通过np.vstack一次性实现合并，而非每次一直在合并
        for index in range(len(batch_data)):
            batch_data[index] = np.vstack(batch_data[index])
        return batch_data
