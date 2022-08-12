#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import struct
import os

path = r'D:\project\CNN_project\jobwork\jobwork02\data\MNIST\raw'
data = ['t10k-images-idx3-ubyte', 't10k-labels-idx1-ubyte',
        'train-images-idx3-ubyte', 'train-labels-idx1-ubyte']
train_images_path = os.path.join(path, data[2])
train_labels_path = os.path.join(path, data[3])
test_images_path = os.path.join(path, data[0])
test_labels_path = os.path.join(path, data[1])

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


def load_imges(path):
    with open(path, 'rb') as f:
        data = f.read()
    row, cols = struct.unpack('>ii', data[8:16])
    data = np.asarray(bytearray(data[16:]), dtype=np.float32)
    data = data.reshape((-1, row, cols))
    return data


def load_labels(path):
    with open(path, 'rb') as f:
        labels = f.read()
    labels = np.asarray(bytearray(labels[8:]), dtype=np.float32)
    labels = labels[:, None]
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

    train_datas = load_imges(train_images_path)
    train_labels = load_imges(test_images_path)

    test_datas = load_labels(train_labels_path)
    test_labels = load_labels(test_labels_path)

    img = train_datas[0]

    img = Image.fromarray(img)
    img.show()
