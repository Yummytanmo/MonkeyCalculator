import pyautogui
import time

# 等待几秒钟以便切换到绘画应用程序
time.sleep(5)

# 定义要绘制的数字和符号的形状
# 这里以绘制数字1为例
def draw_one(start_x, start_y, size):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragRel(0, size, duration=0.5)  # 画竖线

# 定义一个函数来控制绘画区域
def draw_in_area():
    # 指定区域的起始坐标和大小
    start_x = 500
    start_y = 400
    size = 100

    # 在指定区域内绘制数字1
    draw_one(start_x, start_y, size)

draw_in_area()