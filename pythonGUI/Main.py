# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pythonGUI/Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Tran import Ui_Tran
from Zhuanhuan import *
from Scanbak import *
from TranQR import *

#############函数所需
import pandas as pd
import xlrd
import csv
import codecs
#################

class Ui_MainWindow(QtWidgets.QMainWindow):
     # 为了使类继承父类中的内容
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    ###########
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 600)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 171, 31))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 80, 191, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 链接按钮和窗口
        self.pushButton.clicked.connect(self.tran)
        self.pushButton_2.clicked.connect(self.zhuanhuan)
        self.pushButton_3.clicked.connect(self.scanbak)
        self.pushButton_4.clicked.connect(self.tranQR)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    # 定义功能函数1，转化CSV-xlsx,在主界面中添加其他窗口的类
    def tran(self):
        ui_Tran.show()
        MainWindow.close()
    def zhuanhuan(self):
        ui_Zhuanhuan.show()
        MainWindow.close()
    def scanbak(self):
        ui_Scanbak.show()
        MainWindow.close()
    def tranQR(self):
        ui_TranQR.show()
        MainWindow.close()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">tools-box欢迎您</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CSV-xlsx格式转换工具"))
        self.pushButton_2.setText(_translate("MainWindow", "图像转化为txt文本文件"))
        self.pushButton_3.setText(_translate("MainWindow", "网站目录检测/IP端口扫描"))
        self.pushButton_4.setText(_translate("MainWindow", "字符串生成二维码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_Tran = Ui_Tran()
    ui_Zhuanhuan = Ui_Zhuanhuan()
    ui_Scanbak = Ui_Scanbak()
    ui_TranQR = Ui_TranQR()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
