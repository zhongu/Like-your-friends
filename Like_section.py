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


def like_yourfriends():
    if Selector().text("发消息").type("TextView").find():
        Back = Selector().desc("返回").type("ImageView").find()
        Back_rect = Back.rect
        click(click_coordinate(Back_rect))
        time.sleep(0.5)
        print("已返回")
    if FindImages(R(__file__).res("/img/thumb_up_first.png")).confidence(0.95).find_all():
        thumb = FindImages(R(__file__).res("/img/thumb_up_first.png")).confidence(0.95).find_all()
        sorted_I = sorted(thumb, key=lambda x: x['result'][1], reverse=True)
        thumb = sorted_I
        print('一共{}次点赞'.format(len(thumb)))

        for i in range(len(thumb)):
            if Selector().text("发消息").type("TextView").find():
                Back = Selector().desc("返回").type("ImageView").find()
                Back_rect = Back.rect
                click(click_coordinate(Back_rect))
                time.sleep(0.5)
                print("已返回")

            print('进行了第{}次点赞'.format(i + 1))
            # 点击..
            click(thumb[i]['result'][0], thumb[i]['result'][1], 50)
            # 输出中心坐标
            print(thumb[i]['result'])
            print("准备点赞")
            time.sleep(1)

            if Selector().desc("取消点赞").text("取消").find_all() is not None:
                # 判断界面是不是取消点赞界面
                # 是：取消点赞界面
                Cancel_thumb_up = Selector().desc("取消点赞").text("取消").find_all()
                Cancel_thumb_up_rect = Cancel_thumb_up[0].rect
                x = Cancel_thumb_up_rect.left - 200
                y = Cancel_thumb_up_rect.top
                click(x, y, 50)
                print(x, y)  # 输出中心坐标
                print("已经点赞过了")
                time.sleep(0.5)
            else:
                # 否：是点赞界面
                # 图片识别方案
                # thumb_up=FindImages(R(__file__).res("/img/thumb_up_second.png")).confidence(0.8).find_all()
                # click(thumb_up[0]['result'] + (20,))
                # print(thumb_up[0]['result'])
                # 节点树方案
                if Selector().text("赞").desc("赞").type("TextView").find():
                    thumb_up = Selector().text("赞").desc("赞").type("TextView").find()
                    thumb_up_rect = thumb_up.rect

                    click(click_coordinate(thumb_up_rect))
                    print(click_coordinate(thumb_up_rect))  # 输出中心坐标
                    print("点赞成功")
                    time.sleep(0.5)

        # slide(100, 1700, 100, 200, 500)
        touch.down(100, 1700)
        touch.up(200, 500)
        time.sleep(0.5)
        print("向下滑动")
    else:
        time.sleep(0.5)
