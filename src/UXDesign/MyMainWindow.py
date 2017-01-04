# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt4 import QtCore, QtGui
from src.UXDesign.MainWindow import Ui_MainWindow
from src.UXDesign.MergePDF import Ui_MergePDF as MergePDF
from src.UXDesign.MyRegisterCompile import RegisterCompileClass as RegisterCompile
from src.UXDesign.About import Ui_About as About
from src.UXDesign.MyMergeDXF import MergeDXFClass
from src.UXDesign.MyRegisterUpdate import UpdateRegisterClass
from src.Client.UX.Add_Client import AddClient


class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.widget = None
        self.merge = MergePDF()
        self.register = RegisterCompile()
        self.about = About()
        self.mergeDXF = MergeDXFClass()
        self.update = UpdateRegisterClass()
        self.setupUi(self)
        self.button_actions()

        self.show()
        self.AddClient = AddClient(self)


    def button_actions(self):
        self.actionMerge_Pdf_s.triggered.connect(self.mergerPdfs)
        self.actionRegister_Compile.triggered.connect(self.registerCompile)
        self.actionAbout.triggered.connect(self.about_popup)
        self.actionDXF_Combine.triggered.connect(self.start_mergeDXF)
        self.actionRegister_Update.triggered.connect(self.start_update_register)
        self.actionAdd_Client.triggered.connect(self.add_client)

# TODO these functions need to be combined into one function

    def widget_hide(self):
        try:
            self.widget.hide()
            self.gridLayout.removeWidget(self.widget)
        except AttributeError:
            pass

    def mergerPdfs(self):
        self.widget_hide()
        self.gridLayout.addWidget(self.merge, 0, 0, 1, 1)
        self.merge.show()
        self.widget = self.merge

    def start_mergeDXF(self):
        self.widget_hide()
        self.gridLayout.addWidget(self.mergeDXF, 0, 0, 1, 1)
        self.mergeDXF.show()
        self.widget = self.mergeDXF

    def registerCompile(self):
        self.widget_hide()
        self.gridLayout.addWidget(self.register, 0, 0, 1, 1)
        self.register.show()
        self.widget = self.register

    def start_update_register(self):
        self.widget_hide()
        self.gridLayout.addWidget(self.update, 0, 0, 1, 1)
        self.update.show()
        self.widget = self.update

    def add_client(self):
        self.widget_hide()
        self.gridLayout.addWidget(self.AddClient, 0, 0, 1, 1)
        self.AddClient.show()
        self.widget = self.AddClient

    def about_popup(self):
        self.about.show()


def run():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('cullen3logo.png'))
    ex = MyMainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('../cullen3logo.png'))
    ex = MyMainWindow()
    sys.exit(app.exec_())
