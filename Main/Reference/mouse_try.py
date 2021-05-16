#!usr/bin/env/python3
#-*- coding: utf-8 -*-
__author__ = 'Michael Shen'

# pip install pynput
'''
监听、操作鼠标、键盘是实现自动化的捷径，比如我实现自动化签到用到了模拟键盘操作。
https://www.cnblogs.com/tobe-goodlearner/archive/2020/05/17/tutorial-pynput.html
'''
import pynput
ctr = pynput.mouse.Controller()
# ctr.move(0, 50)
ctr.position = (500, 500)
'''
examples:

ctr.position = (500, 500)

ctr.press(pynput.mouse.Button.left)
#按下左键。

ctr.move(50, 0)
#右移50单位。

ctr.move(0, 50)
#下移50单位。

ctr.release(pynput.mouse.Button.left)
#释放左键。

ctr = pynput.mouse.Controller()

ctr.click(pynput.mouse.Button.left)
#左键单击。

ctr.click(pynput.mouse.Button.left, 2)
#左键双击。

ctr.click(pynput.mouse.Button.right)
#右键单击。
'''
with pynput.mouse.Events() as event:
    for i in event:
        # 迭代用法。
        if isinstance(i, pynput.mouse.Events.Move):
            # 鼠标移动事件。
            print(i.x, i.y)
            # 不要直接打印`i`，模块这里有问题，会报错。

        elif isinstance(i, pynput.mouse.Events.Click):
            # 鼠标点击事件。
            print(i.x, i.y, i.button, i.pressed)
            # 这个i.button就是上文所说的“鼠标按键”中的一个，用is语句判断即可。

        elif isinstance(i, pynput.mouse.Events.Scroll):
            # 鼠标滚轮。
            print(i.x, i.y, i.dx, i.dy)

        break

with pynput.keyboard.Events() as event:
    for i in event:
        # 迭代用法。
        key_event = i
        break

    key_event = event.get()
    # get用法。
    # 可以提供一个实数作为最长等待时间（单位秒），超过这个时间没有事件，
    # 就会报错。错误类型是queue模块的Empty，而非TimeoutError。

# 判断事件情况：

if isinstance(key_event, pynput.keyboard.Events.Press):
    print('按下按键', end='')
elif isinstance(key_event, pynput.keyboard.Events.Release):
    print('松开按键', end='')

# 判断按键：

# *这个事件的`key`属性*对应才是*Listener方法获得的按键`'key'`*。

try:
    print(key_event.key.name)
except AttributeError:
    # 说明这个是普通按键。
    print(key_event.key.char)
else:
    # 两种判断方式，第一种是我自创的，第二种是官网上的。
    if (key_event.key.name).startswith('ctrl'):
        # 通过名称判断。
        print('发生了ctrl键事件。')
    elif key_event.key is pynput.keyboard.Key.esc:
        print('发生了esc键事件。')




'''
另一种方法，也可以
'''
import pyautogui,sys
# pip install PyAutoGUI

'''
安装pyautogui库
我们可以先安装一下 pyauogui 这个库，通过它你就可以写一些 Python 脚本来控制你的鼠标和键盘了，
比如你可以定义鼠标在哪个位置点击，定义键盘在什么时候输入什么内容等

鼠标的位置就可以通过 position 方法获取
'''