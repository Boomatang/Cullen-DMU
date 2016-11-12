# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt4 import QtCore, QtGui
from UXDesign.MergePDF import Ui_MergePDF as MergePDF
from UXDesign.registerCompile import Ui_RegisterCompile as RegisterCompile
from UXDesign.About import Ui_About as About



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


class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.widget = ""
        self.merge = MergePDF()
        self.register = RegisterCompile()
        self.about = About()
        self.setupUi(self)
        self.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.DefaultStart = QtGui.QWidget(self.centralwidget)
        self.DefaultStart.setObjectName(_fromUtf8("DefaultStart"))
        self.gridLayout.addWidget(self.DefaultStart, 0, 0, 1, 1)
        self.widget = self.DefaultStart

        MainWindow.setCentralWidget(self.centralwidget)

        self.create_menus(MainWindow)
        self.button_actions()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuMenu.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionMerge_Pdf_s.setText(_translate("MainWindow", "Merge Pdf\'s", None))
        self.actionDXF_Combine.setText(_translate("MainWindow", "DXF Combine", None))
        self.actionRegister_Update.setText(_translate("MainWindow", "Register Update", None))
        self.actionRegister_Compile.setText(_translate("MainWindow", "Register Compile", None))

    def create_menus(self, MainWindow):
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
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
        self.menuMenu.addAction(self.actionMerge_Pdf_s)
        self.menuMenu.addAction(self.actionDXF_Combine)
        self.menuMenu.addAction(self.actionRegister_Update)
        self.menuMenu.addAction(self.actionRegister_Compile)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

    def button_actions(self):
        self.actionMerge_Pdf_s.triggered.connect(self.mergerPdfs)
        self.actionRegister_Compile.triggered.connect(self.registerCompile)
        self.actionAbout.triggered.connect(self.about_popup)

    def mergerPdfs(self):
        self.widget.hide()
        self.gridLayout.removeWidget(self.widget)
        self.gridLayout.addWidget(self.merge, 0, 0, 1, 1)
        self.merge.show()
        self.widget = self.merge

    def registerCompile(self):
        self.widget.hide()

        self.gridLayout.removeWidget(self.widget)
        self.gridLayout.addWidget(self.register, 0, 0, 1, 1)
        self.register.show()
        self.widget = self.register

    def about_popup(self):
        self.about.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('../cullen3logo.png'))
    ex = Ui_MainWindow()

    sys.exit(app.exec_())
