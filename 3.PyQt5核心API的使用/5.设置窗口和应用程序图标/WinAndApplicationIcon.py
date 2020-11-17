"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: WinAndApplicationIcon.py.py
@time: 2020/11/17 上午11:33
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class WinAndApplicationIcon(QMainWindow):
    def __init__(self):
        super(WinAndApplicationIcon, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        # 同时设置主窗口的尺寸和位置
        self.setGeometry(400, 400, 300, 200)
        # 设置窗口图标
        self.setWindowIcon(QIcon('../images/Basilisk.ico'))


if __name__ == '__main__':
    # 创建一个应用程序对象(传入参数)
    app = QApplication(sys.argv)
    # 设置应用程序的图标
    app.setWindowIcon(QIcon('../images/Dragon.ico'))  # 可以用来设置主窗口的图标和应用程序的图标，但是如果主窗口已经设置了的图标，这里只能用于设置应用程序的图标
    # 创建窗口类的对象
    main = WinAndApplicationIcon()
    # 显示窗口
    main.show()
    # 调用exit()进入程序的主循环
    sys.exit(app.exec_())

"""
同时设置窗口坐标和位置
window中会显示窗口图标，只能在标题栏左上角显示图标

"""
