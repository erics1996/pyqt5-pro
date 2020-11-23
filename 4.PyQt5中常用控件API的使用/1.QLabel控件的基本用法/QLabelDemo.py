"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: QLabelDemo.py
@time: 2020/11/17 下午5:56
"""
import sys
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化窗口界面
        self.init_ui()

    def init_ui(self):
        # 创建4个QLabel控件
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        # 设置label1文本(支持html标签)
        label1.setText('<font color="orange">这是一个文本标签</font>')
        # 创建调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)  # 设置控件的背景色
        # 设置label1使用创建的调色板（设置label1控件的背景色）
        label1.setPalette(palette)
        # 设置label1自动填充背景
        label1.setAutoFillBackground(True)
        # 设置label1居中对齐
        label1.setAlignment(Qt.AlignCenter)

        # 设置label2的文本
        label2.setText('<a href="#">欢迎你使用Python GUI程序！</a>')  # 跳转网页或者是点击事件
        # 设置label2文本居中
        label3.setAlignment(Qt.AlignCenter)
        # 设置提示信息
        label3.setToolTip('这是一个图片标签！')
        # 设置标签下显示图片
        label3.setPixmap(QPixmap('../images/python.jpg'))

        # 设置label4的文本
        label4.setText('<a href="https://pythoneers.cn">感谢您访问我的网站！</a>')
        # 屏蔽事件（点击之后打开网页，而不是触发事件）
        label4.setOpenExternalLinks(True)  # False是响应事件
        # 设置label4右对齐
        label4.setAlignment(Qt.AlignRight)
        # 设置提示信息
        label4.setToolTip('这是一个超链接！')

        # 创建垂直布局对象
        vbox = QVBoxLayout()
        # 将label1、label2、label2、label3控件添加到布局中
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 滑过label2标签的信号绑定到槽(函数)
        label2.linkHovered.connect(self.linkHovered)
        # 点击label4标签的信号绑定槽(函数)
        label4.linkActivated.connect(self.linkClicked)
        # 设置窗口的布局
        self.setLayout(vbox)
        # 设置窗口标题
        self.setWindowTitle('QLabel控件演示')


    def linkHovered(self):
        """
        当鼠标划过标签label2时触发事件
        :return:
        """
        print('当鼠标划过标签label2时触发事件')

    def linkClicked(self):
        """
        当鼠标单击标签label4时触发事件
        :return:
        """
        print('当鼠标单击标签label4时触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QLabelDemo()
    mainWindow.show()
    sys.exit(app.exec_())
