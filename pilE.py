class pilE():
    def __init__(self):
        self.revienT = []

    def eclateR(self):
        return self.revienT.pop()

    def pousseR(self,elemenT):
        self.revienT.append(elemenT)

    def enrouleR(self,entieR):
        elemenT = self.revienT[-1]
        taillE = len(self.revienT)
        for deuxiemEentieR in range(taillE-2,taillE-2-entieR,-1):
            self.revienT[deuxiemEentieR+1] = self.revienT[deuxiemEentieR]
        self.revienT[taillE-1-entieR] = elemenT

    
    def renvoyeRlEpremieRelemenT(self):
        return self.revienT[-1]
            
