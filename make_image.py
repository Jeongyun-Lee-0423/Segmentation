# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:33:24 2020

@author: jeong
"""


import numpy as np
import os
import cv2 as cv



for image_num in range(0,100):
    data = np.random.randint(100,125, size = 256*256 , dtype = np.uint8)
    data = np.reshape(data, (256,256))
    label_data = np.zeros((256,256), dtype = np.uint8)
    
    for defect_num in range(1,3):
        size_x = np.random.randint(8,64, size = 1 , dtype = np.uint8)
        size_y = np.random.randint(8,64, size = 1 , dtype = np.uint8)
        x = np.random.randint(0,256-size_x[0], size = 1 , dtype = np.uint8)
        y = np.random.randint(0,256-size_y[0], size = 1 , dtype = np.uint8)
        defect_contrast = np.random.randint(3,4, size = 1 , dtype = np.uint8)
        
        
        for col in range(x[0], x[0]+size_x[0]):
            for row in range(y[0],y[0]+size_y[0]):
                data[row][col] = np.random.randint(100 + defect_contrast[0],125 + defect_contrast[0], size = 1 , dtype = np.uint8)
                label_data[row][col] =255
        
     
    cv.imwrite("D:/WORKPLACE/make_image/test/" +str(image_num) + ".png",data)  
    cv.imwrite("D:/WORKPLACE/make_image/test/label/" +str(image_num) + ".png",label_data)    
    #cv.imwrite("D:/WORKPLACE/make_image/train/image/" +str(image_num) + ".png",data)
    #cv.imwrite("D:/WORKPLACE/make_image/train/label/" +str(image_num) + ".png",label_data)
   # cv.imshow("test",data)
