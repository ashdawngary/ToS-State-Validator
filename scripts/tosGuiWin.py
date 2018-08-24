'''
Windows Specific Gui
'''
import tosGui
import win32api,win32con # Windows libraries for interfacing with OS
from PIL import ImageGrab
from Tkinter import *
master = tosGui.master
cMouseCords = None
def initWindows(master):
    print master
    global cMouseCords
    cMouseCords = Label(master,text = "Is this mouse position working?")
    cMouseCords.place(x=10,y=600)
def mouseUpdate():
    cc = getcords()
    cMouseCords['text'] = "X: %s Y: %s"%(cc[0],cc[1])
    master.after(20,mouseUpdate)
def getcords():
    return win32api.GetCursorPos()
def getPixelatmouse():
    im = ImageGrab.grab()
    return im.getpixel(getcords())
initWindows(master)
tosGui.rePopulate()
mouseUpdate()
master.mainloop()
