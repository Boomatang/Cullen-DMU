# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/Client/Client_View.ui'
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
        Form.resize(524, 441)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.client_label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.client_label.setFont(font)
        self.client_label.setObjectName(_fromUtf8("client_label"))
        self.verticalLayout_2.addWidget(self.client_label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.logo_image = QtGui.QLabel(self.widget_2)
        self.logo_image.setText(_fromUtf8(""))
        self.logo_image.setPixmap(QtGui.QPixmap(_fromUtf8("/home/boomatang/Projects/Python/Cullen-DMU/cullen3.png")))
        self.logo_image.setObjectName(_fromUtf8("logo_image"))
        self.verticalLayout_3.addWidget(self.logo_image)
        self.logo_path = QtGui.QLabel(self.widget_2)
        self.logo_path.setObjectName(_fromUtf8("logo_path"))
        self.verticalLayout_3.addWidget(self.logo_path)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.back_button = QtGui.QPushButton(self.widget_3)
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.horizontalLayout.addWidget(self.back_button)
        spacerItem1 = QtGui.QSpacerItem(315, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.edit_button = QtGui.QPushButton(self.widget_3)
        self.edit_button.setObjectName(_fromUtf8("edit_button"))
        self.horizontalLayout.addWidget(self.edit_button)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Client Name:", None))
        self.client_label.setText(_translate("Form", "This is the Client Name", None))
        self.logo_path.setText(_translate("Form", "Logo Path", None))
        self.back_button.setText(_translate("Form", "Back", None))
        self.edit_button.setText(_translate("Form", "Edit Details", None))

