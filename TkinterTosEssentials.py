from Tkinter import *
import tosBasher
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
    f.geometry("300x100")
    f.mainloop()
    ans =  r.get()
    f.destroy()
    master.lift()
    return ans
def getTOSRole(title,Question):
    cRole = getString(title,Question)
    while not cRole in tosBasher.roles:
        cRole = getString(title,Question)
    return cRole
def getUserNumber(title,Question):
    a = getString(title,Question)
    try:
        int(a)
        assert int(a) > 0 and int(a) < 16
        return int(a)
    except:
        return getUserNumber(title,Question)
def getYesNo_proto(title,Question):
    ''' defaults to no'''
    global master
    winRoot = Tk()
    winRoot.title(title)
    q = Label(winRoot,text=Question)
    q.place(x=30,y=10)
    resultVar  =StringVar()
    resultVar.set("Answer Here")
    result = Label(winRoot,textvariable = resultVar)
    result.place(x=30,y=30)
    yesButton = Button(winRoot,text = "yes",command = lambda :resultVar.set("YES(Enter to Quit)"))
    noButton = Button(winRoot,text = "NO",command = lambda :resultVar.set("NO(Enter to Quit)"))
    yesButton.place(x=30,y=60)
    noButton.place(x=130,y=60)
    winRoot.bind("<Return>",lambda event:winRoot.quit())
    winRoot.geometry("200x100")
    winRoot.mainloop()
    rf = resultVar.get()
    winRoot.destroy()
    master.lift()
    return "YES" in rf
def getYesNo(title,Question):
    '''
    poorly done version of get Yes no, very hard to actual use.  we will show a better version.
    '''
    q = getString(title,Question+"\ny/N")
    if q == 'y':
        return True
    elif q == "N":
        return False
    return getYesNo(title,Question)
def multiUserQuery(title,Question):
    ''' Query Multiple Roles '''
    ''' Grids CheckButtons in a 3x5 Format '''
    global master
    global checkVals
    winRoot = Tk()
    winRoot.title(title)
    winRoot.geometry("400x200")
    winRoot.bind("<Return>",lambda event:winRoot.quit())
    checkVals = [IntVar() for i in range(0,15)]
    #map(lambda x:x.set(False),checkVals)
    toprow = [Checkbutton(winRoot,text=str(3*i + 1),command=lambda i=i:checkVals[3*i+0].set(not checkVals[3*i+0].get())) for i in range(0,5)]
    midrow = [Checkbutton(winRoot,text=str(3*i + 2),command=lambda i=i:checkVals[3*i+1].set(not checkVals[3*i+1].get())) for i in range(0,5)]
    botrow = [Checkbutton(winRoot,text=str(3*i + 3),command=lambda i=i:checkVals[3*i+2].set(not checkVals[3*i+2].get())) for i in range(0,5)]
    qLabel = Label(winRoot,text=Question)
    qLabel.place(x=30,y=10)
    for i in range(0,5):
        target_y = 30+ 60 * i
        toprow[i].place(y=50,x=target_y)
        midrow[i].place(y=70,x=target_y)
        botrow[i].place(y=90,x=target_y)
    winRoot.mainloop()
    answer =  filter(lambda x:x != -1, list( [i+1 if checkVals[i].get() else -1 for i in range(0,15) ] ) )
    winRoot.destroy()
    return answer
