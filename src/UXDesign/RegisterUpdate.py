# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/RegisterUpdate.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(625, 388)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.source_register = QtWidgets.QPushButton(Form)
        self.source_register.setObjectName("source_register")
        self.verticalLayout.addWidget(self.source_register)
        self.main_register = QtWidgets.QPushButton(Form)
        self.main_register.setEnabled(True)
        self.main_register.setObjectName("main_register")
        self.verticalLayout.addWidget(self.main_register)
        self.registerCompileStart = QtWidgets.QPushButton(Form)
        self.registerCompileStart.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerCompileStart.sizePolicy().hasHeightForWidth())
        self.registerCompileStart.setSizePolicy(sizePolicy)
        self.registerCompileStart.setObjectName("registerCompileStart")
        self.verticalLayout.addWidget(self.registerCompileStart)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_2.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.update_label = QtWidgets.QLabel(Form)
        self.update_label.setObjectName("update_label")
        self.verticalLayout_2.addWidget(self.update_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.source_register.setText(_translate("Form", "Select TSD Register"))
        self.main_register.setText(_translate("Form", "Select Register"))
        self.registerCompileStart.setText(_translate("Form", "Update Register"))
        self.label_1.setText(_translate("Form", "Chosse TSD drawing register to update from."))
        self.label_2.setText(_translate("Form", "Chosse Register Document to update."))
        self.update_label.setText(_translate("Form", "Updating Register"))

