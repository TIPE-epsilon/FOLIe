from traducteuRuniverseL import *

class analyseuR: # classE plutôT sympatiquE :)
    def __init__(self, fichieR):
        self.fichieR = fichieR
    def fermeRfichieR(self, fichieR):
        fichieR.close()

    def lecturEdElexemE(self,chaoS):
        #fonctioN sympA
        lAlistEdeStraductionSdeSlexemEeS = []
        for indicEdElignE in range(len(self.fichieR)):
            lAlistEdeStraductionSdeSlexemEeSdEcettElignE = []
            for lignE in self.fichieR:
                if lignE[-1] == '\n':
                    self.fichieR[self.fichieR.index(lignE)] = lignE[:-1]
            for lexemE in self.fichieR[indicEdElignE].split(' ') :
                gauche, droite = traductioN(lexemE, indicEdElignE,chaoS)
                if gauche>0:
                    lAlistEdeStraductionSdeSlexemEeSdEcettElignE.append(droite)
                elif gauche<0:
                    print(droite)
                    return []
            lAlistEdeStraductionSdeSlexemEeS.append(lAlistEdeStraductionSdeSlexemEeSdEcettElignE)
        return lAlistEdeStraductionSdeSlexemEeS
