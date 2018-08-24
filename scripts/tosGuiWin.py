'''
Windows Specific Gui
'''
import tosGui
import pilImageHandler
import cordinateTracker

from Tkinter import *
master = tosGui.master

def extractImage():
    global master
    current_screen = pilImageHandler.takeImage(cordinateTracker.getUL(),cordinateTracker.getDR())
    if min(current_screen.size) == 0:
        pilImageHandler.flipToGeneric()
    else:
        pilImageHandler.onImage(current_screen)
    master.after(70,extractImage)
def initWindows(master):
    pilImageHandler.initVision(master)
    cordinateTracker.initTracker(master)




initWindows(master)
extractImage()
tosGui.rePopulate()
master.mainloop()
