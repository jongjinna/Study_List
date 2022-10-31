import cv2

def empty(pos):
  pass

img = cv2.imread('./DL/OpenCV_ex/snowman.png')

name = 'TrackBar'
cv2.namedWindow(name)
cv2.createTrackbar('threshold1', name, 0, 255, empty)
cv2.createTrackbar('threshold2', name, 0, 255, empty)

while 1:
  threshold1 = cv2.getTrackbarPos('threshold1', name)
  threshold2 = cv2.getTrackbarPos('threshold2', name)
  edges = cv2.Canny(img, threshold1, threshold2)
  cv2.imshow('img', img)
  cv2.imshow(name, edges)

  if cv2.waitKey(1) == ord('q'):
    break

cv2.waitKey(0)
cv2.destroyAllWindows()