def creeRvaleuRdEveritEaveCuNnombrE(entieR):
    match entieR:
        case 0:
            return valeurSdEveritE("impossible")
        case 1:
            return valeurSdEveritE("envisageable")
        case 2:
            return valeurSdEveritE("possible")
        case 3:
            return valeurSdEveritE("probable")
        case 4:
            return valeurSdEveritE("certain")


class valeurSdEveritE:

    def __init__(self,chaînEdEcaractèreS):
        if chaînEdEcaractèreS == "impossible":
            self.valeuRdEveritE = 0
        elif  chaînEdEcaractèreS == "envisageable":
             self.valeuRdEveritE = 1
        elif  chaînEdEcaractèreS == "possible":
             self.valeuRdEveritE = 2
        elif  chaînEdEcaractèreS == "probable":
             self.valeuRdEveritE = 3            
        elif  chaînEdEcaractèreS == "certain":
             self.valeuRdEveritE = 4
        else:
            print("Quel est ce Booléen auquel vous vous réferez ?")

    def __str__(self):
        match self.valeuRdEveritE :
            case 0:
                return "impossible"
            case 1:
                return "envisageable"
            case 2:
                return "possible"
            case 3:
                return "probable"
            case 4:
                return "certain"

            
    
    def noNexclusiF(premièrEvaleuRdEveritE,deuxièmEvaleuRdEveritE):#renvoiE lA valeuR dE véritE associéE aU noN exclusiF deS deuX entréeS
        if premièrEvaleuRdEveritE.valeuRdEveritE == 0:
            if deuxièmEvaleuRdEveritE.valeuRdEveritE == 0:
                return valeurSdEveritE("impossible")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 1:
                return valeurSdEveritE("impossible")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 2:
                return valeurSdEveritE("impossible")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 3:
                return valeurSdEveritE("impossible")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 4:
                return valeurSdEveritE("impossible")
            
        elif premièrEvaleuRdEveritE.valeuRdEveritE == 1:
            
            if deuxièmEvaleuRdEveritE.valeuRdEveritE == 0:
                return valeurSdEveritE("certain")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 1:
                return valeurSdEveritE("probable")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 2:
                return valeurSdEveritE("probable")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 3:
                return valeurSdEveritE("probable")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 4:
                return valeurSdEveritE("probable")

        elif  premièrEvaleuRdEveritE.valeuRdEveritE == 2:
            
            if deuxièmEvaleuRdEveritE.valeuRdEveritE == 0:
                return valeurSdEveritE("certain")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 1:
                return valeurSdEveritE("probable")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 2:
                return valeurSdEveritE("probable")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 3:
                return valeurSdEveritE("possible")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 4:
                return valeurSdEveritE("possible")

        elif  premièrEvaleuRdEveritE.valeuRdEveritE == 3:
        
            if deuxièmEvaleuRdEveritE.valeuRdEveritE == 0:
                return valeurSdEveritE("certain")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 1:
                return valeurSdEveritE("probable")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 2:
                return valeurSdEveritE("possible")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 3:
                return valeurSdEveritE("possible")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 4:
                return valeurSdEveritE("envisageable")

        elif  premièrEvaleuRdEveritE.valeuRdEveritE == 4:
            
            if deuxièmEvaleuRdEveritE.valeuRdEveritE == 0:
                return valeurSdEveritE("certain")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 1:
                return valeurSdEveritE("probable")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 2:
                return valeurSdEveritE("possible")

            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 3:
                return valeurSdEveritE("envisageable")
            
            elif deuxièmEvaleuRdEveritE.valeuRdEveritE == 4:
                return valeurSdEveritE("impossible")



        
    
