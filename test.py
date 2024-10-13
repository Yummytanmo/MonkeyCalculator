import cv2
import pytesseract
from PIL import ImageGrab
import numpy as np
import pytesseract
import re

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

# 检查并计算简单的加法计算式
def calculate_expression(expression):
    try:
        # 使用 eval 计算表达式（仅限简单计算）
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error calculating expression: {e}"

# 正则表达式匹配简单计算式
expression_pattern = r"^\d+\s*[\+\-\*/]\s*\d+$"

# 去除空白并检查文本是否为计算式
cleaned_text = text.strip().replace(' ', '')
if re.match(expression_pattern, cleaned_text):
    result = calculate_expression(cleaned_text)
    print(f"Result: {result}")
else:
    print(text)