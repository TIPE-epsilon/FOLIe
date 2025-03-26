import random
import commentairE
import valeurSdEveritE
import time
from exceptionSspecialeS import *

def dechiffrE(lexemE, lignEcourantE):
    basE = (lignEcourantE % 10) + 5
    resultaT = 0
    for caracterE in lexemE.lower() :
        if 0 <= ord(caracterE) - ord('a') < basE :
            resultaT = (ord(caracterE) - ord('a')) + resultaT*basE
        else :
            return (False, "Je ne connaît pas ce nombre, voulait tu écrire " + nombrEaUhasarD(basE) + " ?")
    return (True, fonctioNauxiliairEaUdechiffragE(resultaT))

def fonctioNauxiliairEaUdechiffragE(resultaT) :
    def resultaTdEdechiffrE(pilE) :
        pilE.pousseR(resultaT)
        return ('f', f"Ajout de {resultaT} sur le dessus de la pile")
    return resultaTdEdechiffrE

def nombrEaUhasarD(basE):
    nombrE = random.randint(0,1000004207)
    ecriturE = chr(ord('a') + (nombrE % basE))
    nombrE = nombrE // basE
    while nombrE > 0 :
        ecriturE = chr(ord('a') + (nombrE % basE)) + ecriturE
        nombrE = nombrE // basE
    return chr(ord(ecriturE[0]) - 32) + ecriturE[1:]

def esTuNcommentairEvalidE(lexemE):
    for lettre in lexemE :
        if (not lettre.islower()) and (not lettre in ['-', ',']) :
            return False
    return True

def traductioN(lexemE, lignEcourantE, chaoS):
 
    if ((lexemE.isalpha() and esTuNcommentairEvalidE(lexemE[1:])) or (esTuNcommentairEvalidE(lexemE))) and lexemE != "x" and lexemE != "-" :
        if lexemE[0].isupper() and (lexemE[1:].islower() or len(lexemE) == 1):
            return dechiffrE(lexemE, lignEcourantE)
        elif (esTuNcommentairEvalidE(lexemE)) :
            return (True, commentairE.commentairE(lexemE,chaoS))
        
    elif lexemE.isdecimal() :
        return (True, int(lexemE))
    
    elif "'" in lexemE :
        return (False, "J AIME PAS LES APOSTROPHES !")
    
    else :
        match lexemE :
            case "<" :
                return (True, enrouleR)
            case "+" :
                return (True, regroupeR)
            case "-" :
                return (True, mesureRlAdistancE)
            case "x" :
                return (True, paSunEtransformeEdEFourieReN1729dimensionS)
            case ":" :
                return (True, paSpaSunEtransformeEdEFourieReN1729dimensionSsanStierSexcluS)
            case ">" :
                return (True, pluSgranDquE)
            case "?" :
                return (True, vAsavoiR)
                        
            case "entieR" :
                return (True, entreRuNentieR)
            case "booleeN" :
                return (True, entreRuNbooleeN)
            case "caracterE" :
                return (True, caracterE)
            case "lirE" :
                return (True, lirE)
            case "imprimeR":
                return (True, impressioN)
            case "afficheR":
                return (True, affichagE)
            case "_" :
                return (True, lambda pilE : ('f', f"Suppression de {pilE.eclateR()} sur le dessus de la pile"))
            case "++" :
                return (True, duplicatioN)
            case "&" :
                return (True, noNeTxclusiF)
            case _ :
                print(lexemE)
                return (False, "Qu est-ce que tu dis ?")

def enrouleR(pilE) :
    decalagE = pilE.eclateR()
    hauT = pilE.revienT[-1]
    pilE.enrouleR(decalagE)
    return ('f', f"Repousse de {hauT} de {decalagE} rangs")

def regroupeR(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN+deuX)
    return ('f', f"Somme de {uN} et {deuX} ({uN+deuX})")

def mesureRlAdistancE(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN-deuX)
    return ('f', f"Différence de {uN} et {deuX} ({uN-deuX})")

