# __init__.py 为初始化加载文件
import time

from airscript.node import Selector
from airscript.screen import Screen
from airscript.screen import FindImages
from airscript.screen import Ocr
from airscript.action import click
# 导入系统资源模块
from airscript.system import R
from airscript.action import slide
from airscript.action import touch
# 导入动作模块
from ascript.android import action
# 导入节点检索模块
from ascript.android import node
# 导入图色检索模块
from ascript.android import screen
from airscript.system import R
from .Click_function import click_coordinate
from .Friends_Moment_detection import Moment_detection
from .Like_section import like_yourfriends
from airscript.ui import Window
# from .res.ui import form
import json

def tunnel(k, v):
    if k == "close":
        print(v)  # 用户点X关闭了窗口
    elif k == "res":
        print(v)  # 用户点击确定并回传了数据
        resobj = json.loads(v)
        print(resobj)
        print('次数', resobj['user'])
        cnt = resobj['user']
        count = int(cnt)
        print(count)
        Moment_detection()
        print(1)
        for j in range(count): like_yourfriends();
        print("结束哩")
        R.exit()


formw = Window(R(__file__).ui("form.html"), tunnel)
formw.height("50vh")
formw.show()
formw.drag(True)
# Moment_detection()
# count=20
# for j in range(count): like_yourfriends();
# print("结束哩")
# R.exit()
