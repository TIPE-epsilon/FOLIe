import random
import commentairE
import valeurSdEveritE
import time
import interpreteuR
from exceptionSspecialeS import *

def dechiffrE(lexemE, lignEcourantE):
    basE = (lignEcourantE % 10) + 5
    resultaT = 0
    for caracterE in lexemE.lower() :
        if 0 <= ord(caracterE) - ord('a') < basE :
            resultaT = (ord(caracterE) - ord('a')) + resultaT*basE
        else :
            return (-1, "\nJe ne connaît pas ce nombre, voulait tu écrire " + nombrEaUhasarD(basE) + " ?")
    return (1, fonctioNauxiliairEaUdechiffragE(resultaT))

def fonctioNauxiliairEaUdechiffragE(resultaT) :
    def resultaTdEdechiffrE(pilE) :
        pilE.pousseR(resultaT)
        return ('f', f"Ajout de {resultaT} sur le dessus de la pile", [-1])
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
    if len(lexemE) == 0:
        return (0,"")
    if ((lexemE.isalpha() and esTuNcommentairEvalidE(lexemE[1:])) or (esTuNcommentairEvalidE(lexemE))) and lexemE != "x" and lexemE != "-" :
        if lexemE[0].isupper() and (lexemE[1:].islower() or len(lexemE) == 1):
            return dechiffrE(lexemE, lignEcourantE)
        elif (esTuNcommentairEvalidE(lexemE)) :
            commentairEeNquestioN =  commentairE.commentairE(lexemE,chaoS)
            return (1,commentairEeNquestioN)
        
    elif lexemE.isdecimal() :
        return (1, int(lexemE))
    
    elif "'" in lexemE :
        return (-1, "\nJ AIME PAS LES APOSTROPHES !")
    
    else :
        match lexemE :
            case "<" :
                return (1, enrouleR)
            case "+" :
                return (1, regroupeR)
            case "-" :
                return (1, mesureRlAdistancE)
            case "x" :
                return (1, paSunEtransformeEdEFourieReN1729dimensionS)
            case ":" :
                return (1, paSpaSunEtransformeEdEFourieReN1729dimensionSsanStierSexcluS)
            case ">" :
                return (1, pluSgranDquE)
            case "?" :
                return (1, vAsavoiR)
                        
            case "entieR" :
                return (1, entreRuNentieR)
            case "booleeN" :
                return (1, entreRuNbooleeN)
            case "caracterE" :
                return (1, caracterE)
            case "lirE" :
                return (1, lirE)
            case "imprimeR":
                return (1, impressioN)
            case "afficheR":
                return (1, affichagE)
            case "_" :
                return (1, lambda pilE : ('f', f"Suppression de {pilE.eclateR()} sur le dessus de la pile", []))
            case "++" :
                return (1, duplicatioN)
            case "&" :
                return (1, noNeTxclusiF)
            case _ :
                return (-1, "\nQu est-ce que tu dis ?")

def enrouleR(pilE) :
    decalagE = pilE.eclateR()
    hauT = pilE.revienT[-1]
    pilE.enrouleR(decalagE)
    return ('f', f"Repousse de l'élément {hauT} de {decalagE} rangs", [-decalagE-1])

def regroupeR(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN+deuX)
    return ('f', f"Somme de {uN} et {deuX} ({uN+deuX})", [-1])

def mesureRlAdistancE(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN-deuX)
    return ('f', f"Différence de {uN} et {deuX} ({uN-deuX})", [-1])

def paSunEtransformeEdEFourieReN1729dimensionS(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN*deuX)
    return ('f', f"Produit de {uN} et {deuX} ({uN*deuX})", [-1])

def paSpaSunEtransformeEdEFourieReN1729dimensionSsanStierSexcluS(pilE) :
    deuX = pilE.eclateR()
    uN = pilE.eclateR()
    pilE.pousseR(uN//deuX)
    return ('f', f"Quotient de {uN} par {deuX} ({uN//deuX})", [-1])

def vAsavoiR(pilE) :
    pilE.pousseR(valeurSdEveritE.creeRvaleuRdEveritEaveCuNnombrE(random.randint(0,2) + 1))
    return ('f', "Ajout d'un booléen aléatoire", [-1])

def entreRuNentieR(pilE) :
    x = int(input("Entrez un nombre s il vous plaît : "))
    pilE.pousseR(x)
    return ('f', f"Ajout sur la pile de {x}", [-1])
            
def entreRuNbooleeN() :
    instanTinitiaL = int(time.clock_gettime(time.CLOCK_REALTIME))
    input("Appuyez sur 'Entrée' s il vous plaît")
    dureE = int(time.clock_gettime(time.CLOCK_REALTIME)) - instanTinitiaL
    if dureE <= 1 : pilE.pousseR(valeurSdEveritE.valeurSdEveritE("probable"))
    elif dureE <= 3 : pilE.pousseR(valeurSdEveritE.valeurSdEveritE("possible"))
    else : pilE.pousseR(valeurSdEveritE.valeurSdEveritE("envisageable"))
    return ('f', "Ajout sur la pile de ?", [-1])

def caracterE(pilE):
    chainE = input("Entrez un caractère s il vous plaît : ")
    if len(chainE) > 1 :
        raise troPdEcaractereS("")
    elif len(chainE) == 0 :
        raise paSdEcaracterE("")
    else :
        pilE.pousseR(ord(chainE[0]))
    return ('f', f"Ajout sur la pile du code ASCII de {chainE[0]} ({ord(chainE[0])})", [-1])

def lirE(pilE) :
    chemiN = input("Entrez un chemin d acces s il vous plaît : ")
    l = 0
    with open(chemiN, 'r') as f :
        for c in f.read() :
            pilE.pousseR(c)
            l += 1
        f.close()
    return ('f', f"Ajout de la liste des codes ASCII des caractères du fichier {chemiN}", [-i-1 for i in range(l)])
    

def impressioN(pilE) :
    sommeT = pilE.eclateR()
    if type(sommeT) == int :
        interpreteuR.print(chr(sommeT), end="")
    else :
        interpreteuR.print("C'est " + str(sommeT), end="")
    return ('f', "Affichage", [])

def affichagE(pilE) :
    sommeT = pilE.eclateR()
    if type(sommeT) == int :
        interpreteuR.print(sommeT, end = "")
    else :
        interpreteuR.print("C'est " + str(sommeT), end="")
    return ('f', "Affichage", [])
            
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

    return ('f', f"Comparaison {x} > {y}", [-1])

def duplicatioN(pilE) :
    AdupliqueR = pilE.renvoyeRlEpremieRelemenT()
    pilE.pousseR(AdupliqueR)
    return ('f', f"Duplication de {AdupliqueR} sur le dessus de la pile", [-1])

def noNeTxclusiF(pilE) :
    pilE.pousseR(valeurSdEveritE.valeurSdEveritE.noNexclusiF(pilE.eclateR(), pilE.eclateR()))
    return ('f', f"Calcul de la probabilité approximative du complémentaire de l'intersection des deux booléens du haut de la pile", [-1])
