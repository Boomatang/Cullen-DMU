import datetime
import time
import os


class TextReport:
    def __init__(self, error, progress, ignore, folder):
        self.error = error
        self.progress = progress
        self.ignore = ignore

        self.file = os.path.join(folder, 'report {}.txt'.format(self.date_format()))

    def run(self):

        with open(self.file, 'w') as file:

            self.header(file)

            if len(self.error) > 0:
                self.write_list('ERROR', self.error, file)

            if len(self.progress) > 0:
                self.write_list('In Progress', self.progress, file)

            if len(self.ignore) > 0:
                self.write_list('Files Ignored', self.ignore, file)

            file.write('--------------')

    def header(self, file):
        today = datetime.date.fromtimestamp(time.time())
        today = "Date : {}/{}/{}".format(today.day, today.month, today.year)

        title = 'Title : Un-complied Files'

        file.write(title + "\n")
        file.write(today + "\n\n")

    @staticmethod
    def date_format():
        today = datetime.date.fromtimestamp(time.time())
        return "({}-{}-{})".format(today.year, today.month, today.day)

    def write_list(self, title, items, file):

        title = '----- {} -----\n\n'.format(title)
        end = '\n\n'

        file.write(title)
        for item in items:
            file.write('File Name : {}\t\tRow : {}\n'.format(item.name, item.row))
        file.write(end)


if __name__ == '__main__':
    path = "/home/boomatang/Projects/Python/Cullen-DMU/samples/Sample Job/testing ground/Compile Package/Compile To Folder"
    testing = TextReport(['error'], ['progress'], ['ignore'], path)
    testing.run()