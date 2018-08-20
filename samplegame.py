import tosBasher

cPlayers = [CurrentPerson() for i in range(0,15)]

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
