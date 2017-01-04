# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 530)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.DefaultStart = QtGui.QWidget(self.centralwidget)
        self.DefaultStart.setObjectName(_fromUtf8("DefaultStart"))
        self.gridLayout.addWidget(self.DefaultStart, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuClient = QtGui.QMenu(self.menubar)
        self.menuClient.setObjectName(_fromUtf8("menuClient"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionMerge_Pdf_s = QtGui.QAction(MainWindow)
        self.actionMerge_Pdf_s.setObjectName(_fromUtf8("actionMerge_Pdf_s"))
        self.actionDXF_Combine = QtGui.QAction(MainWindow)
        self.actionDXF_Combine.setObjectName(_fromUtf8("actionDXF_Combine"))
        self.actionRegister_Update = QtGui.QAction(MainWindow)
        self.actionRegister_Update.setObjectName(_fromUtf8("actionRegister_Update"))
        self.actionRegister_Compile = QtGui.QAction(MainWindow)
        self.actionRegister_Compile.setObjectName(_fromUtf8("actionRegister_Compile"))
        self.actionAdd_Client = QtGui.QAction(MainWindow)
        self.actionAdd_Client.setObjectName(_fromUtf8("actionAdd_Client"))
        self.actionView_Clients = QtGui.QAction(MainWindow)
        self.actionView_Clients.setObjectName(_fromUtf8("actionView_Clients"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuMenu.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuClient.setTitle(_translate("MainWindow", "Client", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionMerge_Pdf_s.setText(_translate("MainWindow", "Merge Pdf\'s", None))
        self.actionDXF_Combine.setText(_translate("MainWindow", "DXF Combine", None))
        self.actionRegister_Update.setText(_translate("MainWindow", "Register Update", None))
        self.actionRegister_Compile.setText(_translate("MainWindow", "Register Compile", None))
        self.actionAdd_Client.setText(_translate("MainWindow", "Add Client", None))
        self.actionView_Clients.setText(_translate("MainWindow", "View Clients", None))

