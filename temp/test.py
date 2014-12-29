#coding=utf-8
# from PIL import Image

# im = Image.open('2.bmp')
# ss = im.split()
# im2 = Image.open('0000.gif')
# print im.size,im.mode,im.getbands()
# l = im.getdata()
# l1 = im2.getdata()
# print l[1], im.getbbox(), ss[0].histogram()
# print l1[1], im2.histogram()
# x = 0
# i = 0
# l = r.getdata()
# for y in xrange(b):
# 	for x in xrange(a):
# 		print list(l)[i],
# 		i = i+1
# 	print '\r\n'
#coding=utf-8
# import xlrd
#
# excel = xlrd.open_workbook(u"element.xls")
# print excel.sheet_names()


import re
s = "共11条，共1111页"
r = re.compile("(\d+)")
print r.findall(s)