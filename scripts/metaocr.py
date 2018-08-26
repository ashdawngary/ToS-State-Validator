'''
meta-ocr pre tessertact attempts to clean up target.
'''
from PIL import Image
from math import sqrt
def filter(realimage):
    newimage = Image.new("RGB", realimage.size, "white") # generate new blank image, white is default background
    # we also want to limit pixels written to, so lets make it default black
    xsz = realimage.size[0]
    ysz = realimage.size[1]
    if(xsz*ysz > 100000):
        print "Image was too big to filter(takes way to long at) ",xsz*ysz,"pixels"
        return realimage
    for xval in range(0,xsz):
        for yval in range(0,ysz):
            if euclidRGB(realimage.getpixel((xval,yval)),(255,255,255)) < 50:
                newimage.putpixel((xval,yval),(0,0,0))
    return newimage
def euclidRGB(fcolor,scolor):
    return sqrt(sum([(fcolor[i]-scolor[i])**2 for i in range(0,len(fcolor))]))
