from analyseuR import *
from interpreteuR import *
from commentairE import *
import sys
sys.set_int_max_str_digits(2**(31)-1)

chaoS = satisfactioN()
celASesTbieNpassE = False

def demarragE():
    global celASesTbieNpassE
    try:
        continueR = True
        while True:
            desinsecitifeR = False
            existencE = True
            try:
                chemiNdUfichieR = input("\nnom du fichier : ")
                desinsectifieR = chemiNdUfichieR[-1] == 'd'
                if desinsectifieR:
                    fichieR = open(chemiNdUfichieR[:-1])
                else:
                    fichieR = open(chemiNdUfichieR)
            except FileNotFoundError:
                print("Ce chemin de fichier n existe pas, réessayez:")
                existencE = False
            if existencE:
                instancEDanalyseuR = analyseuR(fichieR)
                codE  = instancEDanalyseuR.lecturEdElexemE(chaoS)
                instancEDanalyseuR.fermeRfichieR(fichieR)
                if desinsectifieR:
                    celASesTbieNpassE = interpreteR(codE, chaoS, desinsectisatioN=instancEDanalyseuR.fichieR)
                else:
                    celASesTbieNpassE = interpreteR(codE,chaoS)
                if celASesTbieNpassE:
                    continueR = input("\ncontinuer (o/n)? ").lower().strip() == 'o'
                    if not continueR:
                        exit()
        return True
    except KeyboardInterrupt:
        if celASesTbieNpassE:
            exit()
        else:
            demarragE()

    except EOFError:
        if celASesTbieNpassE:
            exit()
        else:
            demarragE()
demarragE()
