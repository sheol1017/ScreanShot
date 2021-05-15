#!usr/bin/env/python3
#-*- coding: utf-8 -*-
__author__ = 'Michael Shen'

#pip install python-docx
# pip install pynput
# pip install PyAutoGUI
#pip install python-docx
# pip install keyboard
# pip install pillow
# pip install baidu-aip

import keyboard,time,pynput
from PIL import ImageGrab
# from PIL import Image

# BytesIO是操作二进制数据的模块
from io import BytesIO

# pip install pywin32 # win32clipboard是操作剪贴板的模块
import win32clipboard
import math
import pyautogui as pag
'''
结合greenshot来实时截图
F1 截图--》复制--》保存
'''

def move_and_past(hotkeycode,pos_detal=70):
    keyboard.wait(hotkey=hotkeycode)

    time.sleep(0.5)

    #控制鼠标
    ctr = pynput.mouse.Controller()
    #
    ctr.move(0, int(pos_detal))

    time.sleep(0.3)
    #左键单击。
    ctr.click(pynput.mouse.Button.left)
    #此时已经复制到了剪贴板
    ctr.release(pynput.mouse.Button.left)


def Past_content():
    ctr = pynput.keyboard.Controller()

    ctr.press(pynput.keyboard.KeyCode.from_vk(17))
    # 通过按键的映射码 按下ctrl键。

    # ctr.press(pynput.keyboard.Key.shift)
    # 通过按键对象 按下shift键。

    ctr.press('v')
    # 通过长度为1的字符 按下v键。

    # 扫尾，释放刚才按下的键。后面我会说更简单、优雅的办法。
    ctr.release(pynput.keyboard.Key.ctrl)
    # ctr.release(pynput.keyboard.Key.shift)
    ctr.release('v')

    time.sleep(0.3)

    ctr.press(pynput.keyboard.Key.esc)
    ctr.release(pynput.keyboard.Key.esc)

def clik_mouse_left(cent_pos,pos_detal):
    '''
    控制鼠标处理F2，并移动光标，以及移回到原来位置
    :return:
    '''
    #控制鼠标
    ctr = pynput.mouse.Controller()
    (x,y)=pag.position()
    # print((x,y))
    #移动到中心
    ctr.position = (int(cent_pos), y)

    #左键单击。
    ctr.click(pynput.mouse.Button.left)
    time.sleep(0.3)
    ctr1 = pynput.keyboard.Controller()

    ctr1.press(pynput.keyboard.KeyCode.from_vk(0x71)) #F2
    time.sleep(0.3)
    ctr1.release(pynput.keyboard.KeyCode.from_vk(0x71))
    time.sleep(0.3)
    # ctr.click(pynput.mouse.Button.left)
    #0x23
    ctr1.press(pynput.keyboard.KeyCode.from_vk(0x23)) #F2
    time.sleep(0.3)
    ctr1.release(pynput.keyboard.KeyCode.from_vk(0x23))

    #向上移动回原来位置
    ctr.move(0, (0-int(pos_detal)))

def image_resize(picture_width):

    # image = Image.open('haha.jpg')
    (x,y) = image.size
    # print((x,y))
    x_s = int(picture_width)  # define standard width
    y_s = y * x_s / x  # calc height based on standard width
    y_s = math.ceil(y_s)
    # print((x_s, y_s))
    # image = ImageGrab.grabclipboard()
    out = image.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
    out.save('haha.jpg')
    file_image = 'haha.jpg'
    paste_img(file_image)

def send_msg_to_clip(type_data, msg):
    """
    操作剪贴板分四步：
    1. 打开剪贴板：OpenClipboard()
    2. 清空剪贴板，新的数据才好写进去：EmptyClipboard()
    3. 往剪贴板写入数据：SetClipboardData()
    4. 关闭剪贴板：CloseClipboard()

    :param type_data: 数据的格式，
    unicode字符通常是传 win32con.CF_UNICODETEXT
    :param msg: 要写入剪贴板的数据
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(type_data, msg)
    win32clipboard.CloseClipboard()


def paste_img(file_img):
    """
    图片转换成二进制字符串，然后以位图的格式写入剪贴板

    主要思路是用Image模块打开图片，
    用BytesIO存储图片转换之后的二进制字符串

    :param file_img: 图片的路径
    """

    image = Image.open(file_img)
    # 声明output字节对象
    output = BytesIO()

    # 用BMP (Bitmap) 格式存储
    # 这里是位图，然后用output字节对象来存储
    image.save(output, 'BMP')

    # BMP图片有14字节的header，需要额外去除
    data = output.getvalue()[14:]

    # 关闭
    output.close()

    # DIB: 设备无关位图(device-independent bitmap)，名如其意
    # BMP的图片有时也会以.DIB和.RLE作扩展名
    # 设置好剪贴板的数据格式，再传入对应格式的数据，才能正确向剪贴板写入数据
    send_msg_to_clip(win32clipboard.CF_DIB, data)
    pass

def main():
    # picture_width = input('please input the picture width, word is 200 \n')
    picture_width =500
    pos_detal = 70
    cent_pos = 500
    while True:
        #Greenshot get pic in clipboard
        #等待F1 按下
        try:
            move_and_past('F1',pos_detal)
            time.sleep(0.5)
            image= ImageGrab.grabclipboard()
        except IOError:
            print ('Error: F1 出错')
        #如果需要改变图片大小，但是太糊了，还是用word 的宏处理更好
        # image.save('haha.jpg')
        # image_resize(picture_width)

        #保存图片
        try:
            time.sleep(0.5)
            Past_content()
            time.sleep(0.5)
        except IOError1:
            print('Error: 粘贴 出错')

        #移动到原来位置
        try:
            clik_mouse_left(cent_pos,pos_detal)
        except IOError2:
            print('Error: 鼠标移回 出错')
        # print(image)



if __name__ == '__main__':
    main()
