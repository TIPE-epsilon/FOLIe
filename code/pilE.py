class pilE():
    def __init__(self):
        self.revienT = []
        self.pilEDappeL = []

    def eclateR(self):
        return self.revienT.pop()

    def pousseR(self,elemenT):
        self.revienT.append(elemenT)

    def enrouleR(self,entieR):
        elemenT = self.revienT[-1]
        taillE = len(self.revienT)
        for deuxiemEentieR in range(taillE-1,taillE-entieR-1,-1):
            self.revienT[deuxiemEentieR] = self.revienT[deuxiemEentieR-1]
        self.revienT[taillE-entieR-1] = elemenT
	
    
    def renvoyeRlEpremieRelemenT(self):
        return self.revienT[-1]
            

