# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/MergePDF.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MergePDF(object):
    def setupUi(self, MergePDF):
        MergePDF.setObjectName("MergePDF")
        MergePDF.setEnabled(True)
        MergePDF.resize(625, 388)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MergePDF)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mergeSelectFolder = QtWidgets.QPushButton(MergePDF)
        self.mergeSelectFolder.setObjectName("mergeSelectFolder")
        self.verticalLayout.addWidget(self.mergeSelectFolder)
        self.mergePDF = QtWidgets.QPushButton(MergePDF)
        self.mergePDF.setEnabled(False)
        self.mergePDF.setObjectName("mergePDF")
        self.verticalLayout.addWidget(self.mergePDF)
        self.mergeCancel = QtWidgets.QPushButton(MergePDF)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergeCancel.sizePolicy().hasHeightForWidth())
        self.mergeCancel.setSizePolicy(sizePolicy)
        self.mergeCancel.setObjectName("mergeCancel")
        self.verticalLayout.addWidget(self.mergeCancel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mergeFolder = QtWidgets.QLabel(MergePDF)
        self.mergeFolder.setObjectName("mergeFolder")
        self.verticalLayout_2.addWidget(self.mergeFolder)
        self.mergeProcess = QtWidgets.QLabel(MergePDF)
        self.mergeProcess.setObjectName("mergeProcess")
        self.verticalLayout_2.addWidget(self.mergeProcess)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(MergePDF)
        QtCore.QMetaObject.connectSlotsByName(MergePDF)

    def retranslateUi(self, MergePDF):
        _translate = QtCore.QCoreApplication.translate
        MergePDF.setWindowTitle(_translate("MergePDF", "Form"))
        self.mergeSelectFolder.setText(_translate("MergePDF", "Select Folder"))
        self.mergePDF.setText(_translate("MergePDF", "Merge PDF\'s"))
        self.mergeCancel.setText(_translate("MergePDF", "Cancel Merge"))
        self.mergeFolder.setText(_translate("MergePDF", "Chosse a Folder"))
        self.mergeProcess.setText(_translate("MergePDF", "Prosscessing Files"))

