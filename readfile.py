# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:55:02 2017

@author: Necromancer
"""
#可以读取txt文件，每行的数据形式为  a，b  其中a，b均为小数
#一维数组需要修改shape，使它成为 n*1 或 1*n 然后再做处理

import numpy as np
import matplotlib.pyplot as plt

filename = 'd:\ex1\ex1data1.txt'

x = []
y = []

with open(filename,'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
            pass
        x_tmp,y_tmp = [float(i) for i in lines.split(",")]
        x.append(x_tmp)
        y.append(y_tmp)
        pass
    x = np.array(x)
    y = np.array(y)
    pass
x.shape = (97,1)
x = np.transpose(x)
y.shape = (97,1)
y = np.transpose(y)

training_data = np.concatenate((x,y),axis =0)

print(training_data.shape)

plt.xlim(np.min(x),np.max(x))
plt.ylim(np.min(y),np.max(y))
plt.plot(x,y,'o')