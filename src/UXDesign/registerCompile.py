# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/registerCompile.ui'
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
        self.client_list_box = QtGui.QComboBox(Form)
        self.client_list_box.setDuplicatesEnabled(True)
        self.client_list_box.setObjectName(_fromUtf8("client_list_box"))
        self.verticalLayout.addWidget(self.client_list_box)
        self.register_documnet = QtGui.QPushButton(Form)
        self.register_documnet.setEnabled(True)
        self.register_documnet.setObjectName(_fromUtf8("register_documnet"))
        self.verticalLayout.addWidget(self.register_documnet)
        self.project_folder = QtGui.QPushButton(Form)
        self.project_folder.setObjectName(_fromUtf8("project_folder"))
        self.verticalLayout.addWidget(self.project_folder)
        self.compile_to_folder = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compile_to_folder.sizePolicy().hasHeightForWidth())
        self.compile_to_folder.setSizePolicy(sizePolicy)
        self.compile_to_folder.setObjectName(_fromUtf8("compile_to_folder"))
        self.verticalLayout.addWidget(self.compile_to_folder)
        self.compile_package = QtGui.QPushButton(Form)
        self.compile_package.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compile_package.sizePolicy().hasHeightForWidth())
        self.compile_package.setSizePolicy(sizePolicy)
        self.compile_package.setObjectName(_fromUtf8("compile_package"))
        self.verticalLayout.addWidget(self.compile_package)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mergeFolder = QtGui.QLabel(Form)
        self.mergeFolder.setObjectName(_fromUtf8("mergeFolder"))
        self.verticalLayout_2.addWidget(self.mergeFolder)
        self.mergeProcess = QtGui.QLabel(Form)
        self.mergeProcess.setObjectName(_fromUtf8("mergeProcess"))
        self.verticalLayout_2.addWidget(self.mergeProcess)
        self.mergeProcess_2 = QtGui.QLabel(Form)
        self.mergeProcess_2.setObjectName(_fromUtf8("mergeProcess_2"))
        self.verticalLayout_2.addWidget(self.mergeProcess_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.help_label = QtGui.QLabel(Form)
        self.help_label.setWordWrap(True)
        self.help_label.setObjectName(_fromUtf8("help_label"))
        self.verticalLayout_2.addWidget(self.help_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.register_documnet.setText(_translate("Form", "Select Register Document", None))
        self.project_folder.setText(_translate("Form", "Select Project Folder", None))
        self.compile_to_folder.setText(_translate("Form", "Compile To Folder", None))
        self.compile_package.setText(_translate("Form", "Compile Package", None))
        self.mergeFolder.setText(_translate("Form", "Chosse Project Folder", None))
        self.mergeProcess.setText(_translate("Form", "Chosse Register Document", None))
        self.mergeProcess_2.setText(_translate("Form", "Compile Package update", None))
        self.help_label.setText(_translate("Form", "This is some help test for this page. As you can see it needs filling out.. :)", None))

