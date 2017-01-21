import sys
from PyQt5 import QtGui
from pathlib import Path as p
import src.UXDesign.registerCompile as RegisterCompile
from src.Merge import Compile, merge
from src.other.text_report import TextReport
from src.UXDesign.MyRegisterCompileUpdate import RegisterCompileUpdate
from src.Client.model import Client

class RegisterCompileClass(QtGui.QWidget, RegisterCompile.Ui_Form):
    def __init__(self, parent=None):
        super(RegisterCompileClass, self).__init__()
        self.client_list = Client.select_clients()
        self.register = p('')
        self.project = p('')
        self.destination_Folder = p('')
        self.update = RegisterCompileUpdate.Ui_Dialog()
        self.setupUi(self)
        self.button_actions()
        print(self.client_list)
        self.dropbox_update()

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

    def dropbox_update(self):
        count = len(self.client_list) - 1
        i = 0

        while i <= count:
            self.client_list_box.addItem(self.client_list[i].name)
            i += 1


    def run(self):

        name = self.client_list_box.currentText()

        client = Client.get_client_by_name(name)
        print(client.name)

        '''
        print('I am running')
        files = Compile.run(str(self.register), str(self.project))
        folder = Compile.create_date_folder(str(self.destination_Folder))
        Compile.copy_files(files['normal'], str(folder))
        tsd_files = []
        for file in files['tsd']:
            tsd_files.append(merge.PDF(p(file.path)))
        tsd_files = merge.newest_file(tsd_files)
        tsd_files = merge.group_files(tsd_files)
        tsd_files = merge.sort_files(tsd_files)

        tsd_finish = merge.FinishPDF(folder, tsd_files)
        print('Merging files')
        tsd_finish.run(finish=True)
        print(str(folder))
        report = TextReport(files['error'], files['progress'], files['ignore'], str(folder))
        report.run()
        print('Finished')
        '''

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = RegisterCompileClass()
    ex.show()
    sys.exit(app.exec_())
