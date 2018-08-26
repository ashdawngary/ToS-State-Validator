'''
ocr image graber, interfaced into tkinter.
use pageflipping to rapidly display images.
'''
import ocrReader
from Tkinter import *
from PIL import Image,ImageTk,ImageGrab
import time
currentLoader = None
currentLabel = None
genericBackgroundAsset = None
statusLabel = None
ocrLabel = None
timeLabel = None
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
            self.p1write = True
            self.page1 = ImageTk.PhotoImage(newim)
            self.p1write = False
            self.cLabelInstance.config(image=self.page1)
            self.newest = newim
            self.modewrite = not self.modewrite
        elif not self.modewrite and not self.p2write:
            self.p2write = True
            self.page2 = ImageTk.PhotoImage(newim)
            self.p2write = False
            self.cLabelInstance.config(image=self.page2)
            self.newest = newim
            self.modewrite = not self.modewrite
        #print 'trashed',self.modewrite,self.p1write,self.p2write
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
    global currentLoader
    global currentLabel
    global genericBackgroundAsset
    global statusLabel
    global ocrLabel
    global timeLabel
    genericBackgroundAsset = getAsset("placeholder_buffer.gif")
    currentLabel = Label(master)
    currentLabel.place(x=300,y=30)
    statusLabel = Label(master)
    statusLabel.place(x=300,y=10)
    statusLabel.config(fg='red')
    statusLabel['text'] = "not active"
    ocrLabel = Label(master)
    ocrLabel.place(x=10,y=500)
    ocrLabel['text'] = "no data supplied."
    timeLabel = Label(master)
    timeLabel.place(x=700,y=500)
    timeLabel['text'] = "waiting for data"
    currentLoader = PageFlipperImageDisplayer(genericBackgroundAsset,currentLabel)
    currentLoader.write(genericBackgroundAsset)
def setActive():
    global statusLabel
    statusLabel.config(fg='green')
    statusLabel['text'] = "computing..."
def setInactive():
    global statusLabel
    statusLabel.config(fg='red')
    statusLabel['text'] = "not active"

def flipToGeneric():
    # Flips image to generic
    global currentLoader
    global genericBackgroundAsset
    currentLoader.write(genericBackgroundAsset)
def onImage(cimg,ocr=False):
    #print "Writing on Image"
    # do OCR stuff
    global currentLoader
    currentLoader.write(cimg)
    if ocr:
        updateOCR(cimg)
    #filter by white idk?
def updateOCR(cim):
    global ocrLabel
    global timeLabel
    startTime = time.time()
    ocrLabel['text'] = ocrReader.readImage(cim)
    timeLabel['text'] = "Tesseract Read Time: %s"%(round(time.time()-startTime,2))
