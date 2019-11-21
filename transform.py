# coding=utf8
import sys
import BaiduTrans
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import *
import sys

class Timer2(QThread):
    def __init__(self, parent=None):
        super(Timer2, self).__init__(parent)
        self.stoped = False
        self.mutex = QMutex()
    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        while True:
            self.emit(SIGNAL("transField"))
            sleep(1)
    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True
    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle(u'Trans')
        self.originLang=0
        self.transLang=1
        self.time2 = Timer2()
        self.originGoogleDic = {"英语": "en", "中文": "zh-CN"}
        self.transGoogleDic = {"中文": "zh-CN","英语": "en"}
        self.originLabel = QtGui.QLabel(u'源语言')
        self.transLabel = QtGui.QLabel(u'目标语言')
        self.originChoice = QtGui.QComboBox(self)
        self.originChoice.setMaximumHeight(20)
        self.transChoice = QtGui.QComboBox(self)
        for item in self.originGoogleDic:
            self.originChoice.addItem(self.originGoogleDic[item])
        for item in self.transGoogleDic:
            self.transChoice.addItem(self.transGoogleDic[item])
        self.toolBarSplitter = QSplitter(Qt.Horizontal)
        self.toolBarSplitter.addWidget(self.originLabel)
        self.toolBarSplitter.addWidget(self.originLabel)
        self.toolBarSplitter.addWidget(self.originChoice)
        self.toolBarSplitter.addWidget(self.transLabel)
        self.toolBarSplitter.addWidget(self.transChoice)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolBarSplitter)


        self.originTextField = QTextEdit(u'原文')
        self.transTextField = QTextEdit(u'')
        self.googleTransField = QTextEdit(u'')
        self.textFieldSplitter = QSplitter(Qt.Horizontal)
        self.textFieldSplitter.addWidget(self.originTextField)
        self.textFieldSplitter.addWidget(self.transTextField)
        # self.textFieldSplitter.addWidget(self.googleTransField)
        self.textFieldSplitter.setMinimumHeight(300)
        self.layout.addWidget(self.textFieldSplitter)
        self.clearButton = QPushButton("Clear")
        self.transButton = QPushButton("Trans")
        self.exitButton = QPushButton("Exit")
        self.clearButton.setMaximumHeight(20)
        self.connect(self.clearButton, SIGNAL("clicked()"), self.clearTextField)
        self.connect(self.exitButton,SIGNAL("clicked()"),self.exitProgram)
        self.connect(self.transButton,SIGNAL("clicked()"),self.translate)
        self.connect(self.originChoice, SIGNAL('activated(int)'),self.setOriginLang)
        self.connect(self.transChoice, SIGNAL('activated(int)'), self.setTransLang)
        self.connect(self.time2,SIGNAL("transField"),self.translate)
        self.buttonSplitter = QSplitter(Qt.Horizontal)
        self.buttonSplitter.addWidget(self.clearButton)
        self.buttonSplitter.addWidget(self.transButton)
        self.buttonSplitter.addWidget(self.exitButton)
        self.layout.addWidget(self.buttonSplitter)
        self.setLayout(self.layout)
    def setOriginLang(self,text):
        self.originLang = text
    def setTransLang(self,text):
        self.transLang = text
    def clearTextField(self):
        self.transTextField.setText(u'')
        self.originTextField.setText(u'')
    def exitProgram(self):
        sys.exit(0)
    def translate(self):
        strings =str(self.originTextField.toPlainText().toUtf8())
        self.e = BaiduTrans.transByHttpRequest(self.originLang,self.transLang,strings)
        self.transTextField.setText("")
        for resultItem in self.e:
            self.transTextField.append(QString(resultItem))

