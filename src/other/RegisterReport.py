from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from PIL import Image


class RegisterReport:

    def __init__(self, file_name, data):
        self.MAX_IMAGE_SIZE = (260, 90)
        self.style = None
        self.page_frame = None
        self.doc = self.create_document(file_name)
        self.PAGE_HEIGHT = self.doc.height
        self.data = data
        self.doc_story = []
        self.doc_table_row_data = []
        self.date_line = 'Date: {}'.format(self.data.date)
        self.project_title_line = 'Project: {}'.format(self.data.project_title)
        self.create_page_templates()

    @staticmethod
    def create_document(name):
        return BaseDocTemplate(name, showBoundary=1)

    def create_all_styles(self):
        styles = getSampleStyleSheet()
        self.style = styles['Normal']

    def format_header(self, canvas):
        canvas.setFont('Times-Roman', 14)
        canvas.drawImage(self.image_file(), 36, self.PAGE_HEIGHT+10)
        canvas.drawString(300, self.PAGE_HEIGHT + 70, self.project_title_line)
        canvas.drawString(300, self.PAGE_HEIGHT+50, self.date_line)

    def static_page(self, canvas, doc):
        canvas.saveState()
        self.format_header(canvas)
        self.format_footer(canvas)
        canvas.setFont('Times-Roman', 9)
        canvas.restoreState()

    def format_page_frame(self):
        return Frame(self.doc.leftMargin / 2,
                     self.doc.bottomMargin / 2,
                     self.doc.width + self.doc.leftMargin,
                     self.doc.height * 0.95,
                     id='normal')

    def create_page_templates(self):
        self.doc.addPageTemplates([
            PageTemplate(id='Page', frames=self.format_page_frame(), onPage=self.static_page)
        ])

    def build_story(self):
        self.doc_story.append(self.build_table())

    def build_final_document(self):
        self.build_story()
        self.doc.build(self.doc_story)

    def image_file(self):
        return ImageReader(self.make_resized_image_byte_stream())

    def format_footer(self, canvas):
        canvas.setFont('Times-Roman', 9)
        canvas.drawString(inch, 0.75 * inch, "Page {}".format(self.doc.page))

    def build_table(self):
        table = Table(self.format_table_data())
        table.setStyle(self.style_table())

        return table

    def make_resized_image_byte_stream(self):
        data = BytesIO()
        image = self.image_resize()
        image.save(data, format='png')
        data.seek(0)
        return data

    def image_resize(self):
        image = Image.open(self.data.image)
        image.thumbnail(self.MAX_IMAGE_SIZE, Image.ANTIALIAS)
        return image

    def style_table(self):
        # TODO this needs to be filled in
        return self.test_style()

    def format_table_data(self):
        # TODO this needs to be filled in
        return self.test_data()

    def test_data(self):
        return [('', 'Day', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'),
                ('', 'Month', '05', '07'),
                ('', 'Year', '17', '17'),
                ('6165-AABE006', 'WELDMENT 6165-AABE006 DETAILS', 'A'),
                ('6165-AABE007', 'WELDMENT 6165-AABE007 DETAILS'),
                ('6165-AABE008', 'WELDMENT 6165-AABE008 DETAILS'),
                ('6165-AABE009', 'WELDMENT 6165-AABE009 DETAILS'),
                ('17-999W-P999', 'SOME OTHER TITLE THAT IS NOT ')]


    def test_style(self):
        return TableStyle([('ALIGN', (0,0), (-2,-1), 'RIGHT'),
                          ('GRID', (0, 3), (15, 7), 1, colors.black),
                          ('LINEBEFORE', (2, 0), (2, 2), 1, colors.black),
                          ('LINEBEFORE', (3, 0), (3, 2), 1, colors.black),
                          ('LINEBEFORE', (4, 0), (4, 2), 1, colors.black),
                          ('LINEBEFORE', (5, 0), (5, 2), 1, colors.black),
                          ('LINEBEFORE', (6, 0), (6, 2), 1, colors.black),
                          ('LINEBEFORE', (7, 0), (7, 2), 1, colors.black),
                          ('LINEBEFORE', (8, 0), (8, 2), 1, colors.black),
                          ('LINEBEFORE', (9, 0), (9, 2), 1, colors.black),
                          ('LINEBEFORE', (10, 0), (10, 2), 1, colors.black),
                          ('LINEBEFORE', (11, 0), (11, 2), 1, colors.black),
                          ('LINEBEFORE', (12, 0), (12, 2), 1, colors.black),
                          ('LINEBEFORE', (13, 0), (13, 2), 1, colors.black),
                          ('LINEBEFORE', (14, 0), (14, 2), 1, colors.black),
                          ('LINEBEFORE', (15, 0), (15, 2), 1, colors.black),
                          ('LINEBEFORE', (16, 0), (16, 2), 1, colors.black)
                          ])


class RegisterData:
    def __init__(self):
        self.date = None
        self.project_title = None
        self.image = '/home/boomatang/Projects/Python/Cullen-DMU/NoteBooks/image.png'

if '__main__' == __name__:
    data = RegisterData()
    data.date = '11/01/2017'
    data.project_title = 'Test data title'

    report = RegisterReport('testregister.pdf', data)
    report.build_final_document()