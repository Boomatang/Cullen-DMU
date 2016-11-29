# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterCompileUpdate.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(473, 377)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.norrmal_files = QtGui.QWidget()
        self.norrmal_files.setObjectName(_fromUtf8("norrmal_files"))
        self.tabWidget.addTab(self.norrmal_files, _fromUtf8(""))
        self.tsd_files = QtGui.QWidget()
        self.tsd_files.setObjectName(_fromUtf8("tsd_files"))
        self.tabWidget.addTab(self.tsd_files, _fromUtf8(""))
        self.in_progress = QtGui.QWidget()
        self.in_progress.setObjectName(_fromUtf8("in_progress"))
        self.tabWidget.addTab(self.in_progress, _fromUtf8(""))
        self.ignore_files = QtGui.QWidget()
        self.ignore_files.setObjectName(_fromUtf8("ignore_files"))
        self.tabWidget.addTab(self.ignore_files, _fromUtf8(""))
        self.error_files = QtGui.QWidget()
        self.error_files.setObjectName(_fromUtf8("error_files"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.error_files)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.error_files)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.tabWidget.addTab(self.error_files, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "This is the report of the files that are about to be compiled. Please check that the information below in each area is correct and accpable.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.norrmal_files), _translate("Dialog", "Normal Files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tsd_files), _translate("Dialog", "TSD Files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.in_progress), _translate("Dialog", "In Progress", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ignore_files), _translate("Dialog", "Ignored Files", None))
        self.label_2.setText(_translate("Dialog", "These files have errors! please reslove the issues. If you continue these files will be ignored", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.error_files), _translate("Dialog", "Error Files", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_2.setText(_translate("Dialog", "PushButton", None))

