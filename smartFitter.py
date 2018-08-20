import tosBasher
import random
import math
cPlayers = [tosBasher.CurrentPerson() for i in range(0,15)]
'''
define our constants
'''
RM = [0,1,2,3,4,6,7]
mafioso = 8
godfather = 5
TK = [22,21]
TP = [9,10]
TS = [11,15,16,17,20]
TI = [12,18,19,14]
jailor = 13
NK = [26,27,28]
NE = [24,25,23]
EXPLNK = NK
EXPLNE = NE
def setNK(role):
    global EXPLNK
    eid = tosBasher.get(role)
    print "operating under assumption of %s (%s) NK"%(role,eid)
    EXPLNK = eid
    print 'Please refresh'
def setNE(role):
    global EXPLNE
    eid = tosBasher.get(role)
    print "operating under assumption of %s (%s) NE"%(role,eid)
    EXPLNE = eid
    print 'Please refresh'
def mv(idx):
    cPlayers[idx-1].mafvisit=True
    cPlayers[idx-1].mafiavisited()
def applyvisiting(idx):
    cPlayers[idx-1].applyvisiting()
def confirmed_sure(idx,role):
    cPlayers[idx-1].confirmedSelf(tosBasher.get(role))
def confirmed_death(idx,role):
    cPlayers[idx-1].confirmedDeath(tosBasher.get(role))
def confirmed_deathGF(idx,role):
    cPlayers[idx-1].confirmedDeathGF()
def confirmed_deathMafioso(idx,role):
    cPlayers[idx-1].confirmedDeathMafioso()
def confirmed_deathClean(idx):
    cPlayers[idx-1].mafiaVisited()
def confirmed_jailorexe(idx,role):
    cPlayers[idx-1].confirmedDeathJailorExe(tosBasher.get(role))
def accuse_jestClaim(idx,role):
    cPlayers[idx-1].jesteryClaim(tosBasher.get(role))
def player_onclaim(idx,role):
    cPlayers[idx-1].onClaim(tosBasher.get(role))
def player_oninvest(idx,role):
    cPlayers[idx-1].onInvestResults(tosBasher.get(role))
def confirmed_isMafia(idx):
    cPlayers[idx-1].isMafia()
def player_getcatagories(idx):
    proto_possible = set([])
    for i in NE:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("NE")
    for i in NK:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("NK")
    for i in RM:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("RM")
    for i in TS:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("TS")
    for i in TI:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("TI")
    for i in TP:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("TP")
    for i in TK:
        if cPlayers[idx-1].possible[i]:
            proto_possible.add("TK")
    if cPlayers[idx-1].possible[mafioso]:
        proto_possible.add("MAFIOSO")
    if cPlayers[idx-1].possible[godfather]:
        proto_possible.add("GF")
    if cPlayers[idx-1].possible[jailor]:
        proto_possible.add("Jailor")
    return list(proto_possible)
pieces = [None for i in range(0,15)]
def queryList(cidx):
    cRes = pieces[cidx-1]
    if cRes == None:
        # update cRes
        #print 'q'+str(cidx)
        pieces[cidx-1] = player_getcatagories(cidx)
    return pieces[cidx-1]
def clearList():
    global pieces
    pieces = [None for i in range(0,15)]
cVal = [0 for i in range(0,15)]
numPushedStates = 0
def setState(idx,type):
    cVal[idx-1] = types.index(type)

def push():
    global numPushedStates
    if numPushedStates % 100000 == 0:
        print numPushedStates
    #print "Pushed State!",numPushedStates+1
    numPushedStates += 1
    for i in range(0,15):
        cmatr[i][cVal[i]] += 1

cFit = [2,1,1,1,1,1,1,2,3,1,1]
types= ["RM","MAFIOSO","GF","TP","TK","TS","Jailor","TI","RT","NK","NE"]
cmatr = [[0]*len(types) for i in range(0,15)]
adjacent = {}
def project():
    for i in cmatr:
        print i
def rst():
    global cmatr
    cmatr = [[0]*len(types) for i in range(0,15)]
