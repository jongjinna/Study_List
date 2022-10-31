import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)

img = cv2.imread('./DL/OpenCV_ex/book.jpg', cv2.IMREAD_GRAYSCALE)

O_erode = cv2.erode(img, kernel, iterations=3)
O_dilate = cv2.dilate(O_erode, kernel, iterations=3)
C_dilate = cv2.dilate(img, kernel, iterations=3)
C_erode = cv2.erode(C_dilate, kernel, iterations=3)

cv2.imshow('img', img)
cv2.imshow('opening', O_dilate)
cv2.imshow('closing', C_erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
