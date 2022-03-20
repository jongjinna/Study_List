import cv2
import numpy as np


cap = cv2.VideoCapture(0)

if not cap.isOpened():
  print("there is no camera")
  exit()

while 1:
  ret, frame = cap.read() # ret: True or False, frame: numpy.ndarray 받아온 이미지(프레임)
  if not ret:
    print("there is no frame")
    break

  # frame = frame[200:520, 500:780]
  cv2.imshow('camera', frame)

  if cv2.waitKey(1) == ord('q'):
    print("quit")
    break
  
cap.release()
cv2.destroyAllWindows() 