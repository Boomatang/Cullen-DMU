import sys
from pathlib import Path as p


from src.Client.UX.Add_Update import Ui_Form
from src.Client.model import Client
from PyQt5.QtWidgets import *


class AddClient(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(AddClient, self).__init__()
        self.r = None
        self.logo = None
        self.setupUi(self)

        self.cancel_button.close()
        self.info_label.hide()
        self.action_button.setText('Add Client')

        self.button_actions()

        self.main_window = parent

    def button_actions(self):
        self.broswe_button.clicked.connect(self.get_logo)
        self.action_button.clicked.connect(self.add_client)

    def get_logo(self):
        r = QFileDialog.getOpenFileName()
        self.logo = p(r)
        self.logo_path.setText(str(self.logo))

    def add_client(self):

        if len(self.client_name.displayText()) > 0:
            self.info_massage('Adding Client to database...')
            Client.add_client(self.client_name.displayText(), self.logo_path.displayText())
            self.info_massage('Client added')

            try:
                self.main_window.view_client_list()
            except AttributeError:
                self.info_massage('An internal error happened please try again')
        else:
            self.info_massage('Please enter a Client name before continuing!')

    def info_massage(self, text):
        self.info_label.hide()
        self.info_label.setText(text)
        self.info_label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AddClient()
    ex.show()
    sys.exit(app.exec_())
