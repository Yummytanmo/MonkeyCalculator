import pyautogui
import time

# 定义数字的绘制函数
def draw_number(char, start_x, start_y):
    # 基本长度
    length = 100

    # 设置起始位置
    pyautogui.moveTo(start_x, start_y)

    if char == '>':
        pyautogui.dragRel(length, length, duration=0.2)  # 斜线向下
        pyautogui.moveRel(-length, 0, duration=0.1)      # 移动到中间
        pyautogui.dragRel(length, -length, duration=0.2) # 斜线向上
    elif char == '<':
        pyautogui.dragRel(-length, length, duration=0.2) # 斜线向下
        pyautogui.moveRel(length, 0, duration=0.1)       # 移动到中间
        pyautogui.dragRel(-length, -length, duration=0.2)# 斜线向上
        

def main():
    input_char = input("请输入符号 ")
    start_x = 300 #int(input("请输入起始X坐标: "))
    start_y = 300 #int(input("请输入起始Y坐标: "))
    time.sleep(2)  # 给用户2秒时间调整鼠标到屏幕上
    draw_number(input_char, start_x, start_y)

if __name__ == "__main__":
    main()