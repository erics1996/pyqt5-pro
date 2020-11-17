"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: WindowAndApplicationIcon.py
@time: 2020/11/17 上午11:33
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        """
        初始化
        :param parent:控件放到parent
        """
        super(FirstMainWin, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle('第一个窗口应用')
        # 设置窗口的尺寸
        self.resize(400, 300)
        # 获取当前的状态栏(默认是有状态栏的)
        self.status = self.statusBar()
        # 设置状态栏显示的消息(消息只存在5s)
        self.status.showMessage('只显示5s的消息！', 5000)


if __name__ == '__main__':
    # 创建一个应用程序对象(传入参数)
    app = QApplication(sys.argv)
    # 设置应用程序的图标
    app.setWindowIcon(QIcon('../images/Dragon.ico'))
    # 创建窗口类的对象
    main = FirstMainWin()
    # 显示窗口
    main.show()
    # 调用exit()进入程序的主循环
    sys.exit(app.exec_())

"""
同时设置窗口坐标和位置
window中会显示窗口图标，只能在标题栏左上角显示图标

"""