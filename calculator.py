# -*- coding: utf-8 -*-

"""
Module implementing MyCalc.
"""
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from UI.Ui_Calc_dialog import Ui_Dialog


class MyCalc(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        super(MyCalc, self).__init__()
        self.setupUi(self)
        # 定义变量
        self.str1 = ''  # 第一个操作数
        self.str2 = ''  # 第二个操作数
        self.flag = 0  # 输入数字标志，0表示未完成，1表示操作数输入完成，2计算后结果作为第一个操作数
        self.op = ''  # 操作符


    @pyqtSlot()  # 信号槽方法以响应事件，每个响应前面加这个修饰
    def on_pushButton_0_clicked(self):  # on_对象名称_信号名称(self,参数)：也可以自己按此格式创建
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '0'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '0'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '1'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '1'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '2'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '2'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 2:
            self.str1 = self.lineEdit_result.text()
            self.str2 = ''
        self.flag = 1
        self.op = '+'
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '3'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '3'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '4'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '4'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '5'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '5'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_sub_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 2:
            self.str1 = self.lineEdit_result.text()
            self.str2 = ''
        self.flag = 1
        self.op = '-'
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '6'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '6'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '7'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '7'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '8'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '8'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_mult_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 2:
            self.str1 = self.lineEdit_result.text()
            self.str2 = ''
        self.flag = 1
        self.op = '*'
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 0:
            self.str1 = self.str1 + '9'
            self.lineEdit_result.setText(self.str1)
        else:
            self.str2 = self.str2 + '9'
            self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_dot_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        strx = self.lineEdit_result.text()
        if strx.find('.') == -1:  # 如果没有小数点就加个小数点
            if self.flag == 0:
                self.str1 = self.str1 + '.'
                self.lineEdit_result.setText(self.str1)
            elif self.flag == 1:
                self.str2 = self.str2 + '.'
                self.lineEdit_result.setText(self.str2)
        if strx == '':
            if self.flag == 0:
                self.str1 = '0.'
                self.lineEdit_result.setText(self.str1)
            elif self.flag == 1:
                self.str2 = '0.'
                self.lineEdit_result.setText(self.str2)
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_reverse_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        strx = self.lineEdit_result.text()
        fla = -float(strx)
        strx = str(fla)
        self.lineEdit_result.setText(strx)
        if self.flag == 1:
            self.str2 = strx
        else:
            self.str1 = strx
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_div_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.flag == 2:
            self.str1 = self.lineEdit_result.text()
            self.str2 = ''
        self.flag = 1
        self.op = '/'
        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.flag == 0
        self.str1 = ''
        self.str2 = ''
        self.lineEdit_result.setText(self.str1)

        # raise NotImplementedError


    @pyqtSlot()
    def on_pushButton_calc_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.str1 == '':
            a = 0
        else:
            a = float(self.str1)
        if self.str2 == '':
            b = 0
        else:
            b = float(self.str2)
        res = 0
        if self.op == '+':
            res = a + b
        elif self.op == '-':
            res = a - b
        elif self.op == '*':
            res = a * b
        elif self.op == '/':
            if b == 0:
                res = 0
            else:
                res = a / b

        self.lineEdit_result.setText(str(res))
        self.flag = 2

        # raise NotImplementedError

#
# if __name__ == "__main__":
#     import sys
#     from PyQt4 import QtGui
#
#     app = QtGui.QApplication(sys.argv)
#     Dialog = MyCalc()  # 运行计算器窗口
#     Dialog.show()  # 显示窗口
#     sys.exit(app.exec_())