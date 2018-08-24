from Tkinter import *
import win32api,win32con # Windows libraries for interfacing with OS

LeftCorner = [0,0]
RightCorner = [0,0]
master = None
LeftCornerLabel = None
RightCornerLabel = None
update_left = False
update_right = False
cMouseCords = None
def getcords():
    return win32api.GetCursorPos()
def getUL():
    return LeftCorner
def getDR():
    return RightCorner
def configureKeyBinds():
    master.bind("<Escape>",terminateCorner)
def terminateCorner(event=None):
    global update_left,update_right
    update_left = False
    update_right = False
    LeftCornerLabel['text'] = 'UL: %s %s'%(LeftCorner[0],LeftCorner[1])
    RightCornerLabel['text'] = "DR: %s %s"%(RightCorner[0],RightCorner[1])
def onLeftUpdate():
    global LeftCornerLabel, LeftCorner
    if not update_left:
        terminateCorner()
        return
    LeftCorner = list(getcords())
    LeftCornerLabel['text'] = 'Upper-Left-Corner: %s %s'%(LeftCorner[0],LeftCorner[1])
    master.after(50,onLeftUpdate)
def onRightUpdate():
    if not update_right:
        terminateCorner()
        return
    global RightCornerLabel,RightCorner
    RightCorner = list(getcords())
    RightCornerLabel['text'] = "Down-Right-Corner: %s %s"%(RightCorner[0],RightCorner[1])
    master.after(50,onRightUpdate)
def mouseUpdate():
    cc = getcords()
    cMouseCords['text'] = "X: %s Y: %s"%(cc[0],cc[1])
    master.after(20,mouseUpdate)
def editLeft(event=None):
    global update_left
    update_left = True
    onLeftUpdate()

def editRight(event=None):
    global update_right
    update_right = True
    onRightUpdate()

def initTracker(recMaster):
    global master
    global cMouseCords
    global LeftCornerLabel
    global RightCornerLabel
    master = recMaster
    configureKeyBinds()
    cMouseCords = Label(master,text = "Is this mouse position working?")
    LeftCornerLabel = Label(master,text='UL: %s %s'%(LeftCorner[0],LeftCorner[1]))
    RightCornerLabel = Label(master,text="DR: %s %s"%(RightCorner[0],RightCorner[1]))
    LeftCornerLabel.bind("<Button-1>",editLeft)
    RightCornerLabel.bind("<Button-1>",editRight)
    cMouseCords.place(x=10,y=600)
    LeftCornerLabel.place(x=10,y=560)
    RightCornerLabel.place(x=10,y=580)
    mouseUpdate()
