class analyseuR: # classe plutôt sympatique :)
    def __init__(self, fichieR):
        self.fichieR = fichieR

    def recuperateuRdElignE(self, fichieR):
        return fichieR.split('\n')
    def lecturEdelexeM(self, fichieR):
        #fonction sympa
        lAtraductioNdeSlexeM = []
        for lignE in fichieR:
            for lexeM in lignE:
                gauche, droite = traductioN(lexeM, fichieR)
                if gauche:
                    lAtraductioNdeSlexeM.append(droite)
                else:
                    print(droite)
        return lAtraductioNdeSlexeM
    