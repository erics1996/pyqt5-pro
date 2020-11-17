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
        self.init_ui()

    def init_ui(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText('<font color=red>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)

        label2.setText('<a href="#">欢迎你，我是Python开发栈！</a>')

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签！')
        label3.setPixmap(QPixmap("../images/python.jpg"))

        label4.setText('<a href="https://pythoneers.cn">感谢您访问本站！</a>')
        label4.setAlignment(Qt.AlignRight)
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        label2.linkHovered.connect(self.linkHovered)
        label4.linkHovered.connect(self.linkClicked)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def onclick_button(self):
        sender = self.sender()
        print(sender.text() + "按键被按下！")
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qlabel_demo = QLabelDemo()
    qlabel_demo.show()
    sys.exit(app.exec_())
