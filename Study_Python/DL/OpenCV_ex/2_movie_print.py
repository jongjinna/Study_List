import cv2

# cap = cv2.VideoCapture('./DL/OpenCV_ex/video.mp4')

# while cap.isOpened():
#   ret, frame = cap.read() # ret: True or False, frame: numpy.ndarray 받아온 이미지(프레임)
#   if not ret:
#     print("there is no frame")
#     break

#   cv2.imshow('video', frame)

#   if cv2.waitKey(1) == ord('q'):
#     print("quit")
#     break

# cap.release()
# cv2.destroyAllWindows() 

cap = cv2.VideoCapture(0)

if not cap.isOpened():
  print("there is no camera")
  exit()

while 1:
  ret, frame = cap.read() # ret: True or False, frame: numpy.ndarray 받아온 이미지(프레임)
  if not ret:
    print("there is no frame")
    break

  cv2.imshow('camera', frame)

  if cv2.waitKey(1) == ord('q'):
    print("quit")
    break
  
cap.release()
cv2.destroyAllWindows() 