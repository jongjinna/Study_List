import cv2
import numpy as np

# img = cv2.imread('./DL/OpenCV_ex/newspaper.jpg')

# width, height = 640, 240

# src = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)
# dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

# matrix = cv2.getPerspectiveTransform(src, dst)
# result = cv2.warpPerspective(img, matrix, (width, height))

# cv2.imshow('img', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread('./DL/OpenCV_ex/poker.jpg')

width, height = 530, 710

src = np.array([[702, 143], [1133, 413], [726, 1007], [276, 700]], dtype=np.float32)
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('img', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 마우스 이벤트 등록
