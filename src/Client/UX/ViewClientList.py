import sys
from src.Client.UX.ClintList import Ui_Form, _fromUtf8
from src.Client.model import Client
from PyQt4 import QtGui


class ViewClientList(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ViewClientList, self).__init__()
        self.setupUi(self)
        self.main_window = parent

        self.setup_buttons()

    def setup_buttons(self):
        clients = Client.select_clients()

        for client in clients:
            button = self.add_client_button(client)
            button.clicked.connect(lambda: self.button_action(client))

        self.add_spacer()

    def add_client_button(self, client):
        client_name = QtGui.QPushButton(self.scrollAreaWidgetContents)
        client_name.setObjectName(_fromUtf8(client.name))
        client_name.setText(client.name)
        self.verticalLayout.addWidget(client_name)
        return client_name

    def add_spacer(self):
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def button_action(self, client):
        print(client.name)
        self.main_window.view_client_details(client)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = ViewClientList()
    ex.show()
    sys.exit(app.exec_())
