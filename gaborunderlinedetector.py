import numpy as np
import cv2
import thinning as thin
import sys,os

print 'started!'
img_fn = 'Arial36Italic'
 
img = cv2.imread(img_fn+'.png')
# make grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# binarize
ret,img_bin = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('binarized.jpg',img_bin) 

# noise removal with CC?

# apply Gabor filter
ksize = 31
sig = 3
theta = np.pi / 2
lm = 8
gm = 0
psi = 0 #np.pi / 2
filtr = cv2.getGaborKernel((ksize, ksize), sig, theta, lm, gm, psi, ktype=cv2.CV_32F)
#filter /= 1.5*filter.sum()
fimg = cv2.filter2D(img_bin, cv2.CV_8UC3, filtr)
 
cv2.imwrite('filtered.jpg',fimg)

# binarize
ret2,img_bin2 = cv2.threshold(fimg,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('binarized2.jpg',img_bin2) 

# remove noise
cont_img = 255-img_bin2
contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)

comp_img = img_bin2.copy()
npall = img_bin2.shape[0] * img_bin2.shape[1];
width = img_bin2.shape[1]
height = img_bin2.shape[0]
print width
print height
np = npall - cv2.countNonZero(img_bin2);
nc = len(contours)
nt = (2*(np/nc))/100
for cnt in contours:
    # reject bad components: delete those which are above mid-line and are not long enough (80% of text line??)
              
    x,y,w,h = cv2.boundingRect(cnt)
    if w>0.8*width and y>height/2:
        #for pnt in cnt:
        #    x = pnt[0][0]
        #    y = pnt[0][1]
        #    img[y,x]=(0,0,255)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)


fname = 'D:/imgs/'+img_fn+'_ulines.jpg'
cv2.imwrite(fname,img)

# thinning
thinned = thin.Thinner.Thin(comp_img)
cv2.imwrite('thinned.jpg',thinned)

print 'finished!' 