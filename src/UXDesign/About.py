# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/About.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.NonModal)
        About.resize(376, 176)
        self.horizontalLayout = QtWidgets.QHBoxLayout(About)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.product = QtWidgets.QLabel(About)
        self.product.setAlignment(QtCore.Qt.AlignCenter)
        self.product.setObjectName("product")
        self.verticalLayout.addWidget(self.product)
        self.author = QtWidgets.QLabel(About)
        self.author.setAlignment(QtCore.Qt.AlignCenter)
        self.author.setObjectName("author")
        self.verticalLayout.addWidget(self.author)
        self.contact = QtWidgets.QLabel(About)
        self.contact.setAlignment(QtCore.Qt.AlignCenter)
        self.contact.setObjectName("contact")
        self.verticalLayout.addWidget(self.contact)
        self.version = QtWidgets.QLabel(About)
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.version)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.aboutOk = QtWidgets.QPushButton(About)
        self.aboutOk.setObjectName("aboutOk")
        self.horizontalLayout_2.addWidget(self.aboutOk)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.product.setText(_translate("About", "Cullen DMU "))
        self.author.setText(_translate("About", "Auther: James Fiotzpatrick"))
        self.contact.setText(_translate("About", "Contact: James@jfitzpatrick.me"))
        self.version.setText(_translate("About", "Version: 0.1"))
        self.aboutOk.setText(_translate("About", "OK"))

