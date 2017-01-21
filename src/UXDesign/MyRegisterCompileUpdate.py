import sys
from PyQt5 import QtGui
import src.UXDesign.RegisterCompileUpdate as RegisterCompileUpdate


class RegisterCompileUpdateClass(QtGui.QDialog, RegisterCompileUpdate.Ui_Dialog):
    def __init__(self, parent=None):
        super(RegisterCompileUpdateClass, self).__init__(parent)
        self.setupUi(self)
        self.button_actions()

    def button_actions(self):
        # self.register_documnet.clicked.connect(self.get_register_document)
        # self.project_folder.clicked.connect(self.get_project_folder)
        # self.compile_to_folder.clicked.connect(self.get_destination_folder)
        # self.compile_package.clicked.connect(self.run)
        pass

    def run(self):
        print('I am running and I\'m the update')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = RegisterCompileUpdateClass()
    ex.show()
    sys.exit(app.exec_())