def fitClaims():
    clearList()
    for i in range(0,15):
        queryList(i)
    prks = [[i,len(pieces[i])+random.random()*0.05] for i in range(0,15)]
    prks.sort(key = lambda a:a[1])
    cTime = 1
    for v in prks:
        cTime *= v[1]
    print cTime
    print prks
    print "TenPower: "+str(math.log(cTime)/math.log(10))
     # now we can intialize our basher
    startlist = list(cFit)
    for i in range(0,len(prks)-1):
        adjacent[prks[i][0] + 1] = prks[i+1][0] + 1
    adjacent[prks[len(prks)-1][0] + 1] = 16

    for i in range(0,100000):
        update(startlist,prks[0][0]+1)

def update(clist,idx):
    #print idx
    if idx == 16:
        #print "Found Solution"
        push()
        return True
    checkwise = list(queryList(idx))
    random.shuffle(checkwise)
    while checkwise != []:
        next = checkwise.pop(0)
        if next == "RM" and clist[0] > 0:
            for rMaf in RM:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[0] -= 1
                    setState(idx,"RM")
                    q = update(clist,adjacent[idx])
                    clist[0] += 1
                    if q == True:
                        return True
        elif next == "MAFIOSO" and clist[1] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("mafioso")]:
                clist[1] -= 1
                setState(idx,"MAFIOSO")
                q = update(clist,adjacent[idx])
                clist[1] += 1
                if q == True:
                    return True
        elif next == "GF" and clist[2] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("gf")]:
                clist[2] -= 1
                setState(idx,"GF")
                q = update(clist,adjacent[idx])
                clist[2] += 1
                if q == True:
                    return True
        elif next == "TP" and clist[3] > 0:
            for rMaf in TP:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[3] -= 1
                    setState(idx,"TP")
                    q = update(clist,adjacent[idx])
                    clist[3] += 1
                    if q == True:
                        return True
        elif next == "TP" and clist[8] > 0:
            for rMaf in TP:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[8] -= 1
                    setState(idx,"RT")
                    q = update(clist,adjacent[idx])
                    clist[8] += 1
                    if q == True:
                        return True
        elif next == "TK" and clist[4] > 0:
            for rMaf in TK:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[4] -= 1
                    setState(idx,"TK")
                    q = update(clist,adjacent[idx])
                    clist[4] += 1
                    if q == True:
                        return True
        elif next == "TK" and clist[8] > 0:
            for rMaf in TK:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[8] -= 1
                    setState(idx,"RT")
                    q = update(clist,adjacent[idx])
                    clist[8] += 1
                    if q == True:
                        return True
        elif next == "TS" and clist[5] > 0:
            for rMaf in TS:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[5] -= 1
                    setState(idx,"TS")
                    q = update(clist,adjacent[idx])
                    clist[5] += 1
                    if q == True:
                        return True
        elif next == "TS" and clist[8] > 0:
            for rMaf in TS:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[8] -= 1
                    setState(idx,"RT")
                    q = update(clist,adjacent[idx])
                    clist[8] += 1
                    if q == True:
                        return True
        elif next == "Jailor" and clist[6] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("jailor")]:
                clist[6] -= 1
                setState(idx,"Jailor")
                q = update(clist,adjacent[idx])
                clist[6] += 1
                if q == True:
                    return True
        elif next == "TI" and clist[7] > 0:
            for rMaf in TI:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[7] -= 1
                    setState(idx,"TI")
                    q = update(clist,adjacent[idx])
                    clist[7] += 1
                    if q == True:
                        return True
        elif next == "TI" and clist[8] > 0:
            for rMaf in TI:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[8] -= 1
                    setState(idx,"RT")
                    q = update(clist,adjacent[idx])
                    clist[8] += 1
                    if q == True:
                        return True
        elif next == "NK" and clist[9] > 0:
            for rMaf in NK:
                if cPlayers[idx-1].possible[rMaf] and rMaf in EXPLNK:
                    clist[9] -= 1
                    setState(idx,"NK")
                    q = update(clist,adjacent[idx])
                    clist[9] += 1
                    if q == True:
                        return True
        elif next == "NE" and clist[10] > 0:
            for rMaf in NE:
                if cPlayers[idx-1].possible[rMaf] and rMaf in EXPLNE:
                    clist[10] -= 1
                    setState(idx,"NE")
                    q = update(clist,adjacent[idx])
                    clist[10] += 1
                    if q == True:
                        return True
#    if adjacent[idx] == 16:
#        print "Ran out of options: ",idx,adjacent[idx],clist,queryList(idx),"didnt fit last min"
#    else:
#        print "Ran out of options: ",idx,adjacent[idx],clist,queryList(idx)
#    return False
