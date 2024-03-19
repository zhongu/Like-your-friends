class Rect:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom


def click_coordinate(rect1):
    return (rect1.left + rect1.right) / 2, (rect1.top + rect1.bottom) / 2, 40

# 点击的传入坐标，rect1为传入的范围坐标
