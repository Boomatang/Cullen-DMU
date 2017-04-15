# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/registerCompile.ui'
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
        self.client_list_box = QtWidgets.QComboBox(Form)
        self.client_list_box.setDuplicatesEnabled(True)
        self.client_list_box.setObjectName("client_list_box")
        self.verticalLayout.addWidget(self.client_list_box)
        self.register_documnet = QtWidgets.QPushButton(Form)
        self.register_documnet.setEnabled(True)
        self.register_documnet.setObjectName("register_documnet")
        self.verticalLayout.addWidget(self.register_documnet)
        self.project_folder = QtWidgets.QPushButton(Form)
        self.project_folder.setObjectName("project_folder")
        self.verticalLayout.addWidget(self.project_folder)
        self.compile_to_folder = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compile_to_folder.sizePolicy().hasHeightForWidth())
        self.compile_to_folder.setSizePolicy(sizePolicy)
        self.compile_to_folder.setObjectName("compile_to_folder")
        self.verticalLayout.addWidget(self.compile_to_folder)
        self.compile_package = QtWidgets.QPushButton(Form)
        self.compile_package.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compile_package.sizePolicy().hasHeightForWidth())
        self.compile_package.setSizePolicy(sizePolicy)
        self.compile_package.setObjectName("compile_package")
        self.verticalLayout.addWidget(self.compile_package)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mergeFolder = QtWidgets.QLabel(Form)
        self.mergeFolder.setObjectName("mergeFolder")
        self.verticalLayout_2.addWidget(self.mergeFolder)
        self.mergeProcess = QtWidgets.QLabel(Form)
        self.mergeProcess.setObjectName("mergeProcess")
        self.verticalLayout_2.addWidget(self.mergeProcess)
        self.mergeProcess_2 = QtWidgets.QLabel(Form)
        self.mergeProcess_2.setObjectName("mergeProcess_2")
        self.verticalLayout_2.addWidget(self.mergeProcess_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.help_label = QtWidgets.QLabel(Form)
        self.help_label.setWordWrap(True)
        self.help_label.setObjectName("help_label")
        self.verticalLayout_2.addWidget(self.help_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_documnet.setText(_translate("Form", "Select Register Document"))
        self.project_folder.setText(_translate("Form", "Select Project Folder"))
        self.compile_to_folder.setText(_translate("Form", "Compile To Folder"))
        self.compile_package.setText(_translate("Form", "Compile Package"))
        self.mergeFolder.setText(_translate("Form", "Chosse Project Folder"))
        self.mergeProcess.setText(_translate("Form", "Chosse Register Document"))
        self.mergeProcess_2.setText(_translate("Form", "Compile Package update"))
        self.help_label.setText(_translate("Form", "This is some help test for this page. As you can see it needs filling out.. :)"))

