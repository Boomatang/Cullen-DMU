# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
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

class Ui_About(QtGui.QWidget):

    def __init__(self):
        super(Ui_About, self).__init__()
        self.setupUi(self)

    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        # About.setWindowModality(QtCore.Qt.WindowModal)
        About.resize(376, 176)
        self.horizontalLayout = QtGui.QHBoxLayout(About)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.product = QtGui.QLabel(About)
        self.product.setAlignment(QtCore.Qt.AlignCenter)
        self.product.setObjectName(_fromUtf8("product"))
        self.verticalLayout.addWidget(self.product)
        self.author = QtGui.QLabel(About)
        self.author.setAlignment(QtCore.Qt.AlignCenter)
        self.author.setObjectName(_fromUtf8("author"))
        self.verticalLayout.addWidget(self.author)
        self.contact = QtGui.QLabel(About)
        self.contact.setAlignment(QtCore.Qt.AlignCenter)
        self.contact.setObjectName(_fromUtf8("contact"))
        self.verticalLayout.addWidget(self.contact)
        self.version = QtGui.QLabel(About)
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName(_fromUtf8("version"))
        self.verticalLayout.addWidget(self.version)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.aboutOk = QtGui.QPushButton(About)
        self.aboutOk.setObjectName(_fromUtf8("aboutOk"))
        self.horizontalLayout_2.addWidget(self.aboutOk)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)


        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.product.setText(_translate("About", "Cullen DMU ", None))
        self.author.setText(_translate("About", "Auther: James Fiotzpatrick", None))
        self.contact.setText(_translate("About", "Contact: James@jfitzpatrick.me", None))
        self.version.setText(_translate("About", "Version: 0.1", None))
        self.aboutOk.setText(_translate("About", "OK", None))
        if __name__ == "__main__":
            self.aboutOk.clicked.connect(sys.exit)
        else:
            self.aboutOk.clicked.connect(self.hide)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_About()
    ex.show()
    sys.exit(app.exec_())
