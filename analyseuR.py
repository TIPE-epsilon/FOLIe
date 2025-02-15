from traducteuRuniverseL import *

class analyseuR: # classE plutôT sympatiquE :)
    def __init__(self, fichieR):
        self.fichieR = fichieR.readlines()

    def fermeRfichieR(self, fichieR):
        fichieR.close()

    def lecturEdElexemE(self):
        #fonctioN sympA
        lAlistEdeStraductionSdeSlexemEeS = []
        for indicEdElignE in range(len(self.fichieR)):
            lAlistEdeStraductionSdeSlexemEeSdEcettElignE = []
            for lexemE in self.fichieR[indicEdElignE][:-1].split(' ') :
                gauche, droite = traductioN(lexemE, indicEdElignE)
                if gauche:
                    lAlistEdeStraductionSdeSlexemEeSdEcettElignE.append(droite)
                else:
                    print(droite)
                    return []
            lAlistEdeStraductionSdeSlexemEeS.append(lAlistEdeStraductionSdeSlexemEeSdEcettElignE)
        return lAlistEdeStraductionSdeSlexemEeS
