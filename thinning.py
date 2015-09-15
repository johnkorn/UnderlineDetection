    # encoding: utf-8
    # thinning.py
    # Hilditch Thinning Algorithms
    # 2012-3-6
    # Eiichiro Momma
import cv2
import numpy as np
    
class Thinner:
    @staticmethod
    def Thin(image):
        # first invert the image
        img = (255-image)
        
        size = np.size(img)
        skel = np.zeros(img.shape,np.uint8)
 
        element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        done = False
 
        while( not done):
            eroded = cv2.erode(img,element)
            temp = cv2.dilate(eroded,element)
            temp = cv2.subtract(img,temp)
            skel = cv2.bitwise_or(skel,temp)
            img = eroded.copy()
 
            zeros = size - cv2.countNonZero(img)
            if zeros==size:
                done = True
 
        return (255-skel) # return inverted images 