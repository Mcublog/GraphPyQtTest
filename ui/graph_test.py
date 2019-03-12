# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\Python\PyQT\GraphTest\ui\graph_test.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/<img>/ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lwFiles = QtWidgets.QListWidget(self.centralwidget)
        self.lwFiles.setObjectName("lwFiles")
        self.verticalLayout.addWidget(self.lwFiles)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbChooseDir = QtWidgets.QPushButton(self.centralwidget)
        self.pbChooseDir.setObjectName("pbChooseDir")
        self.horizontalLayout.addWidget(self.pbChooseDir)
        self.pbClear = QtWidgets.QPushButton(self.centralwidget)
        self.pbClear.setObjectName("pbClear")
        self.horizontalLayout.addWidget(self.pbClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GraphTest"))
        self.pbChooseDir.setText(_translate("MainWindow", "Choose dir"))
        self.pbClear.setText(_translate("MainWindow", "Clear"))


import res_rc
