# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\Python\PyQT\GraphPyQtTest\ui\select_dialog\select_graph.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectDialog(object):
    def setupUi(self, SelectDialog):
        SelectDialog.setObjectName("SelectDialog")
        SelectDialog.resize(110, 105)
        self.groupBox = QtWidgets.QGroupBox(SelectDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 107, 98))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbTemperature = QtWidgets.QRadioButton(self.groupBox)
        self.rbTemperature.setObjectName("rbTemperature")
        self.verticalLayout.addWidget(self.rbTemperature)
        self.rbPressure = QtWidgets.QRadioButton(self.groupBox)
        self.rbPressure.setObjectName("rbPressure")
        self.verticalLayout.addWidget(self.rbPressure)
        self.rbHumidity = QtWidgets.QRadioButton(self.groupBox)
        self.rbHumidity.setObjectName("rbHumidity")
        self.verticalLayout.addWidget(self.rbHumidity)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SelectDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectDialog)

    def retranslateUi(self, SelectDialog):
        _translate = QtCore.QCoreApplication.translate
        SelectDialog.setWindowTitle(_translate("SelectDialog", "Type Selector"))
        self.groupBox.setTitle(_translate("SelectDialog", "GraphType"))
        self.rbTemperature.setText(_translate("SelectDialog", "Temperature"))
        self.rbPressure.setText(_translate("SelectDialog", "Pressure"))
        self.rbHumidity.setText(_translate("SelectDialog", "Humidity"))


