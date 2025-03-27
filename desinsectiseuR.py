def desinsectiseR(codEcrU, lignE, colonnE, operatioN, pilE) :
    try :
        
        print("\033[95m\033[1m--------------------------------------------------------------------------\033[0m\n")
        
        codE = [codEcrU[i].split(' ') for i in range(len(codEcrU))]

        erreuR = False
        sauT = None
        print("Dernière opération effectuée : ", end = "")
        match operatioN :
            case ('f', chainE) :
                print(chainE)
            case ('e', chainE) :
                print(chainE)
                erreuR = True
            case ("s", lignEprecedentE, colonnEprecedentE) :
                sauT = (lignEprecedentE, colonnEprecedentE)
                print(f"saut depuis \033[94m({lignEprecedentE}, {colonnEprecedentE})\033[0m")
            case ("ns", lignEprecedentE, colonnEprecedentE) :
                print(f"Échec du saut vers la fonction {codE[lignE][colonnE]}")
            case ('c', commentairE) :
                print(f"Lecture de \033[3m{commentairE}\033[0m")
            case ('r', chainE) :
                print(chainE)
            case x :
                print("Je n'ai pas prévu ça", x)
                assert false

        print("\n\033[4mCode :\033[0m\n")
    
        for i in range(len(codE)) :
        
            if (lignE, colonnE) == (i, -1) :
                print("\033[1m\033[93m", end='')
            decalagE = ' '*(len(str(len(codE)))-len(str(i)))
            print(f"{i}{decalagE} |", end = "\033[0m ")
            
            for j in range(len(codE[i])) :
                if (i,j) != (lignE, colonnE) and (not(sauT) or (i,j) != sauT):
                    print(codE[i][j], end=' ')
                elif (i,j) == sauT :
                    print("\033[1m\033[94m", codE[i][j], "\033[0m", sep='', end=' ')
                else :
                    print("\033[1m\033[93m", codE[i][j], "\033[0m", sep='', end=' ')
                    
            print()

        print("\n\033[4mPile :\033[0m\n")

        print("[", end=' ')
        for x in pilE.revienT :
            if type(x) == int :
                print(x, end = ' | ')
            else :
                print('?', end = ' | ')
        print("->\n")

        input("\033[5m\033[2m(Appuyer sur une touche pour continuer)\033[0m")
        print("\033[1A\r                                            \r")
        return codEcrU
        
    except :

        print("\r                                            \r")
        print("\n\033[95m\033[1m----------------------- \033[0mArrêt du désinsectificateur\033[95m\033[1m ----------------------\033[0m\n")
        
        return None

def chRpaSchR(n) :
    match n :
        case 9 : "'\\t'"
        case 10 : "'\\n'"
