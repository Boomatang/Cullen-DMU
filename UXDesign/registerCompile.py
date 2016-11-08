# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerCompile.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
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

class Ui_RegisterCompile(QtGui.QWidget):

    def __init__(self):
        super(Ui_RegisterCompile, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.registerCompileSelectFolder = QtGui.QPushButton(Form)
        self.registerCompileSelectFolder.setObjectName(_fromUtf8("registerCompileSelectFolder"))
        self.verticalLayout.addWidget(self.registerCompileSelectFolder)
        self.registerCompileDocument = QtGui.QPushButton(Form)
        self.registerCompileDocument.setEnabled(False)
        self.registerCompileDocument.setObjectName(_fromUtf8("registerCompileDocument"))
        self.verticalLayout.addWidget(self.registerCompileDocument)
        self.registerCompileStart = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerCompileStart.sizePolicy().hasHeightForWidth())
        self.registerCompileStart.setSizePolicy(sizePolicy)
        self.registerCompileStart.setObjectName(_fromUtf8("registerCompileStart"))
        self.verticalLayout.addWidget(self.registerCompileStart)
        self.registerCompileCancel = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerCompileCancel.sizePolicy().hasHeightForWidth())
        self.registerCompileCancel.setSizePolicy(sizePolicy)
        self.registerCompileCancel.setObjectName(_fromUtf8("registerCompileCancel"))
        self.verticalLayout.addWidget(self.registerCompileCancel)
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
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.registerCompileSelectFolder.setText(_translate("Form", "Select Project Folder", None))
        self.registerCompileDocument.setText(_translate("Form", "Select Register Document", None))
        self.registerCompileStart.setText(_translate("Form", "Compile Package", None))
        self.registerCompileCancel.setText(_translate("Form", "Cancel Compile", None))
        self.mergeFolder.setText(_translate("Form", "Choose Project Folder", None))
        self.mergeProcess.setText(_translate("Form", "Choose Register Document", None))
        self.mergeProcess_2.setText(_translate("Form", "Compile Package update", None))
        self.mergeProcess.setWordWrap(True)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_RegisterCompile()
    ex.show()
    sys.exit(app.exec_())
