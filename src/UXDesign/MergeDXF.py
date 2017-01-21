# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/MergeDXF.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MergeDXF(object):
    def setupUi(self, MergeDXF):
        MergeDXF.setObjectName("MergeDXF")
        MergeDXF.setEnabled(True)
        MergeDXF.resize(625, 388)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MergeDXF)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mergeSelectFolder = QtWidgets.QPushButton(MergeDXF)
        self.mergeSelectFolder.setObjectName("mergeSelectFolder")
        self.verticalLayout.addWidget(self.mergeSelectFolder)
        self.mergePDF = QtWidgets.QPushButton(MergeDXF)
        self.mergePDF.setEnabled(False)
        self.mergePDF.setObjectName("mergePDF")
        self.verticalLayout.addWidget(self.mergePDF)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mergeFolder = QtWidgets.QLabel(MergeDXF)
        self.mergeFolder.setObjectName("mergeFolder")
        self.verticalLayout_2.addWidget(self.mergeFolder)
        self.mergeProcess = QtWidgets.QLabel(MergeDXF)
        self.mergeProcess.setObjectName("mergeProcess")
        self.verticalLayout_2.addWidget(self.mergeProcess)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.func_disc = QtWidgets.QLabel(MergeDXF)
        self.func_disc.setWordWrap(True)
        self.func_disc.setObjectName("func_disc")
        self.verticalLayout_2.addWidget(self.func_disc)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(MergeDXF)
        QtCore.QMetaObject.connectSlotsByName(MergeDXF)

    def retranslateUi(self, MergeDXF):
        _translate = QtCore.QCoreApplication.translate
        MergeDXF.setWindowTitle(_translate("MergeDXF", "Form"))
        self.mergeSelectFolder.setText(_translate("MergeDXF", "Select Folder"))
        self.mergePDF.setText(_translate("MergeDXF", "Merge DXF\'s"))
        self.mergeFolder.setText(_translate("MergeDXF", "Chosse a Folder"))
        self.mergeProcess.setText(_translate("MergeDXF", "Prosscessing Files"))
        self.func_disc.setText(_translate("MergeDXF", "The DXF merge tool will create a ZIP folder of all DXF files for the project and a report that shows the change to the files. This report is included in the ZIP file."))

