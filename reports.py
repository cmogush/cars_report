#!/usr/bin/env python3  # shebang

from reportlab.platypus import SimpleDocTemplate  # used to generate PDFs
from reportlab.platypus import Paragraph, Spacer, Table, Image  # flowables
from reportlab.lib.styles import getSampleStyleSheet  # used for document styles
from reportlab.lib import colors  # used for table styles

def generate(filename, title, additional_info, table_data):  # function to generate PDF
  styles = getSampleStyleSheet()  # sample dictionary of different styling
  report = SimpleDocTemplate(filename)  # export directory and filename
  report_title = Paragraph(title, styles["h1"])  # title style
  report_info = Paragraph(additional_info, styles["BodyText"])  # body style
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),  # table style
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")  # table info
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])  # generates PDF