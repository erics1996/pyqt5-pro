"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: QLineEditMask.py
@time: 2020/11/25 下午11:41
"""
from PyQt5.QtWidgets import QWidget, QApplication, QFormLayout, QLineEdit
import sys


class QLineEditMask(QWidget):
    def __init__(self):
        # 调用父类QWidget的__init__方法
        super(QWidget, self).__init__()
        # 调用类的实例方法初始化窗口界面
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('5.掩码限制QLineEdit控件的输入')
        # 创建表单布局
        formLayout = QFormLayout()
        # 创建QLineEdit控件
        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()
        # 设置掩码规则（ASCII数字字符允许但不是必须输入0-9），没有输入时显示下划线
        ipLineEdit.setInputMask('000,000,000,000;_')
        # 置掩码规则（ 十六进制格式允许但不是必须输入A-F，a-f，0-9），没有输入时显示下划线
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        # 置掩码规则（ASCII数字字符允许但不是必须输入0-9），没有输入时显示下划线
        dateLineEdit.setInputMask('0000-00-00;_')
        # 置掩码规则（ASCII字母字符必须输入A-Z、a-z，如果输入a-z则小写转大写），没有输入时显示#号
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')
        # 将QLineEdit控件添加到表单布局中
        formLayout.addRow('ip地址', ipLineEdit)
        formLayout.addRow('mac地址', macLineEdit)
        formLayout.addRow('日期', dateLineEdit)
        formLayout.addRow('序列号', licenseLineEdit)
        # 设置窗口的布局为表单布局
        self.setLayout(formLayout)


if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)
    # 创建窗口类的对象
    mainWindow = QLineEditMask()
    # 显示窗口
    mainWindow.show()
    # 调用exit()进入程序的主循环
    sys.exit(app.exec_())
