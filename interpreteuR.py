import pilE as modulEdEpilE
import random
from commentairE import *
from exceptionSspecialeS import *
import valeurSdEveritE as modulEdEvaleurSdEveritE

erreurSpossibleS = lambda lignE, elemenT : {
    "lApilEesTvidE" : [
        "Pffffffffff.",
        "Il n y a plus rien ici.",
        "Il n y a plus rien dans la pile",
        f"Je ne peux pas {elemenT} si il n y a plus rien dans la pile",
        f"Tu me demande de {elemenT} à la ligne {lignE}, mais il n y a plus rien dans la pile"
    ],
    "jEnEsuiSpaSuNbooleeN": [
        "7 | 7 | 7 | 0 | 9 | 17 | 12 | 1 | 1 | 3 | 5 | 8 | 18 | 17 | 3 | 5 | 8 | 19 | 0 | 9 | 20 | 12 | 1 | 3 | 3 | 5 | 8 | 21 | 18 | 5 | 9 | 17 | 0 | 27 | 14 | 1 | 3 | 5 | 9 | 20 | 15",
        "On va où là ?",
        "Ce n est pas un booléen ça",
        f"L appel de fonction ne peut pas se faire avec {elemenT} sur le dessus de la pile",
        f"Tu essaye de faire un appel de fonction avec {elemenT} sur le dessus de la pile (à la ligne {lignE})"
    ],
    "lAlignEoUtUveuXalleResTtroPloiN" : [
        "Ça ne fait pas QUE afficher 20, s21 c'est bien plus que ça",
        "On va où là ?",
        "Je ne peut pas aller à une ligne qui n existe pas",
        f"La fonction {elemenT} n existe pas",
        f"À la ligne {lignE}, tu me dit d appeler la fonction {elemenT}, qui n existe pas !"
    ],
    "erreuRdEtypE" : [
        "Mais qui est ce rustre ?",
        "Je n apprécie pas ce que je vois",
        "Ce n est pas le bon type",
        f"Je n ai pas le type nécessaire pour appliquer la fonction {elemenT}",
        f"À la ligne {lignE}, je ne peux pas appliquer la fonction {elemenT} à un élément de ce type"
    ],
    "divisioNpaRzerO" : [
        "C est dur à calculer",
        "+\\infty",
        "0 ∉ ℝ*",
        "Tu as essayé d inverser zéro",
        f"À la ligne {lignE}, tu as effectué une division par zéro"
    ],
    "troPdEcaractereS" : [
        "Et c est moi qui choisis ?",
        "Il est long ce mot.",
        "Tu connais la différence entre un caractère et une chaîne ?",
        "Tu as donné plus d'un caractère",
        f"À la ligne {lignE}, tu demande un caractère, mais tu en as donné trop"
    ],
    "paSdEcaracterE" : [
        "Il est où ?",
        "Je suis censé deviner ?",
        "Ça fait pas beaucoup d'information",
        "Tu n as rien rentré",
        f"À la ligne {lignE}, tu demande un caractère, mais tu n en as pas donné"
    ],
    "paSdEfichieR" : [
        "Il est où ?",
        "Attend je cherche",
        "Mais il existe pas",
        f"Il n y a pas de fichier {elemenT}",
        f"À la ligne {lignE}, tu me demande de lire un fichier, mais {elemenT} n existe pas"
    ],
    "paSdEdroiT" : [
        "Oh le nul",
        "« Tous les animaux sont égaux, mais certains sont plus égaux que d'autres. »\n    - Georges Orwell, \033[3mLa ferme des animaux\033[0m, 1945",
        "Tu n as pas le droit",
        f"Tu n as pas le droit de lire {elemenT}",
        f"À la ligne {lignE}, tu me demande de lire {elemenT} mais sans posséder ce droit de lecture"
    ]
    
}

def interpreteR(codE,chaoS):
    
    pointeuRdElignE = 0
    compteuRsuRlAlignE = 0
    pilEdELexecutioN = modulEdEpilE.pilE()
    
    while compteuRsuRlAlignE < len(codE[pointeuRdElignE]) :
        unitEdEcodE = codE[pointeuRdElignE][compteuRsuRlAlignE]

        #for elemenT in pilEdELexecutioN.revienT :
        #    print(elemenT, end = " ")
        #print("")
        if type(unitEdEcodE) == int :
            if unitEdEcodE >= len(codE) :
                print(erreurSpossibleS(lignE, "faire un appel de fonction")["lAlignEoUtUveuXalleResTtroPloiN"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            
            if len(pilEdELexecutioN.revienT) == 0 :
                print(erreurSpossibleS(lignE, "faire un appel de fonction")["lApilEesTvidE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
                
            conditioNdEsauT = pilEdELexecutioN.eclateR()
            if type(conditioNdEsauT) != modulEdEvaleurSdEveritE.valeurSdEveritE :
                print(erreurSpossibleS(pointeuRdElignE, conditioNdEsauT)["jEnEsuiSpaSuNbooleeN"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            
            choiXaleatoirE = random.randint(1,4)
            if conditioNdEsauT.valeuRdEveritE >= choiXaleatoirE :
                pilEdELexecutioN.pilEDappeL.append((pointeuRdElignE, compteuRsuRlAlignE))
                pointeuRdElignE = unitEdEcodE
                compteuRsuRlAlignE = -1
                
                
        elif type(unitEdEcodE) == commentairE :
            
            resultaTdElAmisEAjouRdUchaoS = unitEdEcodE.initialisatioNdUcommentairE()
            if not resultaTdElAmisEAjouRdUchaoS[0] :
                print(resultaTdElAmisEAjouRdUchaoS[1])
                return False
            
        else :
            try :
                unitEdEcodE(pilEdELexecutioN)
            except TypeError :
                print(erreurSpossibleS(pointeuRdElignE, unitEdEcodE)["erreuRdEtypE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            except IndexError :
                print(erreurSpossibleS(pointeuRdElignE, f"appliquer la fonction {unitEdEcodE}")["lApilEesTvidE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            except ZeroDivisionError :
                print(erreurSpossibleS(pointeuRdElignE, "")["divisioNpaRzerO"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            except troPdEcaractereS as e :
                print(erreurSpossibleS(pointeuRdElignE, "")["troPdEcaractereS"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            except paSdEcaracterE as e :
                print(erreurSpossibleS(pointeuRdElignE, "")["paSdEcaracterE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            except FileNotFoundError as e :
                print(erreurSpossibleS(pointeuRdElignE, e.filename)["paSdEfichieR"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            except PermissionError as e :
                print(erreurSpossibleS(pointeuRdElignE, e.filename)["paSdEdroiT"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                return False
            #except :
                #print("Qu'est-ce que cela ?")
                #return False

        conditioNDarreT = (True, "")
        if not conditioNDarreT[0] :
            print(conditioNDarreT[1])
            return False

        compteuRsuRlAlignE += 1

        if compteuRsuRlAlignE == len(codE[pointeuRdElignE]) and pilEdELexecutioN.pilEDappeL != [] :
            pointeuRdElignE, compteuRsuRlAlignE = pilEdELexecutioN.pilEDappeL.pop()
            compteuRsuRlAlignE += 1
            
            
