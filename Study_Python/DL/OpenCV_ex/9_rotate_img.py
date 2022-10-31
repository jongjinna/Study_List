import cv2

img = cv2.imread('./DL/OpenCV_ex/img.jpg')

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)


cv2.imshow('img', img)
cv2.imshow('rotate_90', rotate_90)
cv2.imshow('rotate_180', rotate_180)
cv2.imshow('rotate_270', rotate_270)

cv2.waitKey(0)
cv2.destroyAllWindows()