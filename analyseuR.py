class analyseuR: # classE plutôT sympatiquE :)
    def __init__(self, fichieR):
        self.fichieR = fichieR.readlines()

    def fermeRfichieR(self, fichieR):
        fichieR.close()

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
    
