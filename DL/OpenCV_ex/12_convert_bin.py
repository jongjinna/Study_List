import cv2
from numpy import empty

# img = cv2.imread('./DL/OpenCV_ex/book.jpg', cv2.IMREAD_GRAYSCALE)

# ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('img', img)
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# -------------------------

# def empty(pos):
#   pass

# img = cv2.imread('./DL/OpenCV_ex/book.jpg', cv2.IMREAD_GRAYSCALE)

# name = 'Trackbar'
# cv2.namedWindow(name)

# cv2.createTrackbar('block_size', name, 25, 100, empty)
# cv2.createTrackbar('c', name, 3, 10, empty)

# while 1:
#   block_size = cv2.getTrackbarPos('block_size', name)
#   c = cv2.getTrackbarPos('c', name)

#   if block_size <= 1:
#     block_size = 3
#   if block_size % 2 == 0:
#     block_size += 1
  
#   binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
  
#   cv2.imshow(name, binary)
#   if cv2.waitKey(1) == ord('q'):
#     break

# cv2.destroyAllWindows()

# -------------------------
# 오츠 알고리즘, Bimodal Image 에 활용.
img = cv2.imread('./DL/OpenCV_ex/book.jpg', cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('img', img)
cv2.imshow('binary', binary)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
