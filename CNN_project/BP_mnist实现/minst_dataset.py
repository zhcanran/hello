#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import struct
import os

# 32位整数=4个字节
'''
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number      32位，4个字节，表示的是2051
0004     32 bit integer  60000            number of images  多少个图像
0008     32 bit integer  28               number of rows    行数
0012     32 bit integer  28               number of columns 列数
0016     unsigned byte   ??               pixel             具体像素值
0017     unsigned byte   ??               pixel

struct库相关参数
https://blog.csdn.net/qq_30638831/article/details/80421019
'''


class Mnist_dataset:
    def __init__(self, path, train=True):
        data = ['t10k-images-idx3-ubyte', 't10k-labels-idx1-ubyte',
                'train-images-idx3-ubyte', 'train-labels-idx1-ubyte']

        img, label = (data[2], data[3]) if train else (data[0], data[1])
        self.datas = self.load_imges(os.path.join(path, img))
        self.labels = self.load_labels(os.path.join(path, label))
        self.datas=self.datas/255-0.5

    def __getitem__(self, item):
        return self.datas[item], self.labels[item]

    def __len__(self):
        return len(self.datas)

    @staticmethod
    def load_imges(path):
        with open(path, 'rb') as f:
            data = f.read()
        row, cols = struct.unpack('>ii', data[8:16])
        data = np.asarray(bytearray(data[16:]), dtype=np.float32)
        data = data.reshape((-1, row*cols))
        return data

    @staticmethod
    def load_labels(path):
        with open(path, 'rb') as f:
            labels = f.read()
        labels = np.asarray(bytearray(labels[8:]), dtype=np.float32)
        return labels


if __name__ == '__main__':
    # # print(np.array([1,2,3]))
    # with open(train_images_path, 'rb') as f:
    #     train_data = f.read()
    # #< > 指的是读取顺序
    # # print(hex(struct.unpack('>i', train_data[:4])[0]))#16进制与上述注释一致
    # # data = struct.unpack('>iiii', train_data[:16])  # i代表一个数-->4个字符
    #
    # data=np.asarray(bytearray(train_data[16:]),dtype=np.int8)
    # print(data)
    path = r'D:\project\CNN_project\jobwork\jobwork02\data\MNIST\raw'
    data = Mnist_dataset(path)
    #
    # for i in data:
    #     print(i)
    #     break
