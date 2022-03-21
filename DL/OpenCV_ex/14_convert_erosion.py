import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)

img = cv2.imread('./DL/OpenCV_ex/book.jpg', cv2.IMREAD_GRAYSCALE)
erode1 = cv2.erode(img, kernel, iterations=1)
erode2 = cv2.erode(img, kernel, iterations=2)
erode3 = cv2.erode(img, kernel, iterations=3)

cv2.imshow('img', img)
cv2.imshow('erode1', erode1)
cv2.imshow('erode2', erode2)
cv2.imshow('erode3', erode3)
cv2.waitKey(0)
cv2.destroyAllWindows()