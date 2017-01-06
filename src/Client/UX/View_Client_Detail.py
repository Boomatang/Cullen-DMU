import sys
from pathlib import Path as p
from src.Client.UX.Client_View import Ui_Form
from src.Client.model import Client
from PyQt4 import QtGui


class View_Client_Detail(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, client=None):
        super(View_Client_Detail, self).__init__()
        self.setupUi(self)
        print(client)

        # self.button_actions()

        self.main_window = parent

    def button_actions(self):
        self.broswe_button.clicked.connect(self.get_logo)
        self.action_button.clicked.connect(self.add_client)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = View_Client_Detail()
    ex.show()
    sys.exit(app.exec_())
