import os

def create_pdf(sometext):
    outfilename = "myfile.pdf"
    outfiledir = '/somedir'
    outfilepath = os.path.join( outfiledir, outfilename )
    doc = SimpleDocTemplate( outfilepath )
