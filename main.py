import cv2 
import os
import numpy as np
import load
import stackImages

prefix_path = 'source'
path1 = os.path.join(prefix_path, '01')

img = load.Load_Image(path1)

stack_image = stackImages.stackImages(scale=0.5, imgArray=img)

cv2.imshow("windows_name", stack_image)
cv2.waitKey(0)
