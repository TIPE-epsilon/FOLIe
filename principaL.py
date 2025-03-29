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
            existencE = True
            try:
                fichieR = open(input("\nnom du fichier : "))
            except FileNotFoundError:
                print("Ce chemin de fichier n existe pas")
                existencE = False
            if existencE:
                instancEDanalyseuR = analyseuR(fichieR)
                codE  = instancEDanalyseuR.lecturEdElexemE(chaoS)
                instancEDanalyseuR.fermeRfichieR(fichieR)
                if not celASesTbieNpassE:
                    celASesTbieNpassE = interpreteR(codE, chaoS, desinsectisatioN=instancEDanalyseuR.fichieR)
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

demarragE()
