import cv2
import pytesseract
from PIL import ImageGrab
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'F:\Software\Tesseract\tesseract.exe'
# 定义截取区域（左, 上, 右, 下）
bbox = (100, 100, 500, 500)

# 截取屏幕
img = ImageGrab.grab(bbox)

# 转换为 OpenCV 格式
img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

# 使用 Tesseract OCR 识别文本
text = pytesseract.image_to_string(img_cv)
print(text)