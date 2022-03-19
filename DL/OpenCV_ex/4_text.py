import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

COLOR = (255, 255, 255)
THICKNESS = 1
SCALE = 1

cv2.putText(img, 'OpenCV', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 100), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 200), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 250), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()