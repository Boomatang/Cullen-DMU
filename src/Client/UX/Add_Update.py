# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Update.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.client_name = QtWidgets.QLineEdit(self.widget)
        self.client_name.setObjectName("client_name")
        self.verticalLayout_2.addWidget(self.client_name)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.logo_path = QtWidgets.QLineEdit(self.widget_2)
        self.logo_path.setObjectName("logo_path")
        self.verticalLayout_3.addWidget(self.logo_path)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.broswe_button = QtWidgets.QPushButton(self.widget_3)
        self.broswe_button.setObjectName("broswe_button")
        self.horizontalLayout.addWidget(self.broswe_button)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.info_label = QtWidgets.QLabel(Form)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_button = QtWidgets.QPushButton(self.widget_4)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem2 = QtWidgets.QSpacerItem(193, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.action_button = QtWidgets.QPushButton(self.widget_4)
        self.action_button.setObjectName("action_button")
        self.horizontalLayout_2.addWidget(self.action_button)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Client Name: (Required)"))
        self.label_2.setText(_translate("Form", "Client Logo: (Jpg, Png)"))
        self.broswe_button.setText(_translate("Form", "Broswe"))
        self.info_label.setText(_translate("Form", "This is feed back"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.action_button.setText(_translate("Form", "Update"))

