import sys
from pathlib import Path as p
from src.Merge import merge
from PyQt5.QtWidgets import *

import src.UXDesign.MergePDF as Merge


class MergePDFClass(QWidget, Merge.Ui_MergePDF):
    def __init__(self, parent=None):
        super(MergePDFClass, self).__init__(parent)
        self.r = None
        self.root = None
        self.setupUi(self)
        self.button_actions()

    def button_actions(self):
        # self.mergeSelectFolder.clicked.connect(self.get_root)
        # self.mergePDF.clicked.connect(self.run_merge)
        pass

    def get_root(self):
        # r = QFileDialog.getExistingDirectory()
        # self.root = p(r)
        # if self.root.is_dir():
        #     self.mergePDF.setEnabled(True)
        pass

    def run_merge(self):
        merge.run(str(self.root))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MergePDFClass()
    ex.show()
    sys.exit(app.exec_())