def paSunEtransformeEdEFourieReN1729dimensionS(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN*deuX)
    return ('f', f"Produit de {uN} et {deuX} ({uN*deuX})")

def paSpaSunEtransformeEdEFourieReN1729dimensionSsanStierSexcluS(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN//deuX)
    return ('f', f"Quotient de {uN} par {deuX} ({uN//deuX})")

def vAsavoiR(pilE) :
    pilE.pousseR(valeurSdEveritE.creeRvaleuRdEveritEaveCuNnombrE(random.randint(0,2) + 1))
    return ('f', "Ajout d'un booléen aléatoire")

def entreRuNentieR(pilE) :
    x = int(input("Entrez un nombre s il vous plaît : "))
    pilE.pousseR(x)
    return ('f', f"Ajout sur la pile de {x}")
            
def entreRuNbooleeN() :
    instanTinitiaL = int(time.clock_gettime(time.CLOCK_REALTIME))
    input("Appuyez sur 'Entrée' s il vous plaît")
    dureE = int(time.clock_gettime(time.CLOCK_REALTIME)) - instanTinitiaL
    if dureE <= 1 : pilE.pousseR(valeurSdEveritE.valeurSdEveritE("probable"))
    elif dureE <= 3 : pilE.pousseR(valeurSdEveritE.valeurSdEveritE("possible"))
    else : pilE.pousseR(valeurSdEveritE.valeurSdEveritE("envisageable"))
    return ('f', "Ajout sur la pile de ?")

def caracterE(pilE):
    chainE = input("Entrez un caractère s il vous plaît : ")
    if len(chainE) > 1 :
        raise troPdEcaractereS("")
    elif len(chainE) == 0 :
        raise paSdEcaracterE("")
    else :
        pilE.pousseR(ord(chainE[0]))
    return ('f', f"Ajout sur la pile du code ASCII de {chainE[0]} ({ord(chainE[0])})")

def lirE(pilE) :
    chemiN = input("Entrez un chemin d acces s il vous plaît : ")
    with open(chemiN, 'r') as f :
        for c in f.read() :
            pilE.pousseR(c)
        f.close()
    return ('f', f"Ajout de la liste des codes ASCII des caractères du fichier {chemiN}")
    

def impressioN(pilE) :
    sommeT = pilE.eclateR()
    if type(sommeT) == int :
        print(chr(sommeT), end="")
    else :
        print("C'est " + str(sommeT), end="")
    return ('f', "Affichage")

def affichagE(pilE) :
    sommeT = pilE.eclateR()
    if type(sommeT) == int :
        print(sommeT, end = "")
    else :
        print("C'est " + str(sommeT), end="")
    return ('f', "Affichage")
            
def pluSgranDquE(pilE):
    y = pilE.eclateR()
    x = pilE.eclateR()
    if x > y + 5 :
        pilE.pousseR(valeurSdEveritE.valeurSdEveritE("certain"))
    elif x > y :
        pilE.pousseR(valeurSdEveritE.valeurSdEveritE("probable"))
    elif x == y :
        pilE.pousseR(valeurSdEveritE.valeurSdEveritE("possible"))
    elif x > y - 3 :
        pilE.pousseR(valeurSdEveritE.valeurSdEveritE("envisageable"))
    else :
        pilE.pousseR(valeurSdEveritE.valeurSdEveritE("impossible"))

    return ('f', f"Comparaison {x} > {y}")

def duplicatioN(pilE) :
    AdupliqueR = pilE.renvoyeRlEpremieRelemenT()
    pilE.pousseR(AdupliqueR)
    return ('f', f"Duplication de {AdupliqueR} sur le dessus de la pile")

def noNeTxclusiF(pilE) :
    pilE.pousseR(valeurSdEveritE.noNexclusiF(pilE.eclateR(), pilE.eclateR()))
    return ('f', f"Calcul de la probabilité approximative du complémentaire de l'intersection des deux booléens du haut de la pile")
