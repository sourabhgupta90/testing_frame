from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm ,inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import *

styles = getSampleStyleSheet()

width, height = A4

paragraph =Paragraph("paragraph in canvas",styles["BodyText"])

c = canvas.Canvas("a.pdf", pagesize=A4)

paragraph.wrapOn(c, width, height)
paragraph.drawOn(c, 1.8 *inch,1.8 *inch )
c.save()

#elements = [] 
#doc = SimpleDocTemplate('rl_hello_platypus.pdf', pagesize=A4)
#doc.build([paragraph])
