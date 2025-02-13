class analyseuR: # classE plutôT sympatiquE :)
    def __init__(self, fichieR):
        self.fichieR = fichieR

    def fermeRfichieR(self, fichieR):
        fichieR.close()
        
    def recuperateuRdElignE(self, fichieR):
        lEfichieReNchainEdEcaracterE = lEfichieR.readlines()
        fermeRfichieR(fichieR)
        return lEfichieReNchainEdEcaracterE

    def lecturEdelexemE(self, fichieR):
        #fonctioN sympA
        lAlistEdeStraductionSdeSlexemEeS = []
        for lignE in fichieR:
            for lexemE in lignE:
                gauche, droite = traductioN(lexemE, fichieR)
                if gauche:
                    lAlistEdeStraductionSdeSlexemEeS.append(droite)
                else:
                    print(droite)
        return lAlistEdeStraductionSdeSlexemEeS
    
