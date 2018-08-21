from Tkinter import *
from TkinterTosEssentials import *
import smartFitter
import sys
cNames = ["Player%s" for i in range(1,16)]
master = Tk()
setMasterToLift(master)
cValues = [StringVar(master) for i in range(0,15)]
cLabels = [Label(master,textvariable=cValues[i]) for i in range(0,15)]
for i in range(0,len(cLabels)):
    cLabels[i].place(x=120,y=50+(30*i))
nH = []
master.geometry("900x700")

for i in range(0,15):
    name= getString("General","Name of %s"%(i+1))
    nH.append(Label(master,text="%s(%s)"%(name,i+1)))
    nH[-1].place(x=5,y=50+30*i)
psudotypes = list(smartFitter.types)
psudotypes.pop(8)
headerLabel = Label(master,text=' '.join(map(lambda x: x.ljust(7),psudotypes)))
headerLabel.place(x=120,y=10)
tosCore = sys.modules["tosBasher"]
def rePopulate():
    smartFitter.project()
    for i in range(0,15):
        cValues[i].set(smartFitter.topr[i])
    master.after(250,rePopulate)

def oninvest():
    targetidx = getRole("Investigative","User Number")
    if targetidx == None:
        return
    targetRole = getString("Investigative","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("Investigative","Role")
    smartFitter.player_oninvest(targetidx,targetRole)
def usrClaim():
    targetidx = getRole("usr claim","User Number")
    targetRole = getString("usr claim","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("usr claim","Role")
    smartFitter.player_onclaim(targetidx,targetRole)
def confirmIt():
    targetidx = getRole("Confirmed","User Number")
    targetRole = getString("Confirmed","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("Confirmed","Role")
    smartFitter.confirmed_sure(targetidx,targetRole)
def onDeath():
    targetidx = getRole("Dead","User Number")
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
    smartFitter.rst()
    master.after(50,smartFitter.fitClaims)
    master.after(150,smartFitter.fitClaims)
    master.after(250,smartFitter.fitClaims)
    master.after(350,smartFitter.fitClaims)
    master.after(450,smartFitter.fitClaims)
    master.after(550,smartFitter.fitClaims)
    master.after(650,smartFitter.fitClaims)
    master.after(750,smartFitter.fitClaims)
    master.after(850,smartFitter.fitClaims)
    master.after(950,smartFitter.fitClaims)
    master.after(1050,smartFitter.fitClaims)
def getSpyDetails():
    usr = getRole("Spy","User Number")
    smartFitter.mv(usr)
def getSheriffDetails():
    usr = getRole("Sheriff","User Number")
    if getYesNo("Sheriff","Inno?"):
        smartFitter.confirmed_isInno(usr)
    else:
        smartFitter.confirmed_isMafia(usr)
def visitRole():
    usr = getRole("LO visit Results","Number")
    smartFitter.applyvisiting(usr)
oninvestigative = Button(text = "Invest Results",command = oninvest)
onDeath = Button(text = "Death Results",command = onDeath)
onNK = Button(text = "set NK",command = setNK)
onNE = Button(text = "set NE",command = setNE)
onReclaulate = Button(text = "Update Monte Carlo",command=prepReupdate)
onSpy = Button(text="Spy Detail Update",command=getSpyDetails)
onSheriff = Button(text="Sheriff Detail Update",command=getSheriffDetails)
onConfirmed = Button(text = "confirm someone",command = confirmIt)
onVFRClaim = Button(text = "user claim",command=usrClaim)
onVisitng  = Button(text = "visitng Role", command=visitRole)
oninvestigative.place(x=600,y=0)
onReclaulate.place(x=700,y=0)
onSpy.place(x=700,y=50)
onSheriff.place(x=700,y=100)
onConfirmed.place(x=700,y=150)
onDeath.place(x=600,y=50)
onVFRClaim.place(x=700,y=200)
onNK.place(x=600,y=100)
onNE.place(x=600,y=150)
rePopulate()
master.mainloop()
