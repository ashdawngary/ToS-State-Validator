import sys
assert int(sys.version[0]) ==   2,"must be running python 2 running python %s"%(sys.version[0])
from Tkinter import *
from TkinterTosEssentials import *
import smartFitter
import contingencyBox
nH = None
cValues = None
contingencyFrame = None
master = Tk()
setMasterToLift(master)
master.geometry("1200x700")

def resetName(id):
    global NH
    name= getString("General","Name of %s"%(id+1))
    nH[id]['text'] = "%s(%s)"%(name,id+1)

tosCore = sys.modules["tosBasher"]
def rePopulate():
    global cValues
    # use smartFitter.cmatr
    for i in range(0,len(smartFitter.cmatr)):
        r = list(smartFitter.cmatr[i])
        r.pop(8)
        q = max(sum(r),1)
        r = map(lambda x: x/float(q), r)
        for role in range(0,10):
            cValues[i][role].set(str(round(r[role]*100,2)).ljust(5)+"%")
    master.after(250,rePopulate)

def oninvest():
    targetidx = getUserNumber("Investigative","User Number")
    if targetidx == None:
        return
    targetRole = getString("Investigative","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("Investigative","Role")
    smartFitter.player_oninvest(targetidx,targetRole)
def usrClaim():
    targetidx = getUserNumber("usr claim","User Number")
    targetRole = getString("usr claim","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("usr claim","Role")
    smartFitter.player_onclaim(targetidx,targetRole)
def confirmIt():
    targetidx = getUserNumber("Confirmed","User Number")
    targetRole = getString("Confirmed","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("Confirmed","Role")
    smartFitter.confirmed_sure(targetidx,targetRole)
def onDeath():
    targetidx = getUserNumber("Dead","User Number")
    contradiction = getYesNo("Fishy","Was there a clear contradiction?")
    cleaned = getYesNo("Cleaned","was this user cleaned?")
    if cleaned:
        smartFitter.confirmed_deathClean(targetidx)
        return
    targetRole = getString("Dead","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("Dead","Role")
    if contradiction:
        smartFitter.confirmed_sure(targetidx,"disg")
    elif targetRole == "GF":
        smartFitter.confirmed_deathGF(targetidx)
    elif targetRole == "MAFIOSO":
        smartFitter.confirmed_deathMafioso(targetidx)
    elif not contradiction:
        smartFitter.confirmed_sure(targetidx,targetRole)
def setNK():
    targetRole = getString("Define NK","Role")
    if targetRole == None or not targetRole in ["ww","arso","sk"]:
        return
    smartFitter.setNK(targetRole)
def setNE():
    targetRole = getString("Define NE","Role")
    if targetRole == None or not targetRole in ["witch","exe","jester"]:
        return
    smartFitter.setNE(targetRole)
def prepReupdate():
    master.after(10,async_fitClaims)
def async_fitClaims():
    TPR  =[]
    TSR =[]
    TIR = []
    TKR = []
    RMR = []
    q = filter(lambda x: x in tosCore.roles,contingencyBox.loadContingencies())
    print "Revised: ",q
    for i in q:
        id = tosCore.get(i)
        if id in smartFitter.TP:
            TPR.append(id)
        elif id in smartFitter.TK:
            TKR.append(id)
        elif id in smartFitter.RM:
            RMR.append(id)
        elif id in smartFitter.TI:
            TIR.append(id)
        elif id in smartFitter.TS:
            TSR.append(id)
        else:
            print "couldnt find",id,tosCore.roles[id]

    print "Initalizing FitClaims"
    smartFitter.rst()
    for i in range(0,20):
        smartFitter.fitClaims(RmReqs= RMR,TPReqs=TPR,TSReqs = TSR,TIReqs = TIR,TkReqs = TKR,usize = 10000)
    print "FINISHED FITCLAIMING"
def getSpyDetails():
    usr = getUserNumber("Spy","User Number")
    smartFitter.mv(usr)
def getSheriffDetails():
    usr = getUserNumber("Sheriff","User Number")
    if getYesNo("Sheriff","Inno?"):
        smartFitter.confirmed_isInno(usr)
    else:
        smartFitter.confirmed_isMafia(usr)
def visitRole():
    usr = getUserNumber("LO visit Results","Number")
    smartFitter.applyvisiting(usr)
def onlyClaim():
    onlyClaimRole = getTOSRole("Only Claim","What was the Role?(Dont use if there is Janitor)")
    roleList = multiUserQuery("Only Claim","Click all Users who claimed this role.")
    print onlyClaimRole," has %s claimers."%(len(roleList))
    for i in range(1,16):
        if i in onlyClaim:
            smartFitter.player_onclaim(i,onlyClaimRole)
        else:
            smartFitter.player_roleRemove(i,onlyClaimRole)

def initSpecialResults(master):
    global resFrame
    resFrame = Frame(master,width=400,height=100)
    onSpy =           Button(resFrame,text="Spy Detail Update",command=getSpyDetails)
    onSheriff =       Button(resFrame,text="Sheriff Detail Update",command=getSheriffDetails)
    oninvestigative = Button(resFrame,text = "Invest Results",command = oninvest)
    onVisitng  =      Button(resFrame,text = "LO visitng Role", command=visitRole)
    onSpy.place(x=0,y=0)
    onSheriff.place(x=150,y=0)
    oninvestigative.place(x=300,y=0)
    onVisitng.place(x=150,y=30)
    resFrame.place(x=700,y=500)
def loadNames(master):
    global nH
    GenericName = "Chumps"
    nH = []
    for i in range(0,15):
        if GenericName == "":
            name= getString("General","Name of %s"%(i+1))
        else:
            name = GenericName
        nH.append(Label(master,text="%s(%s)"%(name,i+1)))
        nH[-1].place(x=5,y=50+30*i)
        nH[-1].bind("<Button-1>",lambda event,ix=i:resetName(ix))
def loadEvilSetters(master):
    evilFrame = Frame(master,width=100,height=100)
    onNK =            Button(evilFrame,text = "set NK",command = setNK)
    onNE =            Button(evilFrame,text = "set NE",command = setNE)
    evilFrame.place(x=800,y=100)
    onNK.place(x=0,y=0)
    onNE.place(x=0,y=50)
def loadPlayerClaims(master):
    playerFrame =Frame(master,width=200,height=300)
    onConfirmed =     Button(playerFrame,text = "confirm someone",command = confirmIt)
    onVFRClaim =      Button(playerFrame,text = "user claim",command=usrClaim)
    onlyClaimB =       Button(playerFrame,text = "OnlyClaim",command=onlyClaim)
    playerFrame.place(x=900,y=0)
    onlyClaimB.place(x=0,y=250)
    onConfirmed.place(x=0,y=150)
    onVFRClaim.place(x=0,y=200)

def initBase(master):
    global cValues,nH
    global mustBeList
    contingencyBox.initContingency(master)
    loadNames(master)
    psudotypes = list(smartFitter.types)
    psudotypes.pop(8)
    headerLabel = Label(master,text=' '.join(map(lambda x: x.ljust(7),psudotypes)))
    headerLabel.place(x=120,y=10)
    cValues = [[StringVar(master) for j in range(0,10)] for i in range(0,15)]
    cLabels = [[Label(master,textvariable=cValues[i][j]) for j in range(0,10)] for i in range(0,15)]
    for i in range(0,len(cLabels)):
        for j in range(0,10):
            cLabels[i][j].place(x=120+60*(j),y=50+(30*i))
    initSpecialResults(master)
    loadEvilSetters(master)
    loadPlayerClaims(master)
    onDeathB =         Button(master,text = "Death Results",command = onDeath)
    onReclaulate =    Button(master,text = "Update Monte Carlo",command=prepReupdate)

    onReclaulate.place(x=900,y=0)

    onDeathB.place(x=800,y=50)

initBase(master)
if __name__ == "__main__":
    rePopulate()
    master.mainloop()
# we can run windows specific commands now.
