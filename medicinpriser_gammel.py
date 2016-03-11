# - *- coding: utf- 8 - *-
from lxml import etree

doc = etree.parse('xml_test.xml')

root = doc.getroot()

counter = 0

for first_child in root[3]:
	for content in first_child:
		print content.tag
		if content.tag == ("{urn:schemas-microsoft-com:office:spreadsheet}Row"):
			print content.tag
			for cont in content.itertext():
				print cont
				counter += 1
				print counter

	#print "first_child", first_child.tag, first_child.attrib
#	for child in first_child:
		#print 'child', child.tag, child.attrib
#		for last_child in child:
#			print 'last_child', last_child.tag, last_child.attrib
#			for cell in last_child:
#				print cell.find('Cell')
#				print 'cell', cell.tag, cell.attrib, cell.text


#for data in root.findall('workbook'):
#	print type(data)


#etree.tostring(root)

#print etree.tostring(root, xml_declaration=True)


#count = 0

#for elt in doc.getiterator():
#    print elt
#    count += 1
#    print count
	

#1 hent fil fra medicinpriser.dk



#2 parse til sql

#3 søgninger i sql: den største prisstigning, gns prisstigning, firma med størst generel prisstigning, etc.