# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MergePDF.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt4 import QtCore, QtGui

from pathlib import Path as p
from src.Merge import merge

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

class Ui_MergePDF(QtGui.QWidget):

    def __init__(self):
        super(Ui_MergePDF, self).__init__()
        self.setupUi(self)
        self.root = ''
        self.button_actions()

    def setupUi(self, MergePDF):
        MergePDF.setObjectName(_fromUtf8("MergePDF"))
        MergePDF.setEnabled(True)
        MergePDF.resize(625, 388)
        self.horizontalLayout = QtGui.QHBoxLayout(MergePDF)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mergeSelectFolder = QtGui.QPushButton(MergePDF)
        self.mergeSelectFolder.setObjectName(_fromUtf8("mergeSelectFolder"))
        self.verticalLayout.addWidget(self.mergeSelectFolder)
        self.mergePDF = QtGui.QPushButton(MergePDF)
        self.mergePDF.setEnabled(False)
        self.mergePDF.setObjectName(_fromUtf8("mergePDF"))
        self.verticalLayout.addWidget(self.mergePDF)
        self.mergeCancel = QtGui.QPushButton(MergePDF)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergeCancel.sizePolicy().hasHeightForWidth())
        self.mergeCancel.setSizePolicy(sizePolicy)
        self.mergeCancel.setObjectName(_fromUtf8("mergeCancel"))
        self.verticalLayout.addWidget(self.mergeCancel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mergeFolder = QtGui.QLabel(MergePDF)
        self.mergeFolder.setObjectName(_fromUtf8("mergeFolder"))
        self.verticalLayout_2.addWidget(self.mergeFolder)
        self.mergeProcess = QtGui.QLabel(MergePDF)
        self.mergeProcess.setObjectName(_fromUtf8("mergeProcess"))
        self.verticalLayout_2.addWidget(self.mergeProcess)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(MergePDF)
        QtCore.QMetaObject.connectSlotsByName(MergePDF)

    def retranslateUi(self, MergePDF):
        MergePDF.setWindowTitle(_translate("MergePDF", "Form", None))
        self.mergeSelectFolder.setText(_translate("MergePDF", "Select Folder", None))
        self.mergePDF.setText(_translate("MergePDF", "Merge PDF\'s", None))
        self.mergeCancel.setText(_translate("MergePDF", "Cancel Merge", None))
        self.mergeFolder.setText(_translate("MergePDF", "Choose a Folder", None))
        self.mergeProcess.setText(_translate("MergePDF", "Possessing Files", None))


    def button_actions(self):
        self.mergeSelectFolder.clicked.connect(self.get_root)
        self.mergePDF.clicked.connect(self.run_merge)

    def get_root(self):
        r = QtGui.QFileDialog.getExistingDirectory()
        self.root = p(r)
        if self.root.is_dir():
            self.mergePDF.setEnabled(True)

    def run_merge(self):
        merge.run(str(self.root))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MergePDF()
    ex.show()
    sys.exit(app.exec_())
