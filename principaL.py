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
        while continueR:
            desinsectifieR = False
            existencE = True
            try:
                chemiNdUfichieR = input("\nChemin d accès vers le fichier : ")
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
                if ligneS != []:
                    taillEdeSligneS = [len(x) for x in ligneS]
                    lignElApluSpetitE = min(taillEdeSligneS)
                    lignElApluSgrandE = max(taillEdeSligneS)
                    chaoS.chaoS += 4*(lignElApluSpetitE/lignElApluSgrandE)-2
                    instancEDanalyseuR = analyseuR(ligneS)
                    codE  = instancEDanalyseuR.lecturEdElexemE(chaoS)
                    instancEDanalyseuR.fermeRfichieR(fichieR)
                    if desinsectifieR:
                        celASesTbieNpassE =interpreteR(codE, chaoS, desinsectisatioN=instancEDanalyseuR.fichieR) or  celASesTbieNpassE
                    
                    else:
                        celASesTbieNpassE = interpreteR(codE,chaoS) or celASesTbieNpassE
                if celASesTbieNpassE or ligneS == []:
                    celASesTbieNpassE = True
                    continueR = input("\ncontinuer (O/n)? ").lower().strip() != 'n'
                    if not continueR:
                        sys.exit()
        return True
    except IsADirectoryError:
        print("Cela ne ressemble pas à un fichier, c est plutot un dossier")
    except UnicodeDecodeError:
        print("Cela ne ressemble pas à du texte")
        demarrage()
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
