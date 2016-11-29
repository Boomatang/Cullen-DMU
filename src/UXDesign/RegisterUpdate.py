# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterUpdate.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(625, 388)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.source_register = QtGui.QPushButton(Form)
        self.source_register.setObjectName(_fromUtf8("source_register"))
        self.verticalLayout.addWidget(self.source_register)
        self.main_register = QtGui.QPushButton(Form)
        self.main_register.setEnabled(True)
        self.main_register.setObjectName(_fromUtf8("main_register"))
        self.verticalLayout.addWidget(self.main_register)
        self.registerCompileStart = QtGui.QPushButton(Form)
        self.registerCompileStart.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerCompileStart.sizePolicy().hasHeightForWidth())
        self.registerCompileStart.setSizePolicy(sizePolicy)
        self.registerCompileStart.setObjectName(_fromUtf8("registerCompileStart"))
        self.verticalLayout.addWidget(self.registerCompileStart)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_1 = QtGui.QLabel(Form)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout_2.addWidget(self.label_1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.update_label = QtGui.QLabel(Form)
        self.update_label.setObjectName(_fromUtf8("update_label"))
        self.verticalLayout_2.addWidget(self.update_label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.source_register.setText(_translate("Form", "Select TSD Register", None))
        self.main_register.setText(_translate("Form", "Select Register", None))
        self.registerCompileStart.setText(_translate("Form", "Update Register", None))
        self.label_1.setText(_translate("Form", "Chosse TSD drawing register to update from.", None))
        self.label_2.setText(_translate("Form", "Chosse Register Document to update.", None))
        self.update_label.setText(_translate("Form", "Updating Register", None))

