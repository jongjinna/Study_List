import cv2
import numpy as np

# 480 x 640 x 3
img = np.zeros((480, 640, 3), np.uint8)
# img[:] = (255,255,255) # BGR

# 사각형
img[100:200, 200:300] = (255, 255, 255)

# 직선
COLOR = (0, 255, 255)
THICKNESS = 1

cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50, 200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50, 300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)

# 원
COLOR = (255, 255, 0)
RADIUS = 50
THICKNESS = 10

cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

# 사각형
COLOR = (0, 255, 0)
THICKNESS = 3

cv2.rectangle(img, (100, 100), (200, 200), COLOR, THICKNESS, cv2.LINE_AA)
cv2.rectangle(img, (300, 100), (400, 300), COLOR, cv2.FILLED, cv2.LINE_AA)

# 다각형
COLOR = (0, 0, 255)
THICKNESS = 3

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])

# cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA)

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)


cv2.imshow('img', img)

cv2.waitKey(0)

cv2.destroyAllWindows()