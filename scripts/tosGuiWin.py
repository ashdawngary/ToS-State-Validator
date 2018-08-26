'''
Windows Specific Gui
'''
import tosGui
import pilImageHandler
import cordinateTracker
import metaocr
from Tkinter import *
import ttk
from PIL import  ImageChops
winMaster = Tk()
tosGui.setMasterToLift(winMaster)
winMaster.geometry("1200x700")
winMaster.title('Tos-win32-State visualizer')
actual = True
prevImage = None
def equal(im1, im2):
    if im1 == None or im2 == None:
        return False
    if im1.size != im2.size:
        return False
    return ImageChops.difference(im1, im2).getbbox() is None
def extractImage():
    global master
    global actual
    global prevImage
    current_screen = pilImageHandler.takeImage(cordinateTracker.getUL(),cordinateTracker.getDR())
    #if prevImage == None:
    #    print "havenone"
    #else:
#        print current_screen.size,prevImage.size,equal(current_screen,prevImage)
    if min(current_screen.size) == 0:
        pilImageHandler.flipToGeneric()
    elif equal(current_screen,prevImage):
        pilImageHandler.setInactive()
        #pilImageHandler.onImage(current_screen,ocr=False)
    else:
        pilImageHandler.setActive()
        if actual:
            pilImageHandler.onImage(current_screen,ocr=False)
        else:
            pilImageHandler.onImage(metaocr.filter(current_screen),ocr=True)
    prevImage = current_screen
    winMaster.after(70,extractImage)
def flipImageMode(event=None):
    global actual
    actual = not actual
    print "flipped image mode, now %s"%(actual)
def initKeyBinds(master):
    cordinateTracker.initKeyBinds(master)
    master.bind("<f>",flipImageMode)
def initWindows(master):
    pilImageHandler.initVision(master)
    cordinateTracker.initTracker(master)


'''
Initalize The Notebook System.
'''
tosNotebook = ttk.Notebook(winMaster)
tosNotebook.pack(expand=True,fill='both')
monteCarloBase = Frame(tosNotebook)
visionBase = Frame(tosNotebook)

tosGui.initBase(monteCarloBase)
initWindows(visionBase)
initKeyBinds(winMaster)
extractImage()
tosGui.rePopulate()
tosNotebook.add(monteCarloBase,text="Base Gui")
tosNotebook.add(visionBase,text="OCR Extraction")

winMaster.mainloop()
