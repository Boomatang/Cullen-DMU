import os

__author__ = 'Desktop'
from pathlib import Path as p
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def file_name():
    today = datetime.now()
    return "DXF Report ({}-{}-{})".format(today.year, today.month, today.day)


def column_size(padding, number_col, width):
    x = width - (padding * 2)
    col = x / number_col

    output = []
    y = 0
    while y < number_col:
        if len(output) < 1:
            output.append(padding)
            y += 1
        else:
            output.append(output[0] + (col * y))
            y += 1

    return output


def create_pdf(root, files):
    folder = report_folder(root)
    file = file_name()

    width, height = A4

    save_name = os.path.join(folder, file + ".pdf")

    c = canvas.Canvas(save_name)

    c.setLineWidth(.3)

    # Set the header
    c.setFont('Helvetica', 24)
    c.drawCentredString(width / 2, height - 50, file)
    height -= 50

    # create headings
    c.setFont('Helvetica', 12)

    c.line(25, height - 35, width - 25, height - 35)
    col1, col2, col3, col4 = column_size(25, 4, width)
    # print(col1, col2, col3, col4)

    c.drawString(col1, height - 30, "File Name")
    c.drawString(col2, height - 30, "First Created")
    c.drawString(col3, height - 30, "Last Exported")
    c.drawString(col4, height - 30, "Possible Error")
    height -= 35

    # Page contents

    for file in files:
        if height > 50:
            height -= 15
            c.drawString(col1, height, file.name)
            # c.drawString(col2, height - 30, file.first_created)
            # c.drawString(col3, height - 30, file.created_date)
            if not file.changed:
                c.drawString(col4, height, "----")
            else:
                c.drawString(col4, height, "Yes")
        else:
            text = "Page #{}".format(c.getPageNumber())
            c.drawCentredString(width / 2, height - 10, text)
            c.showPage()
            height = A4[1] - 50
            c.drawString(col1, height, file.name)
            # c.drawString(col2, height - 30, file.first_created)
            # c.drawString(col3, height - 30, file.created_date)
            if not file.changed:
                c.drawString(col4, height, "----")
            else:
                c.drawString(col4, height, "Yes")
    text = "Page {}".format(c.getPageNumber())
    c.drawCentredString(width / 2,  40, text)
    c.save()


def report_folder(root):
    folder = p(root, "COMBINED", "Reports")
    if not folder.is_dir():
        folder.mkdir()
    return str(folder)

if __name__ == "__main__":
    here = "E:\Programming\Cullen-DMU\samples\\6148\Plate DXFs"
    file_list = None
    create_pdf(here, file_list)

