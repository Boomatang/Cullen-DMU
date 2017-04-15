# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Programing/Cullen-DMU/ux/RegisterCompileUpdate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 377)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.norrmal_files = QtWidgets.QWidget()
        self.norrmal_files.setObjectName("norrmal_files")
        self.tabWidget.addTab(self.norrmal_files, "")
        self.tsd_files = QtWidgets.QWidget()
        self.tsd_files.setObjectName("tsd_files")
        self.tabWidget.addTab(self.tsd_files, "")
        self.in_progress = QtWidgets.QWidget()
        self.in_progress.setObjectName("in_progress")
        self.tabWidget.addTab(self.in_progress, "")
        self.ignore_files = QtWidgets.QWidget()
        self.ignore_files.setObjectName("ignore_files")
        self.tabWidget.addTab(self.ignore_files, "")
        self.error_files = QtWidgets.QWidget()
        self.error_files.setObjectName("error_files")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.error_files)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.error_files)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tabWidget.addTab(self.error_files, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "This is the report of the files that are about to be compiled. Please check that the information below in each area is correct and accpable."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.norrmal_files), _translate("Dialog", "Normal Files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tsd_files), _translate("Dialog", "TSD Files"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.in_progress), _translate("Dialog", "In Progress"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ignore_files), _translate("Dialog", "Ignored Files"))
        self.label_2.setText(_translate("Dialog", "These files have errors! please reslove the issues. If you continue these files will be ignored"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.error_files), _translate("Dialog", "Error Files"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))

