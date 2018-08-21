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
    EXPLNK = [eid]
    print 'Please refresh'
def setNE(role):
    global EXPLNE
    eid = tosBasher.get(role)
    print "operating under assumption of %s (%s) NE"%(role,eid)
    EXPLNE = [eid]
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
def confirmed_deathGF(idx):
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
def confirmed_isInno(idx):
    cPlayers[idx-1].isInno()
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
def checkBit(val,c):
    if not c in val:
        return False
    return val[c]
def enableBit(val,c):
    q = dict(val)
    if c in q:
        q[c] = True
    return q
cFit = [2,1,1,1,1,1,1,2,3,1,1]
types= ["RM","MAFIOSO","GF","TP","TK","TS","Jailor","TI","RT","NK","NE"]
cmatr = [[0]*len(types) for i in range(0,15)]
adjacent = {}
topr = [None for i in range(0,15)]
def fmt(n):
    f =  "%s%%"%(str(100*round(n,4)))
    return f.ljust(7)
def project():
    psudotypes = list(types)
    psudotypes.pop(8) # no rt header
    #print ' '.join(map(lambda x: x.ljust(7),psudotypes))
    k = 0
    for i in cmatr:
        q = list(i)
        q.pop(8)
        s = max(sum(q),1)
        for i in range(0,len(q)):
            q[i] /= float(s)
        topr[k] = ' '.join(map(fmt,q))
        k += 1
    #print "Operating on NE as : %s"%(', '.join(map(lambda x: tosBasher.roles[x],EXPLNE)))
    #print "Operating on NK as : %s"%(', '.join(map(lambda x: tosBasher.roles[x],EXPLNK)))
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
    alreadyHave = {tosBasher.get("vet"):False,tosBasher.get("ret"):False,tosBasher.get("mayor"):False} # vet is unique role, same as retri
    RmReqs = [tosBasher.get("forger")]
    TPReqs = [tosBasher.get("bg")]
    TSReqs = [tosBasher.get("trans"),tosBasher.get("trans"),tosBasher.get("escort")]
    TIReqs = []
    TkReqs = [tosBasher.get("vet")]
    for i in range(0,1):
        update(startlist,prks[0][0]+1,alreadyHave,RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)

