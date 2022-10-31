import cv2
import numpy as np

img = cv2.imread('./DL/OpenCV_ex/img.jpg')

crop = img[100:200, 200:400]

img[100:200, 400:600] = crop
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()