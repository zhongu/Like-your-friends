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


def Moment_detection():
    # 判断是不是在朋友圈里面
    try:
        Find=FindImages(R(__file__).res("/img/thumb_up_first.png")).confidence(0.95).find()
        discover = Selector().text("发现").find()
        discover_rect = discover.rect
        click(click_coordinate(discover_rect))
        # 寻找“发现”，然后进行点击
        time.sleep(0.75)
        circle_of_friends = Selector().text("朋友圈").find()
        circle_of_friends_rect = circle_of_friends.rect
        click(click_coordinate(circle_of_friends_rect))
        print(("不在朋友圈界面"))
        time.sleep(1)
    except:
        print("在朋友圈界面")