def update(clist,idx,alreadyHave,RmReqs,TPReqs,TSReqs,TIReqs,TkReqs):
    #print idx
    if idx == 16:
        #print "Found Solution"
        push()
        return True
    checkwise = list(queryList(idx))
    random.shuffle(checkwise)
    print idx,clist,alreadyHave,checkwise

    while checkwise != []:
        next = checkwise.pop(0)
        if next == "RM" and clist[0] > 0:
            # First we need to checkwether number of RM slots left is greater lessthan or equal to RmReqs
            if clist[0] > len(RmReqs):
                for rMaf in RM:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        Required = rMaf in RmReqs
                        if Required:
                            RmReqs.remove(rMaf)
                        clist[0] -= 1
                        setState(idx,"RM")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[0] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]," random MAFIA"
                            return True
                        if Required:
                            RmReqs.append(rMaf)
            elif clist[0] == len(RmReqs):
                copy_RmReqs = list(RmReqs)
                for rMaf in copy_RmReqs:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        Required = rMaf in RmReqs
                        RmReqs.remove(rMaf)
                        clist[0] -= 1
                        setState(idx,"RM")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[0] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]," random MAFIA"
                            return True
                        if Required:
                            RmReqs.append(rMaf)
            else:
                print "More RM Claims than Slots :L"
            #Done!
        elif next == "MAFIOSO" and clist[1] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("mafioso")]:
                clist[1] -= 1
                setState(idx,"MAFIOSO")
                q = update(clist,adjacent[idx],alreadyHave,RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                clist[1] += 1
                if q == True:
                    print idx,"was mafisoso"
                    return True
        elif next == "GF" and clist[2] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("gf")]:
                clist[2] -= 1
                setState(idx,"GF")
                q = update(clist,adjacent[idx],alreadyHave,RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                clist[2] += 1
                if q == True:
                    print idx,"was","gf"
                    return True
        elif next == "TP" and clist[3] > 0:
            if TPReqs != []:
                copy_TP = list(TPReqs)
                for rMaf in copy_TP:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[3] -= 1
                        TPReqs.remove(rMaf)
                        setState(idx,"TP")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[3] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TPReqs.append(rMaf)
            else:
                for rMaf in TP:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[3] -= 1
                        setState(idx,"TP")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[3] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
        elif next == "TP" and clist[8] > 0:
            if len(TPReqs) != 0:
                copy_TP = list(TPReqs)
                for rMaf in copy_TP:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[8] -= 1
                        TPReqs.remove(rMaf)
                        setState(idx,"TP")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TPReqs.append(rMaf)
            elif len(TSReqs) == 0 and len(TkReqs) == 0 and len(TIReqs) == 0: # underassumption Tp Reqs is already empty
                for rMaf in TP:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[8] -= 1
                        setState(idx,"TP")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
        elif next == "TK" and clist[4] > 0:
            if len(TkReqs) != 0:
                copy_TK = list(TkReqs)
                for rMaf in copy_TK:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        TkReqs.remove(rMaf)
                        clist[4] -= 1
                        setState(idx,"TK")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[4] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TkReqs.append(rMaf)
            else:
                 for rMaf in TK:
                     if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                         clist[4] -= 1
                         setState(idx,"TK")
                         q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                         clist[4] += 1
                         if q == True:
                             print idx,"was",tosBasher.roles[rMaf]
                             return True
        elif next == "TK" and clist[8] > 0:
            if len(TkReqs) != 0:
                copy_TK = list(TkReqs)
                for rMaf in copy_TK:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        TkReqs.remove(rMaf)
                        clist[8] -= 1
                        setState(idx,"TK")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TkReqs.append(rMaf)
            elif len(TSReqs) == 0 and len(TPReqs) == 0 and len(TIReqs) == 0:
                 for rMaf in TK:
                     if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                         clist[8] -= 1
                         setState(idx,"TK")
                         q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                         clist[8] += 1
                         if q == True:
                             print idx,"was",tosBasher.roles[rMaf]
                             return True
        elif next == "TS" and clist[5] > 0:
            if len(TSReqs) != 0:
                copy_TS = list(TSReqs)
                for rMaf in copy_TS:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[5] -= 1
                        TSReqs.remove(rMaf)
                        setState(idx,"TS")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[5] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TSReqs.append(rMaf)
            else:
                for rMaf in TS:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[5] -= 1
                        setState(idx,"TS")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[5] += 1
                        if q == True:
                            return True
        elif next == "TS" and clist[8] > 0:
            if len(TSReqs) != 0:
                copy_TS = list(TSReqs)
                for rMaf in copy_TS:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[8] -= 1
                        TSReqs.remove(rMaf)
                        setState(idx,"TS")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TSReqs.append(rMaf)
            elif len(TPReqs) == 0 and len(TkReqs) == 0 and len(TIReqs) == 0:
                for rMaf in TS:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[8] -= 1
                        setState(idx,"TS")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
        elif next == "Jailor" and clist[6] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("jailor")]:
                clist[6] -= 1
                setState(idx,"Jailor")
                q = update(clist,adjacent[idx],alreadyHave,RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                clist[6] += 1
                if q == True:
                    print idx,"was","jailer"
                    return True
        elif next == "TI" and clist[7] > 0:
            if len(TIReqs) != 0:
                copy_TK = list(TIReqs)
                for rMaf in copy_TK:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[7] -= 1
                        TIReqs.remove(rMaf)
                        setState(idx,"TI")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[7] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TIReqs.append(rMaf)
            else:
                for rMaf in TI:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[7] -= 1
                        setState(idx,"TI")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[7] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
        elif next == "TI" and clist[8] > 0:
            if len(TIReqs) != 0:
                copy_TK = list(TIReqs)
                for rMaf in copy_TK:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[8] -= 1
                        TIReqs.remove(rMaf)
                        setState(idx,"TI")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
                        TIReqs.append(rMaf)
            elif len(TSReqs) == 0 and len(TkReqs) == 0 and len(TPReqs) == 0:
                for rMaf in TI:
                    if cPlayers[idx-1].possible[rMaf] and not checkBit(alreadyHave,rMaf):
                        clist[8] -= 1
                        setState(idx,"TI")
                        q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                        clist[8] += 1
                        if q == True:
                            print idx,"was",tosBasher.roles[rMaf]
                            return True
        elif next == "NK" and clist[9] > 0:
            for rMaf in NK:
                if cPlayers[idx-1].possible[rMaf] and rMaf in EXPLNK:
                    clist[9] -= 1
                    setState(idx,"NK")
                    q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                    clist[9] += 1
                    if q == True:
                        print idx,"was",tosBasher.roles[rMaf]
                        return True
        elif next == "NE" and clist[10] > 0:
            for rMaf in NE:
                if cPlayers[idx-1].possible[rMaf] and rMaf in EXPLNE:
                    clist[10] -= 1
                    setState(idx,"NE")
                    q = update(clist,adjacent[idx],enableBit(alreadyHave,rMaf),RmReqs,TPReqs,TSReqs,TIReqs,TkReqs)
                    clist[10] += 1
                    if q == True:
                        print idx,"was",tosBasher.roles[rMaf]
                        return True
    if adjacent[idx] == 16:
        print "Ran out of options: ",idx,adjacent[idx],clist,queryList(idx),"didnt fit last min"
    else:
        print "Ran out of options: ",idx,adjacent[idx],clist,queryList(idx)
    return False
