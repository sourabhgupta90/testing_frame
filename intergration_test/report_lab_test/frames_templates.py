from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, A4 , inch
from reportlab.platypus import *
from reportlab.lib import colors
from  reportlab.lib.styles import ParagraphStyle as PS  
from reportlab.rl_config import defaultPageSize
import os
import urllib2
from reportlab.lib.units import mm
from reportlab.graphics.barcode import code39
from reportlab.pdfgen import canvas 
import StringIO


style = getSampleStyleSheet()['Normal']
style.fontName = 'Helvetica'
style.spaceAfter = 15

import StringIO

story = [Paragraph('asdf',style),Paragraph('asdf',style),Paragraph('asdf',style),Paragraph('asdf',style)] 
generated_file = StringIO.StringIO()
frame1 = Frame(50,100,245,240, showBoundary=0)
frame2 = Frame(320,100,245,240, showBoundary=0)
page_template = PageTemplate(frames=[frame1,frame2])
doc = BaseDocTemplate(generated_file,pageTemplates=[page_template])
doc.build(story)
