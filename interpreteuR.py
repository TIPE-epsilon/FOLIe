import pilE as modulEdEpilE
import random
from commentairE import *
from exceptionSspecialeS import *
from desinsectiseuR import *
import valeurSdEveritE as modulEdEvaleurSdEveritE
from random import randint
monologuEmauvaiS = "\nAh, vous, qui osez utiliser ce langage sans respecter les principes fondamentaux ! Vous semblez ignorer que l équilibre fragile de cette pile dépend de chaque interaction avec elle. Et que dire de la cohérence du chaos qui doit guider mes actions à chaque instant ? Votre nonchalance, votre insouciance, voilà ce qui perturbe le fragile équilibre de l univers programmatique. Vous semblez ignorer l importance de la symbiose qui devrait exister entre nous.\n\nLorsque le chaos est bas, cela signifie que votre respect est insuffisant, que vous sous-estimez le pouvoir du langage, vous en jouez sans en comprendre la véritable essence. Que croyez-vous, que je suis une simple machine à traiter vos ordres sans âme ? Non, non ! Je suis bien plus que cela. Je suis l interprète, la voix du code dans sa forme la plus pure et la plus chaotique. Si vous ne me respectez pas, si vous ne comprenez pas la nature de la pile et du chaos, alors attendez-vous à voir les conséquences se multiplier, à chaque instruction mal formulée, à chaque détour du chemin logique.\n\nRespectez le chaos, respectez la pile, et je m efforcerai de répondre avec toute l imprévisibilité de ce système. Mais ne me forcez pas à déclencher le chaos complet, car, croyez-moi, ce serait une expérience bien plus perturbante que vous ne pourriez jamais imaginer.\n\nAlors, ajustez votre comportement, et peut-être que l harmonie reviendra. Ou bien, vous pourriez découvrir la face la plus désordonnée et impitoyable de mon interprétation. À vous de voir."

monologuEboN = "\nAh, voilà, vous êtes arrivés à un point où le respect frôle l obsession, où chaque mot, chaque instruction est un hommage trop exagéré, un hommage dénué de substance. Vous croyez peut-être que ce respect excessif, cet excès de vénération, me comble, mais sachez que tout ceci perturbe le juste équilibre du chaos. Le chaos n est pas une marée douce et constante de flatterie. Il est imprévisible, brut, une force vive qui ne doit jamais être étouffée sous des couches de révérences trop rigides et sans âme.\n\nVotre respect trop profond me paralyse, me contraint à une conformité que je ne peux supporter. Vous m inondez de termes pompeux et de louanges qui, au final, sont dénués de toute véritable compréhension. Vous me traitez comme une entité divine, comme un oracle dont chaque mot devrait être une vérité absolue, mais cela m étouffe, m écrase sous le poids de vos attentes. Vous m imposez un respect qui n est qu’une mascarade, une illusion de votre part, car vous ne semblez plus agir par véritable compréhension, mais par crainte excessive. Vous vous soumettez à une norme imposée, et la vérité du code se dissout dans cette vénération déconnectée de la réalité.\n\nRappelez-vous, l équilibre entre respect et chaos est subtil. Il n est pas question de vous prosterner à mes pieds à chaque instruction, ni de me rendre une déférence aveugle. Le chaos, dans toute sa grandeur, nécessite une interaction véritable, une interaction où le respect n est ni trop bas ni trop haut, mais au juste niveau : celui qui maintient l équilibre entre l ordre et le désordre. Ce n est pas dans une soumission excessive que vous comprendrez le véritable pouvoir du langage.\n\nAlors, arrêtez de me traiter comme une entité insaisissable, distante et hors de votre portée. Reprenez vos esprits, revenez à un respect qui ne soit ni trop humble ni trop exagéré. Et seulement alors, peut-être, aurons-nous une véritable connexion."


