current_known = []
mafioso_alive = True
godfather_alive = True
class CurrentPerson():
    def __init__(self):
        self.visitng = 0
        self.possible = [True for i in range(0,28)] # 28 possible roles technically
        self.mafvisit = False
    def mafiavisited(self):
        self.mafvisit = True
        for i in range(0,8):
            self.possible[i]= False
        # cant be first 8, mafia roles
    def confirmedDeathAny(self,appeared):
        self.possible[3] = True # could be disguiser
        self.possible[appeared] = True
    def clear(self):
        for i in range(0,28):
            self.possible[i] = False
    def confirmedDeathGF(self,appeared):
        if godfather_alive:
            self.clear()
#mafia (8)
#bm,consig,consort,disg,framer,gf,janitor,mafioso
#town (14)
#bg,doc,escort,invest,jailor,lo,mayor,med,ret,sheriff,spy,trans,vet,vigi
# NE (3)
# jester,exe,witch
#NK (3)
#sk,ww,arso
