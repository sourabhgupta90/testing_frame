from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

from reportlab.graphics.barcode import code39


c=canvas.Canvas("barcode_example.pdf",pagesize=A4)

barcode=code39.Extended39("123456789",barWidth=0.2*mm,barHeight=10*mm)
# drawOn puts the barcode on the canvas at the specified coordinates
barcode.drawOn(c,100*mm,50*mm)

# now create the actual PDF
c.showPage()
c.save()
