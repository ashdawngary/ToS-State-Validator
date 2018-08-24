'''
Windows Specific Gui
'''
import tosGui
import pilImageHandler
import cordinateTracker
from PIL import ImageGrab

from Tkinter import *
master = tosGui.master

def extractImage():
    current_screen = pilImageHandler.extractImage(cordinateTracker.getUL(),cordinateTracker.getDR())
    if min(current_screen.size) == 0:
        pilImageHandler.flipToGeneric()
    else:
        pilImageHandler.onImage(current_screen)
def initWindows(master):
    pilImageHandler.initVision(master)
    cordinateTracker.initTracker(master)




initWindows(master)
tosGui.rePopulate()
master.mainloop()
