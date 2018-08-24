'''
DEPRICATED
This is v1.  We will move to v2 which will feature more smoother stuff such as bottom up claiming.  Bottom up claiming is where the lower sectors have higher constraints and higher sectors can be more fluid.
'''

import tosBasher
import random
cPlayers = [tosBasher.CurrentPerson() for i in range(0,15)]

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
cFit = [2,1,1,1,1,1,1,2,3,1,1]
types= ["RM","MAFIOSO","GF","TP","TK","TS","Jailor","TI","RT","NK","NE"]

def update(clist,idx):
    print idx
    if idx == 16:
        print "Found Solution"
        return True
    checkwise = list(types)
    random.shuffle(checkwise)
    while checkwise != []:
        next = checkwise.pop(0)
        if next == "RM" and clist[0] > 0:
            for rMaf in RM:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[0] -= 1
                    q = update(clist,idx+1)
                    clist[0] += 1
                    if q:
                        print idx,"was","random mafia: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "MAFIOSO" and clist[1] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("mafioso")]:
                clist[1] -= 1
                q = update(clist,idx+1)
                if q  == True:
                    print idx,"was mafioso"
                    return True
                clist[1] += 1
        elif next == "GF" and clist[2] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("gf")]:
                clist[2] -= 1
                q = update(clist,idx+1)
                if q  == True:
                    print idx,"was gf"
                    return True
                clist[2] += 1
        elif next == "TP" and clist[3] > 0:
            for rMaf in TP:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[3] -= 1
                    q = update(clist,idx+1)
                    clist[3] += 1
                    if q:
                        print idx,"was","town prot: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "TK" and clist[4] > 0:
            for rMaf in TK:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[4] -= 1
                    q = update(clist,idx+1)
                    clist[4] += 1
                    if q:
                        print idx,"was","town killing: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "TS" and clist[5] > 0:
            for rMaf in TS:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[5] -= 1
                    q = update(clist,idx+1)
                    clist[5] += 1
                    if q:
                        print idx,"was","town supportive: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "Jailor" and clist[6] > 0:
            if cPlayers[idx-1].possible[tosBasher.get("jailor")]:
                clist[6] -= 1
                q = update(clist,idx+1)
                if q  == True:
                    print idx,"was jailor"
                    return True
                clist[6] += 1
        elif next == "TI" and clist[7] > 0:
            for rMaf in TI:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[7] -= 1
                    q = update(clist,idx+1)
                    clist[7] += 1
                    if q:
                        print idx,"was","town investigative: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "RT" and clist[8] > 0:
            for rMaf in TS+TK+TP+TI:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[8] -= 1
                    q = update(clist,idx+1)
                    clist[8] += 1
                    if q:
                        print idx,"was","town random: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "NK" and clist[9] > 0:
            for rMaf in NK:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[9] -= 1
                    q = update(clist,idx+1)
                    clist[9] += 1
                    if q:
                        print idx,"was","newt kil: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
        elif next == "NE" and clist[10] > 0:
            for rMaf in NE:
                if cPlayers[idx-1].possible[rMaf]:
                    clist[10] -= 1
                    q = update(clist,idx+1)
                    clist[10] += 1
                    if q:
                        print idx,"was","newt evil: ",rMaf,tosBasher.roles[rMaf]
                        return True
                    else:
                        break
    return False


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
