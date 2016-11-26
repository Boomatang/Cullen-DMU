# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MergeDXF.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from pathlib import Path as p
from Merge import mergeDXF as merge
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

class Ui_MergeDXF(object):
    def setupUi(self, MergeDXF):
        MergeDXF.setObjectName(_fromUtf8("MergeDXF"))
        MergeDXF.setEnabled(True)
        MergeDXF.resize(625, 388)
        self.horizontalLayout = QtGui.QHBoxLayout(MergeDXF)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mergeSelectFolder = QtGui.QPushButton(MergeDXF)
        self.mergeSelectFolder.setObjectName(_fromUtf8("mergeSelectFolder"))
        self.verticalLayout.addWidget(self.mergeSelectFolder)
        self.mergeDXF = QtGui.QPushButton(MergeDXF)
        self.mergeDXF.setEnabled(False)
        self.mergeDXF.setObjectName(_fromUtf8("mergeDXF"))
        self.verticalLayout.addWidget(self.mergeDXF)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mergeFolder = QtGui.QLabel(MergeDXF)
        self.mergeFolder.setObjectName(_fromUtf8("mergeFolder"))
        self.verticalLayout_2.addWidget(self.mergeFolder)
        self.mergeProcess = QtGui.QLabel(MergeDXF)
        self.mergeProcess.setObjectName(_fromUtf8("mergeProcess"))
        self.verticalLayout_2.addWidget(self.mergeProcess)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.func_disc = QtGui.QLabel(MergeDXF)
        self.func_disc.setWordWrap(True)
        self.func_disc.setObjectName(_fromUtf8("func_disc"))
        self.verticalLayout_2.addWidget(self.func_disc)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(MergeDXF)
        QtCore.QMetaObject.connectSlotsByName(MergeDXF)

    def retranslateUi(self, MergeDXF):
        MergeDXF.setWindowTitle(_translate("MergeDXF", "Form", None))
        self.mergeSelectFolder.setText(_translate("MergeDXF", "Select Folder", None))
        self.mergeDXF.setText(_translate("MergeDXF", "Merge DXF\'s", None))
        self.mergeFolder.setText(_translate("MergeDXF", "Chosse a Folder", None))
        self.mergeProcess.setText(_translate("MergeDXF", "Prosscessing Files", None))
        self.func_disc.setText(_translate("MergeDXF", "The DXF merge tool will create a ZIP folder of all DXF files for the project and a report that shows the change to the files. This report is included in the ZIP file.", None))

