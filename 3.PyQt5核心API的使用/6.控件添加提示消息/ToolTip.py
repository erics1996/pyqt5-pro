"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: ToolTip.py
@time: 2020/11/17 上午11:39
"""
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QToolTip, QHBoxLayout, QWidget, QPushButton, QApplication


class ToolTip(QMainWindow):
    def __init__(self):
        super(ToolTip, self).__init__()
        self.init_ui()

    def init_ui(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('你好,<b>Erics</b>')
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('按钮')
        self.button1.setToolTip('这是一个按钮！')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool_tip = ToolTip()
    tool_tip.show()
    sys.exit(app.exec_())
"""
支持富文本
"""
