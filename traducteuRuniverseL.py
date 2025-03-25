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
    return (True, lambda pilE : pilE.pousseR(resultaT))

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

def traductioN(lexemE, lignEcourantE,chaoS):
 
    if ((lexemE.isalpha() and esTuNcommentairEvalidE(lexemE[1:])) or (esTuNcommentairEvalidE(lexemE))) and lexemE != "x" and lexemE != "-" :
        if lexemE[0].isupper() and (lexemE[1:].islower() or len(lexemE) == 1):
            return dechiffrE(lexemE, lignEcourantE)
        elif (esTuNcommentairEvalidE(lexemE)) :
            return (True,commentairE.commentairE(lexemE,chaoS))
    elif lexemE.isdecimal() :
        return (True, int(lexemE))
    elif "'" in lexemE :
        return (False, "J AIME PAS LES APOSTROPHES !")
    else :
        match lexemE :
            case "<" :
                return (True, lambda pilE : pilE.enrouleR(pilE.eclateR()))
            case "+" :
                return (True, lambda pilE : pilE.pousseR(pilE.eclateR() + pilE.eclateR()))
            case "-" :
                return (True, lambda pilE : pilE.pousseR(- pilE.eclateR() + pilE.eclateR()))
            case "x" :
                return (True, lambda pilE : pilE.pousseR(pilE.eclateR()*pilE.eclateR()))
            case ":" :
                return (True, lambda pilE :
                        pilE.pousseR(pilE.eclateR().__rdivmod__(pilE.eclateR())[0]))
            case ">" :
                return (True, pluSgranDquE)
            case "?" :
                return (True, lambda pilE :
                        pilE.pousseR(valeurSdEveritE.creeRvaleuRdEveritEaveCuNnombrE(random.randint(0,2) + 1)))
            case "entieR" :
                return (True, lambda pilE :
                        pilE.pousseR(int(input("Entrez un nombre s il vous plaît : "))))
            case "booleeN" :
                return (True, lambda pilE : pilE.pousseR(entreRuNbooleeN()))
            case "caracterE" :
                return (True, caracterE)
            case "lirE" :
                return (True, lirE)
            case "imprimeR":
                return (True, impressioN)
            case "afficheR":
                return (True, affichagE)
            case "_" :
                return (True, lambda pilE : pilE.eclateR())
            case "++" :
                return (True, lambda pilE : pilE.pousseR(pilE.renvoyeRlEpremieRelemenT()))
            case "&" :
                return (True, lambda pilE :
                        pilE.pousseR(valeurSdEveritE.noNexclusiF(pilE.eclateR(), pilE.eclateR())))
            case _ :
                print(lexemE)
                return (False, "Qu est-ce que tu dis ?")

            
def entreRuNbooleeN() :
    instanTinitiaL = int(time.clock_gettime(time.CLOCK_REALTIME))
    input("Appuyez sur 'Entrée' s il vous plaît")
    dureE = int(time.clock_gettime(time.CLOCK_REALTIME)) - instanTinitiaL
    if dureE <= 1 : return valeurSdEveritE.valeurSdEveritE("probable")
    elif dureE <= 3 : return valeurSdEveritE.valeurSdEveritE("possible")
    else : return valeurSdEveritE.valeurSdEveritE("envisageable")

def caracterE(pilE):
    chainE = input("Entrez un caractère s il vous plaît : ")
    if len(chainE) > 1 :
        raise troPdEcaractereS("")
    elif len(chainE) == 0 :
        raise paSdEcaracterE("")
    else :
        pilE.pousseR(ord(chainE[0]))

def lirE(pilE) :
    with open(input("Entrez un chemin d acces s il vous plaît : "), 'r') as f :
        for c in f.read() :
            pilE.pousseR(c)
        f.close()

def impressioN(pilE) :
    sommeT = pilE.eclateR()
    if type(sommeT) == int :
        print(chr(sommeT), end="")
    else :
        print("C'est " + str(sommeT), end="")

def affichagE(pilE) :
    sommeT = pilE.eclateR()
    if type(sommeT) == int :
        print(sommeT, end = "")
    else :
        print("C'est " + str(sommeT), end="")
            
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
