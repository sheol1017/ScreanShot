#  *_* coding:utf8 *_*
# pip install baidu-aip
#http://ai.baidu.com/
from aip import AipOcr
from ctypes import windll, c_int

""" 你的 APPID AK SK """
# APP_ID = "24174622"
# API_KEY = "1y3LsKY1B7Iu04j8139mWn3Z"
# SECRET_KEY = "AR6R8U6LTrGgCzQLGrFOUSGzQGXcW7cc"

APP_ID = "24190335"
API_KEY = "D6MUgaQ2btyHkVcv5Cx9ekBI"
SECRET_KEY = "zgXWd6Utmf1tABwGpjn1gdbQyo0maqDT"

ScreenCapture_client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def empty_clipboard():
    # c_int(0)  窗口句柄参数  把大象装进冰箱 4步 （买冰箱 获取user32）
    user32 = windll.user32
    user32.OpenClipboard(c_int(0))
    user32.EmptyClipboard()
    user32.CloseClipboard()


def get_text_from_image(image_path_or_bytes):
    if isinstance(image_path_or_bytes, bytes):
        image = image_path_or_bytes
    else:
        with open(image_path_or_bytes, "rb") as f:
            image = f.read()

    result_data = ScreenCapture_client.basicAccurate(image)
    # print(result_data)
    result_str = ""
    if result_data["words_result"]:
        for data in result_data["words_result"]:
            result_str += data["words"]
    else:
        # print(result_data)
        result_str = "未检测到任何文本内容"
    return result_str
