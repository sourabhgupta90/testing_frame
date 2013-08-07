from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import PageTemplate, Frame, NextPageTemplate, BaseDocTemplate, SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

#c = canvas.Canvas("tables.pdf")
doc = SimpleDocTemplate("mwi.pdf",pagesize=letter,
                    rightMargin=72,leftMargin=72,
                    topMargin=72,bottomMargin=60)

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Table Top Black Back', fontName ='Helvetica',fontSize=14, leading=16,backColor = colors.black, textColor=colors.white, alignment=TA_LEFT))
styles.add(ParagraphStyle(name='Table Top Red Back', fontName ='Helvetica',fontSize=9, leading=12, backColor = colors.red, textColor=colors.black, alignment=TA_LEFT))

styleN = styles["BodyText"]

# Header
# report: topic/subtopic overview
report = []
ptext = 'Test' 
report.append(Paragraph(ptext, styles["Table Top Black Back"]))
report.append(Spacer(1, 24))

ptext = 'Test' 
report.append(Paragraph(ptext, styles["Table Top Black Back"]))
report.append(Spacer(1, 24))

ptext = 'Test' 
report.append(Paragraph(ptext, styles["Table Top Red Back"]))
report.append(Spacer(1, 48))

# Build Document
doc.build(report)
