# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Update.ui'
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
        Form.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.client_name = QtGui.QLineEdit(self.widget)
        self.client_name.setObjectName(_fromUtf8("client_name"))
        self.verticalLayout_2.addWidget(self.client_name)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.logo_path = QtGui.QLineEdit(self.widget_2)
        self.logo_path.setObjectName(_fromUtf8("logo_path"))
        self.verticalLayout_3.addWidget(self.logo_path)
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.broswe_button = QtGui.QPushButton(self.widget_3)
        self.broswe_button.setObjectName(_fromUtf8("broswe_button"))
        self.horizontalLayout.addWidget(self.broswe_button)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.info_label = QtGui.QLabel(Form)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.info_label.setObjectName(_fromUtf8("info_label"))
        self.verticalLayout.addWidget(self.info_label)
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cancel_button = QtGui.QPushButton(self.widget_4)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem2 = QtGui.QSpacerItem(193, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.action_button = QtGui.QPushButton(self.widget_4)
        self.action_button.setObjectName(_fromUtf8("action_button"))
        self.horizontalLayout_2.addWidget(self.action_button)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Client Name: (Required)", None))
        self.label_2.setText(_translate("Form", "Client Logo: (Jpg, Png)", None))
        self.broswe_button.setText(_translate("Form", "Broswe", None))
        self.info_label.setText(_translate("Form", "This is feed back", None))
        self.cancel_button.setText(_translate("Form", "Cancel", None))
        self.action_button.setText(_translate("Form", "Update", None))

