from lxml import etree

root = None
with open('files/ridnaua.xml', encoding="utf-8") as file:
    root = etree.parse(file)

pages = root.xpath('//page')

i = 0

for page in pages:
    print('Fragments on page %i = %f' % (i, page.xpath('count(.//fragment[@type="image"])')))
    i += 1

