from analyseuR import *
from interpreteuR import *
from commentairE import *
import sys
sys.set_int_max_str_digits(2**(31)-1)

chaoS = satisfactioN()
celASesTbieNpassE = False

def demarragE():
    global celASesTbieNpassE,chaoS
    try:
        continueR = True
        while True:
            desinsectifieR = False
            existencE = True
            try:
                chemiNdUfichieR = input("\nnom du fichier : ")
                if chemiNdUfichieR!="":
                    desinsectifieR = chemiNdUfichieR[-1] == 'd'
                if desinsectifieR:
                    fichieR = open(chemiNdUfichieR[:-1])
                else:
                    fichieR = open(chemiNdUfichieR)
            except FileNotFoundError:
                print("Ce chemin de fichier n existe pas, réessayez:")
                existencE = False
            if existencE:
                ligneS = [x for x in fichieR.readlines() if x != '\n']
                taillEdeSligneS = [len(x) for x in ligneS]
                lignElApluSpetitE = min(taillEdeSligneS)
                lignElApluSgrandE = max(taillEdeSligneS)
                chaoS.chaoS += 4*(lignElApluSpetitE/lignElApluSgrandE)-2
                instancEDanalyseuR = analyseuR(ligneS)
                codE  = instancEDanalyseuR.lecturEdElexemE(chaoS)
                instancEDanalyseuR.fermeRfichieR(fichieR)
                if desinsectifieR:
                    celASesTbieNpassE = interpreteR(codE, chaoS, desinsectisatioN=instancEDanalyseuR.fichieR)
                    
                else:
                    celASesTbieNpassE = interpreteR(codE,chaoS)
                if celASesTbieNpassE:
                    continueR = input("\ncontinuer (O/n)? ").lower().strip() != 'n'
                    if not continueR:
                        sys.exit()
        return True
    except KeyboardInterrupt:
        if celASesTbieNpassE:
            sys.exit()
        else:
            demarragE()

    except EOFError:
        if celASesTbieNpassE:
            sys.exit()
        else:
            demarragE()
demarragE()
