'''
Windows Specific Gui
'''
import tosGui
import pilImageHandler
import cordinateTracker
import metaocr
from Tkinter import *
master = tosGui.master
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
    master.after(70,extractImage)
def flipImageMode(event=None):
    global actual
    actual = not actual
def initKeyBinds(master):
    master.bind("<f>",flipImageMode)
def initWindows(master):
    initKeyBinds(master)
    pilImageHandler.initVision(master)
    cordinateTracker.initTracker(master)




initWindows(master)
extractImage()
tosGui.rePopulate()
master.mainloop()
