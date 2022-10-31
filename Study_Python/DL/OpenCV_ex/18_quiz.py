# OpenCV를 이용하여 가로로 촬영된 영상을 세로로 회전하는 프로그램 만들기
# 회전: 시계 반대방향으로 90도
# 재생속도: 원본의 4배
# 출력 파일명: city_output.avi(코덱: DIVX)

import cv2

cap = cv2.VideoCapture('DL/OpenCV_ex/city.mp4')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('DL/OpenCV_ex/city_output.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps*4, (height, width))

while cap.isOpened():
  ret, frame = cap.read() # ret: True or False, frame: numpy.ndarray 받아온 이미지(프레임)
  if not ret:
    print("there is no frame")
    break

  # 이미지 회전
  frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
  out.write(frame)
  cv2.imshow('city', frame)

  if cv2.waitKey(1) == ord('q'):
    print("quit")
    break

out.release()
cap.release()
cv2.destroyAllWindows()