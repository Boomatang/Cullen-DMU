# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/boomatang/Projects/Python/Cullen-DMU/ux/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 530)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DefaultStart = QtWidgets.QWidget(self.centralwidget)
        self.DefaultStart.setObjectName("DefaultStart")
        self.gridLayout.addWidget(self.DefaultStart, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuClient = QtWidgets.QMenu(self.menubar)
        self.menuClient.setObjectName("menuClient")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMerge_Pdf_s = QtWidgets.QAction(MainWindow)
        self.actionMerge_Pdf_s.setObjectName("actionMerge_Pdf_s")
        self.actionDXF_Combine = QtWidgets.QAction(MainWindow)
        self.actionDXF_Combine.setObjectName("actionDXF_Combine")
        self.actionRegister_Update = QtWidgets.QAction(MainWindow)
        self.actionRegister_Update.setObjectName("actionRegister_Update")
        self.actionRegister_Compile = QtWidgets.QAction(MainWindow)
        self.actionRegister_Compile.setObjectName("actionRegister_Compile")
        self.actionAdd_Client = QtWidgets.QAction(MainWindow)
        self.actionAdd_Client.setObjectName("actionAdd_Client")
        self.actionView_Clients = QtWidgets.QAction(MainWindow)
        self.actionView_Clients.setObjectName("actionView_Clients")
        self.menuMenu.addAction(self.actionMerge_Pdf_s)
        self.menuMenu.addAction(self.actionDXF_Combine)
        self.menuMenu.addAction(self.actionRegister_Update)
        self.menuMenu.addAction(self.actionRegister_Compile)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuClient.addAction(self.actionAdd_Client)
        self.menuClient.addAction(self.actionView_Clients)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuClient.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuClient.setTitle(_translate("MainWindow", "Client"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionMerge_Pdf_s.setText(_translate("MainWindow", "Merge Pdf\'s"))
        self.actionDXF_Combine.setText(_translate("MainWindow", "DXF Combine"))
        self.actionRegister_Update.setText(_translate("MainWindow", "Register Update"))
        self.actionRegister_Compile.setText(_translate("MainWindow", "Register Compile"))
        self.actionAdd_Client.setText(_translate("MainWindow", "Add Client"))
        self.actionView_Clients.setText(_translate("MainWindow", "View Clients"))

