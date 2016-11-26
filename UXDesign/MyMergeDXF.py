import sys
from pathlib import Path as p
from Merge import mergeDXF as merge
from PyQt4 import QtGui

import UXDesign.MergeDXF as Merge


class MergeDXFClass(QtGui.QWidget, Merge.Ui_MergeDXF):
    def __init__(self, parent=None):
        super(MergeDXFClass, self).__init__(parent)
        self.r = None
        self.root = None
        self.setupUi(self)
        self.button_actions()

    def button_actions(self):
        self.mergeSelectFolder.clicked.connect(self.get_root)
        self.mergeDXF.clicked.connect(self.run_merge)

    def get_root(self):
        r = QtGui.QFileDialog.getExistingDirectory()
        self.root = p(r)
        if self.root.is_dir():
            self.mergeDXF.setEnabled(True)

    def run_merge(self):
        merge.run(str(self.root))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = MergeDXFClass()
    ex.show()
    sys.exit(app.exec_())
