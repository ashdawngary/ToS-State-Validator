'''
ocr image graber, interfaced into tkinter.
use pageflipping to rapidly display images.
'''
from Tkinter import *
from PIL import Image,ImageTk
currentLoader = None
currentLabel = None

class PageFlipperImageDisplayer:
    def __init__(self,predef,labelInstance):
        '''
        predef is the PIL Image Generic Background image thing.
        '''
        self.cLabelInstance = labelInstance
        self.page1 = ImageTk.PhotoImage(predef)
        self.page2 = ImageTk.PhotoImage(predef)
        self.p1write = False
        self.p2write = False
        self.modewrite = False
        self.newest = None
        self.cLabelInstance.config(image=self.page1)
    def write(self,newim):
        if self.modewrite and not self.p1write:
            # write page 1
            self.modewrite = not self.modewrite
            self.p1write = True
            self.page1 = ImageTk.PhotoImage(newim)
            self.p1write = False
            self.cLabelInstance.config(image=self.page1)
            self.newest = newim
        elif not self.modewrite and not self.p2write:
            self.modewrite = not self.modewrite
            self.p1write = True
            self.page2 = ImageTk.PhotoImage(newim)
            self.p2write = False
            self.cLabelInstance.config(image=self.page1)
            self.newest = newim
    def queryNewestImage(self):
        return self.newest
def getAsset(asset):
    f = __file__.split("\\")
    f = f[:-2]
    f = '\\'.join(f)+"\\assets\\%s"%(asset)
    print "Querying: ",f
    return Image.open(f)
def takeImage(c1,c2):
    left = min(c1[0],c2[0])
    right =  max(c1[0],c2[0])
    up = min(c1[1],c2[1])
    down =  max(c1[1],c2[1])
    return ImageGrab.grab(bbox=(left,up,right,down))
def initVision(master):
    global currentLoader,currentLabel
    currentLabel = Label(master)
    currentLabel.place(x=300,y=550)
    currentLoader = PageFlipperImageDisplayer(getAsset("placeholder_buffer.gif"),currentLabel)
    currentLoader.write(getAsset("placeholder_buffer.gif"))
