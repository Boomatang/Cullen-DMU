import sys
from PyQt4 import QtGui
from pathlib import Path as p
import UXDesign.registerCompile as RegisterCompile
from Merge import Compile


class RegisterCompileClass(QtGui.QWidget, RegisterCompile.Ui_Form):
    def __init__(self, parent=None):
        super(RegisterCompileClass, self).__init__(parent)
        self.register = p('')
        self.project = p('')
        self.destination_Folder = p('')
        self.setupUi(self)
        self.button_actions()

    def button_actions(self):
        self.register_documnet.clicked.connect(self.get_register_document)
        self.project_folder.clicked.connect(self.get_project_folder)
        self.compile_to_folder.clicked.connect(self.get_destination_folder)
        self.compile_package.clicked.connect(self.run)

    def get_project_folder(self):
        r = QtGui.QFileDialog.getExistingDirectory()
        self.project = p(r)
        self.test_ok()

    def get_register_document(self):
        r = QtGui.QFileDialog.getOpenFileName()
        self.register = p(r)
        self.test_ok()

    def get_destination_folder(self):
        r = QtGui.QFileDialog.getExistingDirectory()
        self.destination_Folder = p(r)
        self.test_ok()

    def test_ok(self):
        try:
            if self.project.is_dir() and self.register.is_file() and self.destination_Folder.is_dir():
                # self.registerCompileStart.setEnabled(True)
                self.compile_package.setEnabled(True)
        except AttributeError as e:
            print('Possible button Fail: {}'.format(e))

    def run(self):
        print('I am running')
        Compile.run(str(self.register), str(self.project), str(self.destination_Folder))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = RegisterCompileClass()
    ex.show()
    sys.exit(app.exec_())
