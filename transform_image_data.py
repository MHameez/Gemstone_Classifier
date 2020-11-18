#!/usr/bin/env python
# coding: utf-8

# In[114]:


import cv2
import os
import glob
import numpy as np
import matplotlib.pyplot as plt


# In[118]:


input_path = 'C:/Users/Hameez/.conda/envs/gemstone_dataset/Data/Test/'
output_path = 'C:/Users/Hameez/.conda/envs/gemstone_dataset/Data/Cropped/Test/'


# In[123]:


def centre_crop(img, crop_percent):
    "Takes an Image and the crop the centre of the image based"
    "percentage removed from all four edges of the image"
    img = cv2.imread(img)
    x = img.shape
    remove = crop_percent/100
    x1 = int(x[0] * remove)
    x2 = int(x[0] * (1-remove))
    imgCropped = img[x1:x2,x1:x2]
    
    return imgCropped

# imgCropped = centre_crop(img, 25)
# plt.title("Cropped")
# plt.imshow(imgCropped)


# In[122]:



rootdir = input_path

for subdir, dirs, files in os.walk(rootdir):
#create sub folders for cropped images
    for d in dirs:
        new_sub_fold = output_path + d
        if not os.path.exists(new_sub_fold):
            os.makedirs(new_sub_fold)

#crop and save images to new directory
for subdir2, dirs2, files2 in os.walk(rootdir):
    for file in files2: 
        inp = os.path.join(subdir2, file)
        out_fold = os.path.basename(subdir2)
        img = cv2.imread(inp)
        imgCropped = centre_crop(img, 25)
        cv2.imwrite(output_path+out_fold+'/'+os.path.basename(inp), imgCropped) 
       
        


# In[ ]:




