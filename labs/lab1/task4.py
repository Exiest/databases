import lxml.etree as tree

xml = tree.parse('files/veliki.xml')
xslt_tmp = tree.parse('files/veliki.xslt')
xslt = tree.XSLT(xslt_tmp)
fXml = xslt(xml)
with open('files/veliki.html', 'wb') as f:
    f.write(tree.tostring(fXml, pretty_print=True, encoding="UTF-8"))