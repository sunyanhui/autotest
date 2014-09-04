import os 
from PIL import Image
j = 1
dir="./code/"


img = Image.open('input-black.gif')
for i in range(4): 
	x = 7 + i*13
	y = 3
	img.crop((x, y, x+9, y+13)).save("%d.GIF" % j) 
	print "j=",j 
	j += 1


# for f in os.listdir(dir):
#     if f.endswith(".jpg"):
#         img = Image.open(dir+f)
#         for i in range(4): 
#             x = 7 + i*13
#             y = 3
#             img.crop((x, y, x+9, y+13)).save("font/%d.jpg" % j) 
#             print "j=",j 
#             j += 1