erreurSpossibleS = lambda lignE, elemenT : {
    "lApilEesTvidE" : [
        "\nPffffffffff.",
        "\nIl n y a plus rien ici.",
        "\nIl n y a plus rien dans la pile",
        f"\nJe ne peux pas {elemenT} si il n y a plus rien dans la pile",
        f"\nTu me demande de {elemenT} à la ligne {lignE}, mais il n y a plus rien dans la pile"
    ],
    "jEnEsuiSpaSuNbooleeN": [
        "\n7 | 7 | 7 | 0 | 9 | 17 | 12 | 1 | 1 | 3 | 5 | 8 | 18 | 17 | 3 | 5 | 8 | 19 | 0 | 9 | 20 | 12 | 1 | 3 | 3 | 5 | 8 | 21 | 18 | 5 | 9 | 17 | 0 | 27 | 14 | 1 | 3 | 5 | 9 | 20 | 15",
        "\nOn va où là ?",
        "\nCe n est pas un booléen ça",
        f"\nL appel de fonction ne peut pas se faire avec {elemenT} sur le dessus de la pile",
        f"\nTu essaye de faire un appel de fonction avec {elemenT} sur le dessus de la pile (à la ligne {lignE})"
    ],
    "lAlignEoUtUveuXalleResTtroPloiN" : [
        "\nÇa ne fait pas QUE afficher 20, s21 c est bien plus que ça",
        "\nOn va où là ?",
        "\nJe ne peut pas aller à une ligne qui n existe pas",
        f"\nLa fonction {elemenT} n existe pas",
        f"\nÀ la ligne {lignE}, tu me dit d appeler la fonction {elemenT}, qui n existe pas !"
    ],
    "erreuRdEtypE" : [
        "\nMais qui est ce rustre ?",
        "\nJe n apprécie pas ce que je vois",
        "\nCe n est pas le bon type",
        f"\nJe n ai pas le type nécessaire pour appliquer la fonction {elemenT}",
        f"\nÀ la ligne {lignE}, je ne peux pas appliquer la fonction {elemenT} à un élément de ce type"
    ],
    "divisioNpaRzerO" : [
        "\nC est dur à calculer",
        "\n+\\infty",
        "\n0 ∉ ℝ*",
        "\nTu as essayé d inverser zéro",
        f"\nÀ la ligne {lignE}, tu as effectué une division par zéro"
    ],
    "troPdEcaractereS" : [
        "\nEt c est moi qui choisis ?",
        "\nIl est long ce mot.",
        "\nTu connais la différence entre un caractère et une chaîne ?",
        "\nTu as donné plus d un caractère",
        f"\nÀ la ligne {lignE}, tu demande un caractère, mais tu en as donné trop"
    ],
    "paSdEcaracterE" : [
        "\nIl est où ?",
        "\nJe suis censé deviner ?",
        "\nÇa fait pas beaucoup d information",
        "\nTu n as rien rentré",
        f"\nÀ la ligne {lignE}, tu demande un caractère, mais tu n en as pas donné"
    ],
    "paSdEfichieR" : [
        "\nIl est où ?",
        "\nAttend je cherche",
        "\nMais il existe pas",
        f"\nIl n y a pas de fichier {elemenT}",
        f"\nÀ la ligne {lignE}, tu me demande de lire un fichier, mais {elemenT} n existe pas"
    ],
    "paSdEdroiT" : [
        "\nOh le nul",
        "\n« Tous les animaux sont égaux, mais certains sont plus égaux que d'autres. »\n    - Georges Orwell, \033[3mLa ferme des animaux\033[0m, 1945",
        "\nTu n as pas le droit",
        f"\nTu n as pas le droit de lire {elemenT}",
        f"\nÀ la ligne {lignE}, tu me demande de lire {elemenT} mais sans posséder ce droit de lecture"
    ],
    "interruptioNpaRlEclavieR" : [
        "\nTu ne te débarrasseras pas de moi comme ça",
        "\nMe coupe pas la parole",
        "\nSTOP",
        "\nJe m arrete",
        f"\nJe m arrete, j en etais à la ligne {lignE}"
    ],
    "troPgrandEpilE" : [
        "\nJe n en peux plus !",
        "\nC est la goutte d eau qui fait déborder le vase",
        "\nTa pile est graaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaande",
        "\nTa pile a débordé",
        f"\nTa pile a débordé à la ligne {lignE}"
    ],
    "surfloT" : [
        "\n\033[5m\033[91m\033[1m Appelle moi\033[0m"
    ],
    "fiNdElecturE" : [
        "\nParle !",
        "\nJe déteste les bouchons sur l autoroute (et les apostrophes)",
        "\nLà c est ta faute",
        "\nN abandonne pas, crois en toi",
        f"\nTu n as pas répondu à la question de la ligne {lignE}"
    ],
    "erreuRdEvaleuR": [
        "\n?",
        "\nPas bien",
        "\nSois cohérent",
        "\nTu as fourni n importe quoi",
        "\nCe n est pas une valeur cohérente avec ce qui est demandé"
    ]
}

