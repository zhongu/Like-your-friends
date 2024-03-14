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


# 函数名称：点击坐标
class Rect:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom


def click_coordinate(rect1):
    return (rect1.left + rect1.right) / 2, (rect1.top + rect1.bottom) / 2, 20


# 点击的传入坐标，rect1为传入的范围坐标

nickname = "麻包忠"
# 判断是不是在朋友圈里面
if FindImages(R(__file__).res("/img/thumb_up_first.png")).confidence(0.95).find() is None:
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
else:
    print("在朋友圈界面")


result_friends = Selector(1).text(nickname).find()
if result_friends:
 #   print(result_friends)
    print("在朋友圈界面")




for j in range(3):
    thumb = FindImages(R(__file__).res("/img/thumb_up_first.png")).confidence(0.95).find_all()
    for i in range(len(thumb)) :

        print('一共{}次点赞'.format(len(thumb)))
        print('还剩{}次点赞'.format(i+1))
        click(thumb[i]['result'] + (50,))
        print(thumb[i]['result'])  # 输出中心坐标
        print("准备点赞")
        time.sleep(1.25)

        if Selector().desc("取消点赞").text("取消").find_all() is not None:
            #判断界面是不是取消点赞界面
            #是：取消点赞界面
            Cancel_thumb_up=Selector().desc("取消点赞").text("取消").find_all()
            Cancel_thumb_up_rect=Cancel_thumb_up[0].rect
            x=Cancel_thumb_up_rect.left-200
            y=Cancel_thumb_up_rect.top
            click(x,y,20)
            print(x,y)#输出中心坐标
            print("已经点赞过了")
            time.sleep(1.25)

        else:
            #否：是点赞界面

            # thumb_up=FindImages(R(__file__).res("/img/thumb_up_second.png")).confidence(0.8).find_all()
            # click(thumb_up[0]['result'] + (20,))
            # print(thumb_up[0]['result'])
            # 节点树方案
            thumb_up=Selector().text("赞").desc("赞").type("TextView").find()
            thumb_up_rect=thumb_up.rect
            click(click_coordinate(thumb_up_rect))
            print(click_coordinate(thumb_up_rect))#输出中心坐标
            print("点赞成功")
            time.sleep(1.25)
    slide(100,1700,100,200,500)
    time.sleep(3)
    print(j)

