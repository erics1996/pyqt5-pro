"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: FirstMainWindow.py
@time: 2020/11/17 上午9:50
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterMainWin(QMainWindow):
    def __init__(self):
        """
        初始化
        :param parent:控件放到parent
        """
        super(CenterMainWin, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle('窗口居中')
        # 设置窗口的尺寸
        self.resize(400, 300)
        # 获取当前的状态栏(默认是有状态栏的)
        self.status = self.statusBar()
        # 设置状态栏显示的消息(消息只存在5s)
        self.status.showMessage('只显示5s的消息！', 5000)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        left = (screen.width() - size.width()) / 2
        top = (screen.height() - size.height()) / 2
        # 移动窗口
        self.move(left, top)


if __name__ == '__main__':
    # 创建一个应用程序对象(传入参数)
    app = QApplication(sys.argv)
    # 设置应用程序的图标
    app.setWindowIcon(QIcon('../images/Dragon.ico'))
    # 创建窗口类的对象
    main = CenterMainWin()
    # 显示窗口
    main.show()
    # 窗口居中
    main.center()
    # 调用exit()进入程序的主循环
    sys.exit(app.exec_())
