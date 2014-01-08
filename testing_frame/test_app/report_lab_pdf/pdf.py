from reportlab.platypus.flowables import Flowable
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from StringIO import StringIO
from reportlab.lib.pagesizes import A4

styles = getSampleStyleSheet()


class PdfRenderer():

    def __init__(self):
        self.elements = []
        self.response = StringIO()

    def foot1(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 19)
        canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
        canvas.restoreState()

    def render_pdf(self):
        self.elements.append(Paragraph("Frame one column," * 50,\
                                        styles['Normal']))
        self.elements.append(splitframe("Frame one column",\
                                         styles['Normal']))

    def get_pdf(self, request):
        doc = BaseDocTemplate(self.response, rightMargin=10, leftMargin=10,
                          topMargin=190, bottomMargin=125, pagesize=A4)
        frameT = Frame(doc.leftMargin, 10, doc.width, doc.height, id='normal')
        doc.addPageTemplates([PageTemplate(id='OneCol', frames=[frameT], \
                                                onPage=self.foot1)])
        doc.build(self.elements)
        return self.response.getvalue()


class splitframe(Flowable):

    def __init__(self, paragraphText="", style=styles["Normal"]):
        self.paragraphText = paragraphText
        self.style = styles["Normal"]

    def split(self):
        return []

    def draw(self):
        pass

    def wrap(self, canv, aW, aH):
        
        self.canv = canv
        w, h = self.wrap(aW, aH)
        del self.canv
        return w, h
