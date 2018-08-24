from Tkinter import *
from TkinterTosEssentials import *
mustBeList = []
def loadContingencies():
    cont_roles = mustBeList.get(0,END)
    return list(cont_roles)
def initContingency(master):
    global contingencyFrame
    global mustBeList
    contingencyFrame = Frame(master,width=300,height=200)
    addCont =         Button(contingencyFrame,text = "Add Role Contingency",command=addRoleContingency)
    delCont =         Button(contingencyFrame,text = "Del Role Contingency",command=delRoleContingency)
    mustBeList =      Listbox(contingencyFrame)
    mustBeList.place(x=0,y=0)
    addCont.place(x=150,y=10)
    delCont.place(x=150,y=50)
    contingencyFrame.place(x=800,y=300)

def addRoleContingency():
    global mustBeList
    role = getTOSRole("Contingency","Role Must Exist: ")
    mustBeList.insert(END,role)
def delRoleContingency():
    global mustBeList
    mustBeList.delete(ANCHOR)
