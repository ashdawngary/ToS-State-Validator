from Tkinter import *
master = None
def setMasterToLift(r):
    global master
    master = r
def getString(title,Question):
    global master
    f = Tk()
    f.title(title)
    q = Label(f,text=Question)
    r = Entry(f)
    f.lift()
    f.focus()
    q.pack()
    r.pack()
    r.focus()
    f.bind("<Return>",lambda event:f.quit())
    f.geometry("200x100")
    f.mainloop()
    ans =  r.get()
    f.destroy()
    master.lift()
    return ans

def getRole(title,Question):
    a = getString(title,Question)
    try:
        int(a)
        return int(a)
    except:
        return getRole(title,Question)
def getYesNo(title,Question):
    q = getString(title,Question+"\ny/N")
    if q == 'y':
        return True
    elif q == "N":
        return False
    return getYesNo(title,Question)
