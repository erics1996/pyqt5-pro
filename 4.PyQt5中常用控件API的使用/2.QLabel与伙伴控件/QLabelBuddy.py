"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: QLabelBuddy.py
@time: 2020/11/17 下午6:26
"""
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        # 初始化实例的时候执行
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题栏文本
        self.setWindowTitle('QLabel与伙伴控件')
        # 创建QLabel控件
        nameQLabel = QLabel('&Name', self)
        # 创建QLineEdit控件
        nameQLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameQLabel.setBuddy(nameQLineEdit)
        # 创建QLabel控件
        passwordQLabel = QLabel('&Pwd', self)
        # 创建QLineEdit控件
        passwordQLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordQLabel.setBuddy(passwordQLineEdit)
        ok_btn = QPushButton('&OK')
        cancel_btn = QPushButton('&Cancel')
        # 创建栅格布局
        mainLayout = QGridLayout(self)
        # 将nameQLabel添加到栅格布局中
        mainLayout.addWidget(nameQLabel, 0, 0)
        # 将nameQLineEdit添加到栅格布局中
        mainLayout.addWidget(nameQLineEdit, 0, 1, 1, 2)
        # 将passwordQLabel添加到栅格布局中
        mainLayout.addWidget(passwordQLabel, 1, 0)
        # 将passwordQLineEdit添加到栅格布局中
        mainLayout.addWidget(passwordQLineEdit, 1, 1, 1, 2)
        # 将ok_btn添加到布局中
        mainLayout.addWidget(ok_btn, 2, 1)
        # 将cancel_btn添加到布局中
        mainLayout.addWidget(cancel_btn, 2, 2)
        """
        行索引rowIndex和列索引columnIndex是控件在栅格布局中位置，占用的行数row和占用的列数column是控件的尺寸
        mainLayout.addWidget(控件对象, 行索引rowIndex, 列索引columnIndex, 占用的行数row, 占用的列数column)
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QLabel_Buddy = QLabelBuddy()
    QLabel_Buddy.show()
    sys.exit(app.exec_())
