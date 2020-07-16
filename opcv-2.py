import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')
aa = img[100:300,100:300]
bb = img[300:500,300:500]
dst = cv2.addWeighted(aa,0.7,bb,0.6,0)

img[200:400,200:400]=dst
# plt.imshow(img,cmap = 'pink',interpolation='bicubic')
# plt.xticks([]),plt.yticks([])
# plt.show()

cv2.imshow('show',img)
cv2.waitKey(0)
cv2.destroyAllWindows()