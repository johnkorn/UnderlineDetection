import numpy as np
import cv2
import matplotlib.pyplot as plt

print 'started!'
img_fn = 'Document_line'
 
img = cv2.imread(img_fn+'.png')
# make grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# binarize
ret,img_bin = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
(h, w) = img_bin.shape[:2]

a = 1 - np.array(img_bin)/255
#a.shape(2000, 2000)
b = a.sum(1) # or 1 depending on the axis you want to sum across
t = np.arange(0, h, 1)
grad = np.gradient(b)

max = np.max(b)
ul = 9
bl = 19
mid = 14
print max

fig,ax = plt.subplots()
# Plot the data
ax.bar(t, b, 1, color="blue")
# Plot the average line
grad_line = ax.plot(t,grad, label='Grad', linestyle='--')
plt.axis([0, h, 0, 200])
plt.show()