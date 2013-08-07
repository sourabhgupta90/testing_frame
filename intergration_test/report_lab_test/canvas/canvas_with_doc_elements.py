from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm ,inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

width, height = A4

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

styles = getSampleStyleSheet()
 
 
data = [
            ['Caves',         'Wumpus Population'],
            ['Deep Ditch',    50],
            ['Death Gully',   5000],
            ['Dire Straits',  600],
            ['Deadly Pit',    5],
            ['Conclusion',    'Run!']
       ]
 
ts = [
         ('ALIGN', (1,1), (-1,-1), 'CENTER'),
         ('LINEABOVE', (0,0), (-1,0), 1, colors.purple),
         ('LINEBELOW', (0,0), (-1,0), 1, colors.purple),
         ('FONT', (0,0), (-1,0), 'Times-Bold'),
         ('LINEABOVE', (0,-1), (-1,-1), 1, colors.purple),
         ('LINEBELOW', (0,-1), (-1,-1), 0.5, colors.purple,
          1, None, None, 4,1),
         ('LINEBELOW', (0,-1), (-1,-1), 1, colors.red),
         ('FONT', (0,-1), (-1,-1), 'Times-Bold')
     ]
 
table = Table(data, style=ts)

c = canvas.Canvas("a.pdf", pagesize=A4)
table.wrapOn(c, width, height)
table.drawOn(c, *coord(1.8, 2.6, inch))
c.save()
