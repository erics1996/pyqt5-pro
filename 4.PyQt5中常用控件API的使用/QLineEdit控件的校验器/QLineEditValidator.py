"""
@from：https://pythoneers.cn
@author: qq3330447288
@contact: erics1996@yeah.net
@software: PyCharm
@file: QLineEditValidator.py
@time: 2020/11/24 上午5:14
"""
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QApplication
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp  # 引入正则表达式的类
import sys


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLineEdit控件的校验器')
        # 创建表单布局对象
        formLayout = QFormLayout()
        # 创建三个QLineEdit控件
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()
        # 将控件添加到布局中
        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('字母和数字(正则表达式)', validatorLineEdit)
        # 为QLineEdit控添默认提示内容
        intLineEdit.setPlaceholderText('整数')
        doubleLineEdit.setPlaceholderText('浮点')
        validatorLineEdit.setPlaceholderText('字母和数字')
        """
        1.设置整数校验器(只能输入[1,99]之间的整数)
        """
        # 创建QDoubleValidator校验器对象
        intValidator = QIntValidator(self)
        # 设置校验范围
        intValidator.setRange(1, 99)
        """
        2.设置浮点校验器(只能输入[-99.xx,99.xx]，精度要求保留小数点后2位)
        """
        # 创建QDoubleValidator校验器对象
        doubleValidator = QDoubleValidator(self)
        # 设置校验范围
        doubleValidator.setRange(-99, 99)
        # 正常显示浮点数
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，保留小数点后两位
        doubleValidator.setDecimals(2)
        """
        3.设置字母和数字(正则表达式)校验器
        """
        # 正则表达式
        reg = QRegExp('[a-zA-Z0-9]+$')
        # 正则表达式校验器
        validator = QRegExpValidator(self)
        # 将正则表达式和正则表达式校验器绑定到一起
        validator.setRegExp(reg)
        """
        设置校验器：绑定校验器和控件
        """
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)
        # 应用表单布局
        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
