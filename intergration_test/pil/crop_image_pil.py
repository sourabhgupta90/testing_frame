from PIL import Image
img = Image.open('follow-up.png')

left = 5
top = 5
width = 22
height = 18

box = (left, top, left+width, top+height)
area = img.crop(box)
area.save('follow-up-test', 'png')

left = 46
top = 10
width = 28
height = 25


left = 7
top = 13
width = 27
height = 25



left = 10
top = 57
width = 705
height = 30





