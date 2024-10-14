import pyautogui
import time
import cv2
import pytesseract
from PIL import ImageGrab
import numpy as np
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r'F:\Software\Tesseract\tesseract.exe'
start_time = time.time()
def compare_numbers_in_bbox(bbox):
    # 截取屏幕
    img = ImageGrab.grab(bbox)

    # 转换为 OpenCV 格式
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # 使用 Tesseract OCR 识别文本
    text = pytesseract.image_to_string(img_cv)
    print(text)
    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', text)

    # 如果找到了两个数字，则比较大小
    if len(numbers) >= 2:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        
        if num1 > num2:
            return '>'
        else:
            return '<'
    else:
        print("未找到足够的数字进行比较")

# 定义数字的绘制函数
def draw_number(char, start_x, start_y):
    # 基本长度
    length = 50

    # 设置起始位置
    pyautogui.moveTo(start_x, start_y)

    if char == '>':
        pyautogui.mouseDown()
        pyautogui.dragRel(length, -length,duration=0.2)  # 画上斜线
        pyautogui.dragRel(-length, -length,duration=0.2) # 画下斜线
        pyautogui.mouseUp()
    elif char == '<':
        pyautogui.mouseDown()
        pyautogui.dragRel(-length, -length,duration=0.2) # 斜线向下
        pyautogui.dragRel(length, -length,duration=0.2)# 斜线向上
        pyautogui.mouseUp()
        

def main():

   #time.sleep(2)  # 给用户2秒时间调整鼠标到屏幕上
    start_x = 1560 #int(input("请输入起始X坐标: "))
    start_y = 730 #int(input("请输入起始Y坐标: "))
    bbox = (1432,224,1763, 324)
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse position: ({x}, {y})", end='\r')
            time.sleep(0.1)
            input_char = compare_numbers_in_bbox(bbox)
            draw_number(input_char, start_x, start_y)
    except KeyboardInterrupt:
        print("\n程序中断.")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"程序运行时间: {elapsed_time:.4f} 秒")

if __name__ == "__main__":
    main()