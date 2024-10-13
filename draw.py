import pyautogui
import time

# 定义数字的绘制函数
def draw_number(char, start_x, start_y):
    # 基本长度
    length = 50

    # 设置起始位置
    pyautogui.moveTo(start_x, start_y)

    if char == '0':
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, length, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
        pyautogui.dragRel(0, -length, duration=0.2)
    elif char == '1':
        pyautogui.moveTo(start_x + length // 2, start_y)
        pyautogui.dragRel(0, length, duration=0.2)
    elif char == '2':
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, length // 2, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
        pyautogui.dragRel(0, length // 2, duration=0.2)
        pyautogui.dragRel(length, 0, duration=0.2)
    elif char == '3':
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, length, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
        pyautogui.moveRel(length, 0)
        pyautogui.dragRel(0, length, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
    elif char == '4':
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragRel(0, length // 2, duration=0.2)
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, length // 2, duration=0.2)
        pyautogui.moveTo(start_x + length, start_y)
        pyautogui.dragRel(0, length, duration=0.2)
    elif char == '5':
        pyautogui.moveTo(start_x + length, start_y)
        pyautogui.dragRel(-length, 0, duration=0.2)
        pyautogui.dragRel(0, length // 2, duration=0.2)
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, length // 2, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
    elif char == '6':
        pyautogui.moveTo(start_x + length, start_y)
        pyautogui.dragRel(-length, 0, duration=0.2)
        pyautogui.dragRel(0, length, duration=0.2)
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, -length // 2, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
    elif char == '7':
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(-length, length, duration=0.2)
    elif char == '8':
        pyautogui.dragRel(length, 0, duration=0.2)
        pyautogui.dragRel(0, length, duration=0.2)
        pyautogui.dragRel(-length, 0, duration=0.2)
        pyautogui.dragRel(0, -length, duration=0.2)
        pyautogui.moveRel(0, length // 2)
        pyautogui.dragRel(length, 0, duration=0.2)
    if char == '9':
        pyautogui.dragRel(length, 0, duration=0.2)       # 上部横线
        pyautogui.dragRel(0, length, duration=0.2)       # 右侧竖线
        pyautogui.dragRel(-length, 0, duration=0.2)      # 中部横线
        pyautogui.dragRel(0, -length, duration=0.2)      # 回到上部
        pyautogui.dragRel(length, 0, duration=0.2)       # 右侧小弧线
        pyautogui.dragRel(0, length // 2, duration=0.2)  # 下侧竖线
        pyautogui.dragRel(-length, 0, duration=0.2)      # 下部横线

def main():
    input_char = input("请输入一个数字 (0-9): ")
    start_x = 300 #int(input("请输入起始X坐标: "))
    start_y = 300 #int(input("请输入起始Y坐标: "))
    time.sleep(2)  # 给用户2秒时间调整鼠标到屏幕上
    draw_number(input_char, start_x, start_y)

if __name__ == "__main__":
    main()