import cv2
import numpy as np

# # save image
# img = cv2.imread('DL/OpenCV_ex/img.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# result = cv2.imwrite('DL/OpenCV_ex/img_save.jpg', img) # 저장 포맷 변경 가능
# print(result)

# save video
cap = cv2.VideoCapture('DL/OpenCV_ex/video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 정의

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('DL/OpenCV_ex/video_save.avi', fourcc, fps, (width, height))

while cap.isOpened():
  ret, frame = cap.read()
  if not ret:
    break
  
  out.write(frame)
  cv2.imshow('frame', frame)
  if cv2.waitKey(1) & ord('q'):
    break

out.release()
cap.release()
cv2.destroyAllWindows()