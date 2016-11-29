from datetime import datetime
import time
import os
from pathlib import Path as p
from pprint import pprint
from zipfile import ZipFile
from src.other.Reporting import create_pdf


def run(root):
    # print("Root Path : {}".format(root))
    all_files = (DXFFile(i) for i in path_walk(root))

    all_files = newest_file(all_files)
    files = list(all_files.values())
    files.sort()
    add_files_to_zip(files, root)

    create_pdf(root, files)

    # pprint(files)


def file_name():
    today = datetime.now()
    return "DXF Files ({}-{}-{}).zip".format(today.year, today.month, today.day)


def add_files_to_zip(files, root):
    root = p(root, "COMBINED")
    if not root.is_dir():
        root.mkdir()
    save_path = p(str(root), file_name())

    with ZipFile(str(save_path), 'w') as myzip:
        for file in files:
            myzip.write(file.full_path, file.name)


def first_created(file, test):
    if file.first_created is not None:
        if file.first_created > test.first_created:
            file.first_created = test.first_created

    else:
        file.first_created = test.first_created

    return file


def newest_file(files):
    output = {}
    for file in files:
        if file.name in output.keys():
            test = output.get(file.name)
            if file.created_date > test.created_date:
                file = first_created(file, test)

            if check_file(file.full_path, test.full_path):
                file.changed = True
                file.created_date = test.created_date
            output[file.name] = file

        else:
            file.first_created = file.created_date
            output.setdefault(file.name, file)
    return output



def check_file(file, file2):
    x = 1
    y = 0
    passed = True
    these = [448, 452, 456, 460, 888]
    with open(file) as f:
        with open(file2) as f2:
            f_lines = f.readlines()
            f2_lines = f2.readlines()
            for line1, line2 in zip(f_lines, f2_lines):
                if x not in these:
                    if line1 != line2:
                        # print("line1 : {}, line2 : {}, on line {}".format(line1, line2, x))
                        y += 1
            if y > 5:
                # print("File Error count : {}".format(y))
                passed = False
    return passed


def path_walk(path):
    excluded = ["COMBINED"]

    for root, dirs, files in os.walk(path):
        for exclude in excluded:
            if exclude in dirs:
                dirs.remove(exclude)

        for file in files:
            file = p(os.path.join(root, file))

            if find_file_type(file.suffix):
                yield file


def find_file_type(suffix):
    types = [".dxf"]

    if suffix.lower() in types:
        return True
    else:
        return False


class DXFFile:
    def __init__(self, path):
        # self.file = p(path)
        self.file = path
        self.name = self.file.name
        self.full_path = str(self.file)
        self.created_date = self.file.stat().st_mtime
        self.first_created = None
        self.hash = None
        self.change_date = None
        self.changed = False
        self.old_hash = None

    @staticmethod
    def date_format(change_time):
        return time.ctime(change_time)

    def __repr__(self):
        return "<File Name: {}, File Changed: {}>".format(self.name, self.changed)

    def __lt__(self, other):
        return self.name < other.name