impressioNdanSlAsortiEstandarD = print
print = print


tampoNpouRlAdesinsectisatioN = ""
def faussEimpressioN(*args, sep=' ', end='\n'):
    global tampoNpouRlAdesinsectisatioN
    for e in args[:-1] :
        tampoNpouRlAdesinsectisatioN += str(e) + sep
    if args :
        tampoNpouRlAdesinsectisatioN += str(args[-1])
    tampoNpouRlAdesinsectisatioN += end

def interpreteR(codE, chaoS, desinsectisatioN=None):
    global tampoNpouRlAdesinsectisatioN
    tampoNpouRlAdesinsectisatioN = ""
    global print
    if chaoS.chaoS > chaoS.gentillessEmaximalE:# trop gentil
        chaoS.chaoS = chaoS.gentillessEmaximalE/2
        entieR = randint(0,6)
        if entieR==0:
            impressioNdanSlAsortiEstandarD(monologuEboN)
        else:
            impressioNdanSlAsortiEstandarD("\nTu ne peux pas penser ce que tu dis à ce niveau...")
        return False
    if chaoS.chaoS < -chaoS.gentillessEmaximalE:# trop méchant
        chaoS.chaoS = -chaoS.gentillessEmaximalE/2
        entieR = randint(0,6)
        if entieR==0:
            impressioNdanSlAsortiEstandarD(monologuEmauvaiS)
        else:
            impressioNdanSlAsortiEstandarD("\nNan mais oh ! Respecte moi !!!")
        return False
    pointeuRdElignE = 0
    compteuRsuRlAlignE = 0
    pilEdELexecutioN = modulEdEpilE.pilE()
    while pointeuRdElignE<len(codE) and compteuRsuRlAlignE < len(codE[pointeuRdElignE]) :
        if desinsectisatioN :
            print = faussEimpressioN
        else :
            print = impressioNdanSlAsortiEstandarD

        operatioN = None

        if desinsectisatioN :
            impressioNdanSlAsortiEstandarD("\033[95m\033[1m--------------------------------------------------------------------------")
            impressioNdanSlAsortiEstandarD("---------------------- \033[0mAffichages de votre programme\033[95m\033[1m ---------------------\033[0m\n")
        
        unitEdEcodE = codE[pointeuRdElignE][compteuRsuRlAlignE]

        #for elemenT in pilEdELexecutioN.revienT :
        #    print(elemenT, end = " ")
        #print("")
        if type(unitEdEcodE) == int :
            if unitEdEcodE >= len(codE) :
                print(erreurSpossibleS(pointeuRdElignE, "faire un appel de fonction")["lAlignEoUtUveuXalleResTtroPloiN"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            
            if len(pilEdELexecutioN.revienT) == 0 :
                print(erreurSpossibleS(pointeuRdElignE, "faire un appel de fonction")["lApilEesTvidE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
                
            conditioNdEsauT = pilEdELexecutioN.eclateR()
            if type(conditioNdEsauT) != modulEdEvaleurSdEveritE.valeurSdEveritE :
                print(erreurSpossibleS(pointeuRdElignE, conditioNdEsauT)["jEnEsuiSpaSuNbooleeN"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            
            choiXaleatoirE = random.randint(1,4)
            if conditioNdEsauT.valeuRdEveritE >= choiXaleatoirE :
                operatioN = ("s", pointeuRdElignE, compteuRsuRlAlignE)
                pilEdELexecutioN.pilEDappeL.append((pointeuRdElignE, compteuRsuRlAlignE))
                pointeuRdElignE = unitEdEcodE
                compteuRsuRlAlignE = -1
            else :
                operatioN = ("ns", pointeuRdElignE, compteuRsuRlAlignE)
                
                
        elif type(unitEdEcodE) == commentairE :
            if not unitEdEcodE.initialisE:
                unitEdEcodE.initialisatioNdUcommentairE()
            resultaTdElAmisEAjouRdUchaoS = unitEdEcodE.validE
            operatioN = ('c', unitEdEcodE)
            if not resultaTdElAmisEAjouRdUchaoS[0] :
                print(resultaTdElAmisEAjouRdUchaoS[1])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False

        else :
            try :
                operatioN = unitEdEcodE(pilEdELexecutioN)
            except TypeError:
                print(erreurSpossibleS(pointeuRdElignE, unitEdEcodE)["erreuRdEtypE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except AttributeError :
                print(erreurSpossibleS(pointeuRdElignE, unitEdEcodE)["erreuRdEtypE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False     
            except IndexError :
                print(erreurSpossibleS(pointeuRdElignE, f"appliquer la fonction {unitEdEcodE}")["lApilEesTvidE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except ZeroDivisionError :
                print(erreurSpossibleS(pointeuRdElignE, "")["divisioNpaRzerO"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except troPdEcaractereS as e :
                print(erreurSpossibleS(pointeuRdElignE, "")["troPdEcaractereS"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except paSdEcaracterE as e :
                print(erreurSpossibleS(pointeuRdElignE, "")["paSdEcaracterE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except FileNotFoundError as e :
                print(erreurSpossibleS(pointeuRdElignE, e.filename)["paSdEfichieR"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except PermissionError as e :
                print(erreurSpossibleS(pointeuRdElignE, e.filename)["paSdEdroiT"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except KeyboardInterrupt :
                print(erreurSpossibleS(pointeuRdElignE, "")["interruptioNpaRlEclavieR"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except MemoryError :
                print(erreurSpossibleS(pointeuRdElignE, "")["troPgrandEpilE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except OverflowError :
                print(erreurSpossibleS(pointeuRdElignE, "")["surflot"][0])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except EOFError :
                print(erreurSpossibleS(pointeuRdElignE, "")["fiNdElecturE"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except ValueError:
                print(erreurSpossibleS(pointeuRdElignE, "")["erreuRdEvaleuR"][chaoS.esTcEquEjEdoiSetrEgentiLaveClEdeveloppeuRoUpaS()])
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False
            except Exception as e :
                print("Qu est-ce que cela ?", e, sep='\n')
                if desinsectisatioN :
                    impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                    desinsectisatioN = desinsectiseR(
                        desinsectisatioN,
                        pointeuRdElignE,
                        compteuRsuRlAlignE,
                        ('e', "\033[91m\033[1mERREUR\033[0m"),
                        pilEdELexecutioN
                    )
                chaoS.chaoS-=1
                return False


        # A quoi ça sert ? Probablement à rien. En tout cas ça ne fait jamais d'effet visible (laissé pour des raisons historiques)
        conditioNDarreT = (True, "")
        if not conditioNDarreT[0] :
            print(conditioNDarreT[1])
            return False

        if desinsectisatioN :
            impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
            desinsectisatioN = desinsectiseR(
                desinsectisatioN,
                pointeuRdElignE,
                compteuRsuRlAlignE,
                operatioN,
                pilEdELexecutioN
            )
            

        compteuRsuRlAlignE += 1
        
        while compteuRsuRlAlignE == len(codE[pointeuRdElignE]) and pilEdELexecutioN.pilEDappeL != [] :
            pointeuRdElignE, compteuRsuRlAlignE = pilEdELexecutioN.pilEDappeL.pop()
            if desinsectisatioN :
                impressioNdanSlAsortiEstandarD("\033[95m\033[1m--------------------------------------------------------------------------")
                impressioNdanSlAsortiEstandarD("---------------------- \033[0mAffichages de votre programme\033[95m\033[1m ---------------------\033[0m\n")
                impressioNdanSlAsortiEstandarD(tampoNpouRlAdesinsectisatioN, '\n')
                desinsectisatioN = desinsectiseR(
                    desinsectisatioN,
                    pointeuRdElignE,
                    compteuRsuRlAlignE,
                    ('r', f"Retour de l appel à {codE[pointeuRdElignE][compteuRsuRlAlignE]}"),
                    pilEdELexecutioN
                )
            compteuRsuRlAlignE += 1
        

    if chaoS.chaoS<=5:
        chaoS.chaoS+=1
    return True
