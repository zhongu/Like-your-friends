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
from .Friends_Moment_detection import  Moment_detection
from .Like_section import like_yourfriends

cout=20
# 输入你想翻阅朋友圈的页数
Moment_detection()
for j in range(cout):like_yourfriends();

print("结束哩")
R.exit()

