将视频按帧存储，转换为numpy数组
import numpy as np
import cv2

cap = cv2.VideoCapture('d:\source.avi')
count = 0
big_array = []
flag,frame = cap.read()
big_array = frame
while(flag):
    flag, frame = cap.read()
    if flag == True:
        count += 1
        print(frame.shape)
        big_array = np.append(big_array,frame,axis=2)
print(count)
print(big_array.shape)

