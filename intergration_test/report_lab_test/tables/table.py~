from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors
import reportlab.lib.textsplit
from reportlab.lib.styles import ParagraphStyle as PS

# Our container for 'Flowable' objects
elements = []
 
# A large collection of style sheets pre-made for us
styles = getSampleStyleSheet()
 
# A basic document for us to write to 'rl_hello_table.pdf'
doc = SimpleDocTemplate('rl_hello_table.pdf')
 
elements.append(Paragraph("Wumpus vs Cave Population Report",
 styles['Title']))
 


title = PS(name='Heading1',
           fontSize=16,
           leading=17)

large = PS(name='Heading2',
           fontSize=11,
           leading=13)

normal = PS(name='Heading3',
            fontSize=8,
            leading=10,
            wordWrap = 'CJK')

paragraph_style = {
    'title': title,
    'large': large,
    'normal': normal,
    
}
p = Paragraph( "easfddddddfdsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddddddddddddddddddddddddddddddddddddddddddddddddddddddddsaaaaaaaaaaaaaaaaaaaaaasteatefasd" , paragraph_style['normal'] )
 
data = [['Caves',         'sd'],
        ['Deep Ditch',    p],
        ['Death Gully',   5000],
        ['Dire Straits',  600],
        ['Deadly Pit',    5],
        ['Conclusion',    'Run!']]
 
# First the top row, with all the text centered and in Times-Bold,
# and one line above, one line below.
ts = [('ALIGN', (1,1), (-1,-1), 'CENTER'),
     ('LINEABOVE', (0,0), (-1,0), 1, colors.purple),
     ('LINEBELOW', (0,0), (-1,0), 1, colors.purple),
     ('FONT', (0,0), (-1,0), 'Times-Bold'),
 
# The bottom row has one line above, and three lines below of
# various colors and spacing.
     ('LINEABOVE', (0,-1), (-1,-1), 1, colors.purple),
     ('LINEBELOW', (0,-1), (-1,-1), 0.5, colors.purple,
      1, None, None, 4,1),
     ('LINEBELOW', (0,-1), (-1,-1), 1, colors.red),
     ('FONT', (0,-1), (-1,-1), 'Times-Bold')]
 
# Create the table with the necessary style, and add it to the
# elements list.

table = Table(data,colWidths=[200,200])
table.setStyle(ts)
elements.append(table)
 
# Write the document to disk
doc.build(elements)
