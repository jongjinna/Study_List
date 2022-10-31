from sympy import python
import cv2

img = cv2.imread('./DL/OpenCV_ex/img.jpg')
img_color = cv2.imread('./DL/OpenCV_ex/img.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('./DL/OpenCV_ex/img.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('./DL/OpenCV_ex/img.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('cat_img', img)
cv2.imshow('cat_img_color', img_color)
cv2.imshow('cat_img_gray', img_gray)
cv2.imshow('cat_img_unchanged', img_unchanged)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()

print(img.shape) # (Height, Weight, Channel)
