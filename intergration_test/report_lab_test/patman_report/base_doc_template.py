## {{{ http://code.activestate.com/recipes/123612/ (r1)
"""
examples of reportlab document using
BaseDocTemplate with
2 PageTemplate (one and two columns)

"""
import os
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet


styles=getSampleStyleSheet()
Elements=[]

doc = BaseDocTemplate('basedoc.pdf',showBoundary=1)

def foot1(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',19)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()
def foot2(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

#normal frame as for SimpleFlowDocument
frameT = Frame(doc.leftMargin, 700, doc.width, doc.height/6, id='normal')

#Two Columns
frame1 = Frame(doc.leftMargin, 200, doc.width/2-6, doc.height/4, id='col1')
frame2 = Frame(doc.leftMargin+doc.width/2+6, 200, doc.width/2-6,
               doc.height/4, id='col2')

styleSheet = getSampleStyleSheet()
h1 = styleSheet['Heading1']
h1.pageBreakBefore = 1
h1.keepWithNext = 1

h2 = styleSheet['Heading2']
h2.frameBreakBefore = 1
h2.keepWithNext = 1

Elements.append(NextPageTemplate('OneCol'))

Elements.append(Paragraph("Frame one column, "*50,styles['Normal']))
#Elements.append(NextPageTemplate('TwoCol'))
Elements.append(Paragraph("Frame two columns,"*50,h2))


Elements.append(Paragraph("Une colonne",styles['Normal']))
doc.addPageTemplates([PageTemplate(id='OneCol',frames=[frameT,frame1,frame2],onPage=foot1),
                      
                      #PageTemplate(id='TwoCol',frames=[frame1,frame2],onPage=foot2),
                      ])
#start the construction of the pdf
doc.build(Elements)

# use external program xpdf to view the generated pdf
os.system("xpdf basedoc.pdf")
## end of http://code.activestate.com/recipes/123612/ }}}
