from Tkinter import *
from TkinterTosEssentials import *
import smartFitter
import sys
cNames = ["Player%s" for i in range(1,16)]
master = Tk()

cValues = [StringVar(master) for i in range(0,15)]
cLabels = [Label(master,textvariable=cValues[i]) for i in range(0,15)]
for i in range(0,len(cLabels)):
    cLabels[i].place(x=120,y=50+(30*i))
nH = []
master.geometry("800x600")

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


def oninvest():
    targetidx = getRole("Investigative","User Number")
    if targetidx == None:
        return
    targetRole = getString("Investigative","Role")
    while not targetRole in tosCore.roles:
        targetRole = getString("Investigative","Role",parent=master)
    smartFitter.player_oninvest(targetidx,targetRole)

def onDeath():
    targetidx = getRole("Dead","User Number",parent=master,minvalue=1,maxvalue=15)
    contradiction = getYesNo("Fishy","Was there a clear contradiction?")
    cleaned = getYesNo("Cleaned","was this user cleaned?")
    if cleaned:
        smartFitter.confirmed_deathClean(targetidx)
        return
    targetRole = getString("Dead","Role",parent=master)
    while not targetRole in tosCore.roles:
        targetRole = getString("Dead","Role",parent=master)
    if contradiction:
        smartFitter.confirmed_sure(targetidx,"disg")
    elif targetRole == "GF":
        smartFitter.confirmed_deathGF(targetidx,targetRole)
    elif targetRole == "MAFIOSO":
        smartFitter.confirmed_deathMafioso(targetidx,targetRole)
    else:
        smartFitter.confirmed_death(targetidx)
def setNK():
    targetRole = getString("Define NK","Role",parent=master)
    if targetRole == None or not targetRole in ["ww","arso","sk"]:
        return
    smartFitter.setNK(targetRole)
def setNE():
    targetRole = getString("Define NE","Role",parent=master)
    if targetRole == None or not targetRole in ["witch","exe","jester"]:
        return
    smartFitter.setNE(targetRole)

oninvestigative = Button(text = "Invest Results",command = oninvest)
oninvestigative = Button(text = "Death Results",command = onDeath)
oninvestigative = Button(text = "set NK",command = oninvest)
oninvestigative = Button(text = "set NE",command = oninvest)

rePopulate()
master.mainloop()
