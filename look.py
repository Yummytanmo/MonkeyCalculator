from pynput import mouse
import time

actions = []

def on_move(x, y):
    actions.append(('move', x, y))

def on_click(x, y, button, pressed):
    if pressed:
        actions.append(('press', x, y, button))
    else:
        actions.append(('release', x, y, button))

def on_scroll(x, y, dx, dy):
    actions.append(('scroll', x, y, dx, dy))

# 开始监听鼠标
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    print("Recording... Move the mouse and click. Press Ctrl+C to stop.")
    try:
        listener.join()
    except KeyboardInterrupt:
        print("Recording stopped.")

# 保存操作到文件
with open('mouse_actions.txt', 'w') as file:
    for action in actions:
        file.write(f"{action}\n")