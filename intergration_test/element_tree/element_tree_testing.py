from xml.etree import ElementTree
def parse_html(html):
    root = ElementTree.fromstring('<body>{}</body>'.format(html))
    return root
f = open('test_html.html', 'r')

root = parse_html(f.read())
 
div_attrib = '' 
for divs in root.findall(".//div"):
    if "data-id" in divs.attrib and divs.attrib["data-id"] == "q-tf-band-trigger":
        div_attrib = divs.attrib

print div_attrib

#root.findall(".")
#root.findall('.//input')
#root.findall('.//button[@class="active"]')
