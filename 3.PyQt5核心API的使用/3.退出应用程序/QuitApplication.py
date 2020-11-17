"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: QuitApplication.py
@time: 2020/11/17 上午10:48
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 150)
        self.setWindowTitle('退出应用程序')
        # 添加按钮
        self.buttion1 = QPushButton('退出应用程序')
        # 将信号与槽关联。信号绑定到方法，每一个信号都有一个connect方法
        self.buttion1.clicked.connect(self.onClickButton)
        # 设置水平布局（将按钮放到布局中）
        layout = QHBoxLayout()
        layout.addWidget(self.buttion1)
        # 把布局放到QWidget(所有的控件都放到Qwiget，Qwiget可以充满整个窗口)
        main_frame = QWidget()
        main_frame.setLayout(layout)
        # 框架放到窗口上
        self.setCentralWidget(main_frame)

    def onClickButton(self):
        # 通过sender获取button
        sender = self.sender()
        # 获取button的文本
        print(sender.text() + ' 按钮被按下！')
        # 创建应用程序对象
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
