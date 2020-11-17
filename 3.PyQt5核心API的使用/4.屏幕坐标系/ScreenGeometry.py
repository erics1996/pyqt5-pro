"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: ScreenGeometry.py
@time: 2020/11/17 上午11:15
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def on_click_btn():
    """
    单击button打印窗口的坐标和宽度和高度
    :return:
    """
    print('onclick')
    print('------1------')
    print('widget.x() = %d' % widget.x())  # 窗口横坐标
    print('widget.y() = %d' % widget.y())  # 窗口纵坐标
    print('widget.width() = %d' % widget.width())  # 工作区宽度
    print('widget.height() = %d' % widget.height())  # 工作去高度
    print('------2------')
    print('widget.geometry().x() = %d' % widget.geometry().x())  # 工作区横坐标
    print('widget.geometry().y() = %d' % widget.geometry().y())  # 工作区纵坐标
    print('widget.geometry().width() = %d' % widget.geometry().width())  # 工作区宽度
    print('widget.geometry().height() = %d' % widget.geometry().height())  # 工作区高度
    print('------3------')
    print('widget.geometry().x() = %d' % widget.frameGeometry().x())  # 窗口横坐标
    print('widget.geometry().y() = %d' % widget.frameGeometry().y())  # 窗口纵坐标
    print('widget.geometry().width() = %d' % widget.frameGeometry().width())  # 窗口宽度
    print('widget.geometry().height() = %d' % widget.frameGeometry().height())  # 窗口高度（包括标题栏）


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 使用Qwigit创建窗口
    widget = QWidget()
    # 在窗口放按钮
    btn = QPushButton(widget)
    # 设置按钮的文本
    btn.setText('按钮')
    # 设置按钮相对于窗口（工作区）的位置
    btn.move(10, 10)
    # 绑定槽
    btn.clicked.connect(on_click_btn)
    # 设置工作区的尺寸
    widget.resize(300, 300)
    # 设置窗口的坐标（对于屏幕的位置）
    widget.move(200, 200)
    # 设置窗口标题栏文字
    widget.setWindowTitle('屏幕坐标系')
    # 显示窗口
    widget.show()
    # 进入事件循环
    sys.exit(app.exec_())
