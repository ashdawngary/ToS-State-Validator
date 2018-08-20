current_known = []
mafioso_alive = True
godfather_alive = True
class CurrentPerson:
    def __init__(self):
        self.visitng = 0
        self.possible = [True for i in range(0,28)] # 28 possible roles technically
        self.mafvisit = False
    def mafiavisited(self):
        self.mafvisit = True
        for i in range(0,9):
            self.possible[i]= False
        # cant be first 8, mafia roles
    def applyvisiting(self):
        cant_visit = ["medium","mayor","jailor","veteran","vigi"]
        for i in range(0,len(roles)):
            if roles[i] in cant_visit:
                self.possible[i] = False

    def confirmedDeath(self,appeared):
        self.clear()
        self.possible[3] = True # could be disguiser
        self.possible[appeared] = True
    def clear(self):
        for i in range(0,29):
            self.possible[i] = False
    def confirmedDeathGF(self):
        global mafioso_alive
        global godfather_alive
        if godfather_alive:
            self.clear()
            godfather_alive = False
            self.possible[godfather] = True
        else:
            self.clear()
            mafioso_alive = False
            self.possible[mafioso] = True
    def confirmedDeathMafioso(self):
        global mafioso_alive
        global godfather_alive

        if mafioso_alive or godfather_alive:
            mafioso_alive = False
            self.clear()
            self.possible[mafioso]  = True
        else:
            self.clear()
            for random_mafia in RM:
                self.possible[random_mafia] = True
    def confirmedDeathJailorExe(self,role):
        self.clear()
        self.possible[role] = True
    def isMafia(self):
        for i in range(9,29):
            self.possible[i] = False
    def jesteryClaim(self,role):
        # potential jester / exe / mafia / or actual claim but nothing else.
        self.clear()
        self.possible[roles.index("jester")] = True
        self.possible[roles.index("exe")] = True
        for random_mafia in RM:
            self.possible[random_mafia] = True
        self.possible[role] = True
        updateEntity()
    def onClaim(self,role):
        # always consider that it could be Random Mafia unless they are confirmed
        # consider that they maybe be either mafia / jester / or the role that they claim / or some crappy NK claim.
        for random_mafa in RM:
            self.possible[random_mafia] = True
        self.claim[roles.index("jester")] = True
        self.claim[role] = True
        self.claim[roles.index("vet")]  =True # could be some crappy vet bait we never know
        updateEntity()
    def onInvestResults(self,role):
        #invest results take over, we can only expect that the person is one of the three.
        for result_group in invest_res:
            if role in result_group:
                self.clear()
                for possible_alias in result_group:
                    self.possible[possible_alias] = True
        updateEntity()
    def updateEntity():
        if self.mafvisit:
            self.mafiavisited()
        elif self.visiting == 1:
            self.applyvisiting()
    def confirmedSelf(self,role):
        self.clear()
        self.possible[role] = True
        updateEntity()
def get(role):
    return roles.index(role)
roles = ["bm","consig","consort","disg","framer","gf","janitor","forger","mafioso","bg","doc","escort","invest","jailor","lo","mayor","med","ret","sheriff","spy","trans","vet","vigi","jester","exe"]
roles.extend(["witch","sk","ww","arso"])
invest_res = [[get("spy"),get("bm"),get("jailor")],[get("invest"),get("consig"),get("mayor")],[get("sheriff"),get("exe"),get("ww")],[get("framer"),get("jester")]]
invest_res.append([get("bg"),get("gf"),get("arso")])
invest_res.append([get("escort"),get("trans"),get("consort")])
invest_res.append([get("ret"),get("med"),get("janitor")])
invest_res.append([get("vigi"),get("vet"),get("mafioso")])
invest_res.append([get("lo"),get("forger"),get("witch")])
invest_res.append([get("doc"),get("disg"),get("sk")])

# spy / bm(0) / jailer
# invest / consig / mayor
# sheriff / exe / ww
# framer / vamp / jester
# bg  /gf / arso
# esc / trans / cons
# ret / med / janitor
# vig / vet / mafioso
# lo  / forger / witch
# doc / disg / sk
RM = [0,1,2,3,4,6,7]
mafioso = 8
godfather = 5
#mafia (8)
#bm,consig,consort,disg,framer,gf,janitor,mafioso

#town (14)
#bg,doc,escort,invest,jailor,lo,mayor,med,ret,sheriff,spy,trans,vet,vigi
# NE (3)
# jester,exe,witch
#NK (3)
#sk,ww,arso
