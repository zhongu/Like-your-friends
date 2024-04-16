from airscript.system import R
from airscript.ui import Window
import json

def tunnel(k,v):
    if k =="close":
        print(v) # 用户点X关闭了窗口
    elif k =="res":
        print(v) # 用户点击确定并回传了数据
        resobj = json.loads(v)
        print(resobj)
        print('用户名',resobj['user'])



formw =Window(R(__file__).ui("form.html"),tunnel)
formw.height("70vh")
formw.show()