
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from src.UXDesign.MainWindow import Ui_MainWindow
from src.UXDesign.MyMergePDF import MergePDFClass as MergePDF
from src.UXDesign.MyRegisterCompile import RegisterCompileClass as RegisterCompile
from src.UXDesign.About import Ui_About as About
from src.UXDesign.MyMergeDXF import MergeDXFClass
from src.UXDesign.MyRegisterUpdate import UpdateRegisterClass
from src.Client.UX.Add_Client import AddClient
from src.Client.UX.ViewClientList import ViewClientList
from src.Client.UX.View_Client_Detail import View_Client_Detail


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.widget = None
        self.merge = MergePDF()
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
        self.actionView_Clients.triggered.connect(self.view_client_list)

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
        register = RegisterCompile(self)

        self.widget_hide()
        self.gridLayout.addWidget(register, 0, 0, 1, 1)
        register.show()
        self.widget = register

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

    def view_client_list(self):
        view_client_list = ViewClientList(self)

        self.widget_hide()
        self.gridLayout.addWidget(view_client_list, 0, 0, 1, 1)
        view_client_list.show()
        self.widget = view_client_list

    def view_client_details(self, client):
        view = View_Client_Detail(self, client)

        self.widget_hide()
        self.gridLayout.addWidget(view, 0, 0, 1, 1)
        view.show()
        self.widget = view

    def about_popup(self):
        self.about.show()


def run():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('cullen3logo.png'))
    ex = MyMainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../cullen3logo.png'))
    ex = MyMainWindow()
    sys.exit(app.exec_())
