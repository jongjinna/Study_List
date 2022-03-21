import cv2
import numpy as np

# img = cv2.imread('./DL/OpenCV_ex/newspaper.jpg')

# width, height = 640, 240

# src = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)
# dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

# matrix = cv2.getPerspectiveTransform(src, dst)
# result = cv2.warpPerspective(img, matrix, (width, height))

# cv2.imshow('img', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.imread('./DL/OpenCV_ex/poker.jpg')

# width, height = 530, 710

# src = np.array([[702, 143], [1133, 413], [726, 1007], [276, 700]], dtype=np.float32)
# dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

# matrix = cv2.getPerspectiveTransform(src, dst)
# result = cv2.warpPerspective(img, matrix, (width, height))

# cv2.imshow('img', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 마우스 이벤트 등록
point_list = []
src_img = cv2.imread('./DL/OpenCV_ex/poker.jpg')

COLOR = (255, 0, 255)
def mouse_handler(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    point_list.append((x,y))
  
  for point in point_list:
    cv2.circle(src_img, point, 15, COLOR, cv2.FILLED)

  if len(point_list) == 4:
    show_result()

  cv2.imshow('img', src_img)

def show_result():
  width, height = 530, 710
  src = np.float32(point_list)
  dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

  matrix = cv2.getPerspectiveTransform(src, dst)
  result = cv2.warpPerspective(src_img, matrix, (width, height))

  cv2.imshow('result', result)
  
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
