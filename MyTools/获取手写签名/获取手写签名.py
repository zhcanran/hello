#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from PIL import Image
import numpy as np

img: Image.Image = Image.open(fp='qian.jpg')
# 转成灰度图
img = img.convert("L")
img_arr = np.array(img)
img_arr = img_arr[:, :, None]
print(img_arr.shape)
# 二值化进行处理
img1 = img.point(lambda i: 255 if i > 150 else 0)
img1.save('黑白签字图.jpg')
img1.show()
