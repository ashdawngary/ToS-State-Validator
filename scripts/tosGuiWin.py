'''
Windows Specific Gui
'''
import tosGui
import pilImageHandler
import cordinateTracker
import metaocr
from Tkinter import *
import ttk
winMaster = Tk()
tosGui.setMasterToLift(winMaster)
winMaster.geometry("1200x700")
winMaster.title('Tos-win32-State visualizer')
actual = True
def extractImage():
    global master
    global actual
    current_screen = pilImageHandler.takeImage(cordinateTracker.getUL(),cordinateTracker.getDR())
    if min(current_screen.size) == 0:
        pilImageHandler.flipToGeneric()
    else:
        if actual:
            pilImageHandler.onImage(current_screen)
        else:
            pilImageHandler.onImage(metaocr.filter(current_screen))
    winMaster.after(70,extractImage)
def flipImageMode(event=None):
    global actual
    actual = not actual
def initKeyBinds(master):
    master.bind("<f>",flipImageMode)
def initWindows(master):
    initKeyBinds(master)
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
extractImage()
tosGui.rePopulate()
tosNotebook.add(monteCarloBase,text="Base Gui")
tosNotebook.add(visionBase,text="OCR Extraction")

winMaster.mainloop()
