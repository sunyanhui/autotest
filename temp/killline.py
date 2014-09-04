import os 
from PIL import Image

white = 0
black = 255
def get_left_start_point(im):
    start_point = (0,0)
    found = False
    w, h = im.size
    data = list(im.getdata())
    for x in xrange(w):
        for y in xrange(h):
            if data[ y*w + x ] != white:
                found = True
                start_point = (x,y)
                break
         
        if found:
            break
    return start_point

def remove_line(im, aim):
    w,h = im.size
    data = list( im.getdata() )
    
    for x,y in aim:
        curr = data[ y * w + x ]
        prev = data[ (y-1) * w + x]
        next = data[ (y+1) * w + x]
        
        if prev == black and next == black:
            continue
        
        if prev == black:
            data[ y * w + x ] = white
            data[ (y-1) * w + x] = white

            
        elif next == black:
            data[ y * w + x ] = white
            data[ (y+1) * w + x] = white
            
        else:
            data[ y * w + x ] = white
    im.save("1.gif")

if __name__ == '__main__':
  im = Image.open('input-black.gif')
  print get_left_start_point(im)
  aim = get_left_start_point(im)
  remove_line(im, aim)

