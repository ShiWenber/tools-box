# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\github\tools-box\tools-box\pythonGUI\Scanbak.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Scanbak(object):
    def setupUi(self, Scanbak):
        Scanbak.setObjectName("Scanbak")
        Scanbak.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Scanbak)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_in = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_in.setGeometry(QtCore.QRect(21, 99, 761, 24))
        self.lineEdit_in.setObjectName("lineEdit_in")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 241, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_out = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_out.setEnabled(True)
        self.lineEdit_out.setGeometry(QtCore.QRect(21, 168, 761, 24))
        self.lineEdit_out.setObjectName("lineEdit_out")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 140, 151, 20))
        self.label_2.setObjectName("label_2")
        Scanbak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Scanbak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Scanbak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Scanbak)
        self.statusbar.setObjectName("statusbar")
        Scanbak.setStatusBar(self.statusbar)

        self.retranslateUi(Scanbak)
        QtCore.QMetaObject.connectSlotsByName(Scanbak)

    def retranslateUi(self, Scanbak):
        _translate = QtCore.QCoreApplication.translate
        Scanbak.setWindowTitle(_translate("Scanbak", "MainWindow"))
        self.label.setText(_translate("Scanbak", "请输入存有url网址的txt文件"))
        self.pushButton.setText(_translate("Scanbak", "检测"))
        self.label_2.setText(_translate("Scanbak", "输出文件的路径"))
