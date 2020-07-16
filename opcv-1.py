
import cv2
import numpy as np
img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('open1', img)
cv2.imshow('open', img)  # ''是開啟名稱 讓照片show出來
cv2.waitKey(0)  # 讓show出來的時間停留
cv2.destroyAllWindows()  # 當開啟兩個以上的視窗 按空白鍵可以全部關閉
