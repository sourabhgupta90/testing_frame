import os
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.rl_config import defaultPageSize
from reportlab.graphics.barcode import code39
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.graphics.renderSVG import LINE_STYLES



styles=getSampleStyleSheet()
Elements=[]


def get_column_width(col_w, row_length):
    width, height = A4
    width = width - 600

    if col_w == 'standard':
        if row_length != 1:
            col_width = width / (row_length - 1)
            return [25] + [col_width for ele in range(row_length - 1)]
        else:
            return [width]
    else:
        return col_w

error = TableStyle([
    ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor(0xc0c0c0)),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(0xb93131))
])

normal = TableStyle([
    ('LINEBELOW', (1, 0), (-1, -1), 1, colors.HexColor(0xc0c0c0)),
])
        
large = TableStyle([
    ('LINEBELOW', (1, 0), (-1, -1), 2, colors.HexColor(0xc0c0c0)),
])

table_style = {
    'error': error,
    'normal': normal,
    'large': large
}


def get_table(data=None, ts=None, col_w='standard', l_w=0, h_a='LEFT', r_h=None):

    if data != None and col_w != None:
        col_w = get_column_width(col_w, len(data[0]))
    table_with_style = Table(
        data, colWidths=col_w, hAlign=h_a, rowHeights=r_h, repeatRows=1)

    if ts and ts in table_style:
        table_with_style.setStyle(table_style[ts])
    return table_with_style


title = PS(
    name='Heading1',
    fontSize=20,
    leading=22)

normal = PS(name='Heading2',
            fontSize=10,
            leading=12)

large = PS(name='Heading3',
           fontSize=16,
           leading=18)
paragraph_style = {
    'title': title,
    'normal': normal,
    'large': large
}

def error_table(response, value):
    response =  str(response)
    value = get_para(unicode(value), st='BodyText')
    error_matrix = [["Error in ", unicode(response), value]]
    status_table = add_status_into_table(error_matrix)
    print status_table
    table = get_table(status_table, l_w=1, ts='error', col_w='standard')  
    return table


def get_para(label, st=None):
    styles = getSampleStyleSheet()

    if st in paragraph_style:
        return Paragraph(label, paragraph_style[st])
    elif st == 'BodyText':
        st = styles["BodyText"]
        return Paragraph(label, st)
    else:
        return Paragraph(label)


doc = BaseDocTemplate('basedoc.pdf', rightMargin=10, leftMargin=10,
                          topMargin=75, bottomMargin=175,showBoundary=1 )

def add_status_into_table(table,status=None):
    empty_cell,new_table = [''],[]
    if status:
        images = get_image('static/img/' + status + '.png')
        empty_cell = [images]
    for row in table:
        row = empty_cell + row    
        new_table.append(row)
        empty_cell = ['']    
    return new_table


def foot1(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',19)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

Elements.append(get_table([['adfsssssssssssa','aafdsssssssss','aafsddddddd','aasdfffff','aasfddddd','a'],
                        ['adfsssssssssssa','aafdsssssssss','aafsddddddd','aasdfffff','aasfddddd','a'],
                        ['adfsssssssssssa','aafdsssssssss','aafsddddddd','aasdfffff','aasfddddd','a']
                    ],
    ts='normal', col_w='standard', l_w=1, h_a='LEFT', r_h=None))

Elements.append(error_table('erroasdfafdsr inc', 'fasdsdsdsd'))
Elements.append(Paragraph("Frame one column, "*500,styles['Normal']))

doc.addPageTemplates([PageTemplate(id='OneCol',frames=[frameT],onPage=foot1)])

doc.build(Elements)

os.system("xpdf basedoc.pdf")