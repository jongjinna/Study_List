from tkinter import font
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image # 한글 이미지 폰트 설정

def myPutText(src, text, pos, font_size, font_color, thickness):
  img_pil = Image.fromarray(src)
  draw = ImageDraw.Draw(img_pil)
  font = ImageFont.truetype("fonts/gulim.ttc", font_size) # 폰트 파일 지정
  draw.text(pos, text, font=font, fill=font_color, stroke_width=thickness)
  return np.array(img_pil)

img = np.zeros((480, 640, 3), np.uint8)

COLOR = (255, 255, 255)
THICKNESS = 1
SCALE = 1

cv2.putText(img, 'OpenCV', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 100), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 200), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, 'OpenCV', (10, 250), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

Font_size = 30
Font_color = (255, 255, 255)
# img = myPutText(img, '한글예시', (10, 350), Font_size, Font_color, THICKNESS)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()