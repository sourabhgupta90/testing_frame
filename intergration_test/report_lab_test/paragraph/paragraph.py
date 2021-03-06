from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
 
# Our container for 'Flowable' objects
elements = []
 
# A large collection of style sheets pre-made for us
styles = getSampleStyleSheet()
 
# A basic document for us to write to 'rl_hello_platypus.pdf'
doc = SimpleDocTemplate('rl_hello_platypus.pdf')
 
# Create two 'Paragraph' Flowables and add them to our 'elements'

elements.append(Paragraph('<b>The Platypus<img src="../images/testimg.gif" valign="top"/></b>', styles['Heading1']))
elements.append(Paragraph("Very <i>Special</i>!", styles['Normal']))
 
# Write the document to disk
doc.build(elements)
