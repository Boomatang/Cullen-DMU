import sys
from pathlib import Path as p
from PyQt5 import QtGui
from src.Merge import UpdateExcel

import src.UXDesign.RegisterUpdate as Update


class UpdateRegisterClass(QtGui.QWidget, Update.Ui_Form):
    def __init__(self, parent=None):
        super(UpdateRegisterClass, self).__init__(parent)
        self.r = None
        self.root = p('')
        self.source = p('')
        self.setupUi(self)
        self.button_actions()

    def button_actions(self):
        self.source_register.clicked.connect(self.get_source)
        self.main_register.clicked.connect(self.get_root)
        self.registerCompileStart.clicked.connect(self.run)

    def get_root(self):
        r = QtGui.QFileDialog.getOpenFileName()
        self.root = p(r)
        if self.root.is_file() and self.source.is_file():
            self.registerCompileStart.setEnabled(True)

    def get_source(self):
        r = QtGui.QFileDialog.getOpenFileName()
        self.source = p(r)
        if self.root.is_file() and self.source.is_file():
            self.registerCompileStart.setEnabled(True)

    def run(self):
        UpdateExcel.run(str(self.root), str(self.source))
        print('Im finished')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = UpdateRegisterClass()
    ex.show()
    sys.exit(app.exec_())
