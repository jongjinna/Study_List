import cv2
import numpy as np

# # img
# # 고정 크기
# img = cv2.imread('./DL/OpenCV_ex/img.jpg')
# img_resize = cv2.resize(img, (400, 500))
# cv2.imshow('img', img)
# cv2.imshow('img_resize', img_resize)

# # 비율
# img_resize = cv2.resize(img, None, fx=0.5, fy=0.5)
# cv2.imshow('img_resize_rate', img_resize)

# # 보간법
# img_resize = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
# cv2.imshow('img_resize_interpolation_area', img_resize)

# img_resize = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
# cv2.imshow('img_resize_interpolation_cubic', img_resize)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# video

cap = cv2.VideoCapture('./DL/OpenCV_ex/video.mp4')
while cap.isOpened():
  ret, frame = cap.read()
  if not ret:
    break
  # # 고정 크기
  # frame_resize = cv2.resize(frame, (400,500))
  # 비율
  frame_resize = cv2.resize(frame, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
  cv2.imshow('video', frame_resize)

  if cv2.waitKey(1) == ord('q'):
    print("quit")
    break

cap.release()
cv2.destroyAllWindows()

