from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
import os
import urllib2
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

filename = './python-logo.JPEG'  

def get_python_image():
    """ Get a python logo image for this example """
    if not os.path.exists(filename):
        response = urllib2.urlopen(
            'http://www.python.org/community/logos/python-logo.png')
        f = open(filename, 'w')
        f.write(response.read())
        f.close()

get_python_image()

 
# Our container for 'Flowable' objects
elements = []
 
# A large collection of style sheets pre-made for us
styles = getSampleStyleSheet()
 
# A basic document for us to write to 'rl_hello_platypus.pdf'
doc = SimpleDocTemplate('rl_hello_platypus.pdf')
 
# Create two 'Paragraph' Flowables and add them to our 'elements'

elements.append(Paragraph("The Platypus", styles['Heading1']))
elements.append(Paragraph("Very <i>Special</i>!",
 styles['Normal']))

elements.append(Image(filename)) 
# Write the document to disk
doc.build(elements)

