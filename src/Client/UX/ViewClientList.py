import sys
from src.Client.UX.ClintList import Ui_Form, _fromUtf8
from src.Client.model import Client
from PyQt5 import QtGui


class ViewClientList(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ViewClientList, self).__init__()
        self.setupUi(self)
        self.main_window = parent

        self.setup_buttons()
        # self.setup()


    def setup(self):
        clients = Client.select_clients()
        button_list = []

        for client in clients:
            button_list.append(ClientButton(self, client))

        for button in button_list:
            button.add()
            print(button.id)
            button.add_action()




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
        print(client)
        self.main_window.view_client_details(client)


class ClientButton(QtGui.QPushButton):

    def __init__(self, parent=None, client=None):
        super(ClientButton, self).__init__()

        self.parent = parent
        self.name = client.name
        self.id = client.id

    def add_action(self):
        self.clicked.connect(self.next_view)

    def add(self):
        client_name = QtGui.QPushButton(self.parent.scrollAreaWidgetContents)
        client_name.setObjectName(_fromUtf8(self.name))
        client_name.setText(self.name)
        self.parent.verticalLayout.addWidget(client_name)

    def next_view(self):
        self.parent.button_action(self.id)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = ViewClientList()
    ex.show()
    sys.exit(app.exec_())
