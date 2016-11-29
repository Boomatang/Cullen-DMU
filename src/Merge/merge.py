import datetime
import time
import os
from pathlib import Path as p
from PyPDF2 import PdfFileMerger
from pprint import pprint


def group_files(files):
    output = {}
    values = files.values()

    wbs = (i.wbs for i in values)

    for wb in wbs:
        if wb in output.keys():
            pass
        else:
            output.setdefault(wb, {})

    file_list = (a for a in files.values())
    for file in file_list:
        if file.discipline in output[file.wbs].keys():
            output[file.wbs][file.discipline].append(file)
        else:
            output[file.wbs].setdefault(file.discipline, [file])
    return output


def sort_files(dict_of_lists):
    keys = dict_of_lists.keys()
    for key in keys:
        list_wbs = dict_of_lists.get(key)
        wbs_keys = list_wbs.keys()

        for wbs in wbs_keys:
            dict_of_lists[key][wbs] = sorted(dict_of_lists[key][wbs], key=lambda PDF: PDF.name)

    return dict_of_lists


def get_wbs_and_disp(all_files):
    output = {}
    all_wbs = all_files.keys()

    for wbs in all_wbs:
        disp = all_files[wbs].keys()
        output.setdefault(wbs, disp)
    return output


def run(root):
    all_files = (PDF(i) for i in path_walk(root))
    all_files = newest_file(all_files)
    all_files = group_files(all_files)
    all_files = sort_files(all_files)

    wbs_and_disp = get_wbs_and_disp(all_files)

    folders = Folder(wbs_and_disp)

    folders.find_root_dir(root)
    folders.create_folders()

    combined_pdfs = FinishPDF(folders.date_folder, all_files)
    combined_pdfs.run()

    print('Finished')


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
    types = [".pdf"]

    if suffix.lower() in types:
        return True
    else:
        return False


def newest_file(files):
    output = {}
    for file in files:
        if file.name in output.keys():
            test = output.get(file.name)
            if file.version > test.version:
                output[file.name] = file
        else:
            output.setdefault(file.name, file)
    return output


class PDF:
    def __init__(self, path_obj):
        self.path_obj = path_obj
        self.full_name = self.path_obj.name
        self.full_path = str(self.path_obj)
        self.wbs = self.what_wbs()
        self.name, self.version = self.what_revision()
        self.project = self.what_project()
        self.discipline = self.get_discipline()
        self.create_date = 0

    def what_wbs(self):
        temp = self.full_name.split("-")

        types = ["vn", "pl", "se", "ga"]

        if temp[1][:2].lower() not in types:
            return temp[1][:2]
        else:
            return "Global"

    def what_revision(self):
        temp = self.full_name.split('.')
        temp = temp[0].split("_")
        return temp[0], temp[-1]

    def what_project(self):
        temp = self.full_name.split('-')
        return temp[0]

    def get_discipline(self):
        temp = self.full_name.split("-", 2)

        if temp[1].lower().startswith("vn"):
            return "VENDOR"
        elif temp[1].lower().startswith("pl"):
            return "PLATE"
        elif temp[1].lower().startswith("se"):
            return "SECTION"
        elif temp[1][3:5].lower().startswith("ga"):
            temp = self.full_name.split("-")
            return temp[3]
        else:
            return temp[1][2:4].upper()

    def __repr__(self):
        return "<File : %s>" % self.full_name


class Folder:

    def __init__(self, folder_names):
        self.folders = folder_names
        self.root_folder = None
        self.combine = None
        self.date_folder = None

    def find_root_dir(self, root):
        root = p(root)
        self.root_folder = "Pdf's"

        if self.root_folder in root.parts:
            print(root.parts)
            i = root.parts.index(self.root_folder)
            print(i)
            self.root_folder = p(*[i for i in root.parts[:i+1]])
            print(self.root_folder.absolute())
        else:
            for root, dirs, files in os.walk(str(root)):

                for d in dirs:
                    d = p(root, d)
                    if d.name == self.root_folder:
                        self.root_folder = d
                        return

    def create_combine(self):

        folder = p(self.root_folder, "COMBINED")

        if folder.is_dir():
            self.combine = folder
        else:
            folder.mkdir()
            self.combine = folder

    def create_date(self):
        today = datetime.date.fromtimestamp(time.time())
        folder_name = "{}-{}-{}".format(today.year, today.month, today.day)

        folder = p(self.combine, folder_name)

        if not folder.is_dir():
            folder.mkdir()

        self.date_folder = folder

    def create_WBS(self, area):
        folder = p(self.date_folder, area)

        if not folder.is_dir():
            folder.mkdir()

    def create_folders(self):
        self.create_combine()
        self.create_date()

        keys = self.folders.keys()

        for key in keys:
            values = self.folders.get(key)
            self.create_WBS(key)
            # for value in values:
            #     paths = os.path.join(key, value)
            #     self.create_WBS(paths)


class FinishPDF:

    def __init__(self, date_folder, all_files):
        self.date_folder = date_folder
        self.all_files = all_files

    def run(self, finish=False):
        wbs_keys = self.all_files.keys()

        for key in wbs_keys:
            disp_keys = self.all_files[key].keys()
            for disp in disp_keys:
                values = self.all_files[key].get(disp)
                self.create_pdf(values, finish)

    def name_builder(self, wbs, disp, finish=False):
        today = datetime.date.fromtimestamp(time.time())
        file_name = "{} ({}-{}-{}).pdf".format(disp, today.year, today.month, today.day)
        if finish:
            file_name = p(self.date_folder, file_name)
        else:
            file_name = p(self.date_folder, wbs, file_name)

        return str(file_name)

    def create_pdf(self, combine_files, finish=False):
        merger = PdfFileMerger()
        wbs = None
        disp = None
        for file in combine_files:
            if wbs is None:
                wbs = file.wbs
                disp = file.discipline
            file = open(file.full_path, "rb")
            merger.append(file)
        output = open(self.name_builder(wbs, disp, finish=finish), "wb")
        merger.write(output)
